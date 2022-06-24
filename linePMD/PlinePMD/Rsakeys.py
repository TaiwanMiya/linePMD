import math
import os
import struct
import typing
import logging
import base64
import warnings
from threading import Lock
from pyasn1.type import univ, namedtype
from pyasn1 import error
from multiprocessing.connection import Connection
import multiprocessing as mp
from hmac import compare_digest

log = logging.getLogger(__name__)
FlexiText = typing.Union[str, bytes]
DEFAULT_EXPONENT = 65535

class AbstractKeyPMD:

    __slots__ = ("n", "e", "blindfac", "blindfac_inverse", "mutex")

    def __init__(self, n: int, e: int) -> None:
        self.n = n
        self.e = e
        self.blindfac = self.blindfac_inverse = -1
        self.mutex = Lock()

    @classmethod
    def _load_pkcs1_pem(cls, keyfile: bytes) -> "AbstractKeyPMD":
        der = CryptographyPMD.load_pem(keyfile, "RSA PUBLIC KEY")
        return cls._load_pkcs1_der(der)

    @classmethod
    def _load_pkcs1_der(cls, keyfile: bytes) -> "AbstractKeyPMD":
        from pyasn1.codec.der import decoder
        (priv, _) = decoder.decode(keyfile, asn1Spec=AsnPubKey())
        return cls(n=int(priv["modulus"]), e=int(priv["publicExponent"]))

    def _save_pkcs1_pem(self) -> bytes:...

    def _save_pkcs1_der(self) -> bytes:...

    @classmethod
    def load_pkcs1(cls, keyfile: bytes, format: str = "PEM") -> "AbstractKeyPMD":
        methods = {
            "PEM": cls._load_pkcs1_pem,
            "DER": cls._load_pkcs1_der,
        }

        method = cls._assert_format_exists(format, methods)
        return method(keyfile)

    @staticmethod
    def _assert_format_exists(file_format: str, methods: typing.Mapping[str, typing.Callable]) -> typing.Callable:
        try:
            return methods[file_format]
        except KeyError as ex:
            formats = ", ".join(sorted(methods.keys()))
            raise ValueError("Unsupported format: %r, try one of %s" % (file_format, formats)) from ex

    def _update_blinding_factor(self) -> typing.Tuple[int, int]:
        with self.mutex:
            if self.blindfac < 0:
                self.blindfac = self._initial_blinding_factor()
                self.blindfac_inverse = CryptographyPMD.inverse(self.blindfac, self.n)
            else:
                self.blindfac = pow(self.blindfac, 2, self.n)
                self.blindfac_inverse = pow(self.blindfac_inverse, 2, self.n)

            return self.blindfac, self.blindfac_inverse

    def save_pkcs1(self, format: str = "PEM") -> bytes:
        methods = {
            "PEM": self._save_pkcs1_pem,
            "DER": self._save_pkcs1_der,
        }

        method = self._assert_format_exists(format, methods)
        return method()

    def blind(self, message: int) -> typing.Tuple[int, int]:
        blindfac, blindfac_inverse = self._update_blinding_factor()
        blinded = (message * pow(blindfac, self.e, self.n)) % self.n
        return blinded, blindfac_inverse

    def unblind(self, blinded: int, blindfac_inverse: int) -> int:
        return (blindfac_inverse * blinded) % self.n

    def _initial_blinding_factor(self) -> int:
        for _ in range(1000):
            blind_r = CryptographyPMD.randint(self.n - 1)
            if CryptographyPMD.are_relatively_prime(self.n, blind_r):
                return blind_r
        raise RuntimeError("unable to find blinding factor ^^")

    def _update_blinding_factor(self) -> typing.Tuple[int, int]:
        with self.mutex:
            if self.blindfac < 0:
                self.blindfac = self._initial_blinding_factor()
                self.blindfac_inverse = CryptographyPMD.inverse(self.blindfac, self.n)
            else:
                self.blindfac = pow(self.blindfac, 2, self.n)
                self.blindfac_inverse = pow(self.blindfac_inverse, 2, self.n)
            return self.blindfac, self.blindfac_inverse

class PublicKeyPMD(AbstractKeyPMD):

    __slots__ = ('n', 'e')

    def __getitem__(self, key: str) -> int:return getattr(self, key)

    def __repr__(self) -> str:return "PublicKey(n=%i, e=%i)" % (self.n, self.e)

    def __getstate__(self) -> typing.Tuple[int, int]:return self.n, self.e

    def __setstate__(self, state: typing.Tuple[int, int]) -> None:
        self.n, self.e = state
        AbstractKeyPMD.__init__(self, self.n, self.e)

    def __eq__(self, other: typing.Any) -> bool:
        if other is None:return False
        if not isinstance(other, PublicKeyPMD):return False
        return self.n == other.n and self.e == other.e

    def __ne__(self, other: typing.Any) -> bool:return not (self == other)

    def __hash__(self) -> int:return hash((self.n, self.e))

    def _save_pkcs1_pem(self) -> bytes:

        der = self._save_pkcs1_der()
        return CryptographyPMD.save_pem(der, "RSA PUBLIC KEY")

    def _save_pkcs1_der(self) -> bytes:
        from pyasn1.codec.der import encoder
        asn_key = AsnPubKey()
        asn_key.setComponentByName("modulus", self.n)
        asn_key.setComponentByName("publicExponent", self.e)
        return encoder.encode(asn_key)

    @classmethod
    def _load_pkcs1_pem(cls, keyfile: bytes) -> "PublicKeyPMD":

        der = CryptographyPMD.load_pem(keyfile, "RSA PUBLIC KEY")
        return cls._load_pkcs1_der(der)
    
    @classmethod
    def _load_pkcs1_der(cls, keyfile: bytes) -> "PublicKeyPMD":
        from pyasn1.codec.der import decoder

        (priv, _) = decoder.decode(keyfile, asn1Spec=AsnPubKey())
        return cls(n=int(priv["modulus"]), e=int(priv["publicExponent"]))

    @classmethod
    def load_pkcs1_openssl_pem(cls, keyfile: bytes) -> "PublicKeyPMD":
        der = CryptographyPMD.load_pem(keyfile, "PUBLIC KEY")
        return cls.load_pkcs1_openssl_der(der)

    @classmethod
    def load_pkcs1_openssl_der(cls, keyfile: bytes) -> "PublicKeyPMD":
        from pyasn1.codec.der import decoder
        from pyasn1.type import univ

        (keyinfo, _) = decoder.decode(keyfile, asn1Spec=OpenSSLPubKey())

        if keyinfo["header"]["oid"] != univ.ObjectIdentifier("1.2.840.113549.1.1.1"):
            raise TypeError("This is not a DER-encoded OpenSSL-compatible public key ^^")

        return cls._load_pkcs1_der(keyinfo["key"][1:])



class PrivateKeyPMD(AbstractKeyPMD):

    __slots__ = ("n", "e", "d", "p", "q", "exp1", "exp2", "coef")

    def __init__(self, n: int, e: int, d: int, p: int, q: int) -> None:
        AbstractKeyPMD.__init__(self, n, e)
        self.d = d
        self.p = p
        self.q = q
        self.exp1 = int(d % (p - 1))
        self.exp2 = int(d % (q - 1))
        self.coef = CryptographyPMD.inverse(q, p)

    def __getitem__(self, key: str) -> int:
        return getattr(self, key)

    def __repr__(self) -> str:
        return "PrivateKey(n=%i, e=%i, d=%i, p=%i, q=%i)" % (self.n, self.e, self.d, self.p, self.q)

    def __getstate__(self) -> typing.Tuple[int, int, int, int, int, int, int, int]:
        return self.n, self.e, self.d, self.p, self.q, self.exp1, self.exp2, self.coef

    def __setstate__(self, state: typing.Tuple[int, int, int, int, int, int, int, int]) -> None:
        self.n, self.e, self.d, self.p, self.q, self.exp1, self.exp2, self.coef = state
        AbstractKeyPMD.__init__(self, self.n, self.e)

    def __eq__(self, other: typing.Any) -> bool:
        if other is None:
            return False

        if not isinstance(other, PrivateKeyPMD):
            return False

        return (
            self.n == other.n
            and self.e == other.e
            and self.d == other.d
            and self.p == other.p
            and self.q == other.q
            and self.exp1 == other.exp1
            and self.exp2 == other.exp2
            and self.coef == other.coef
        )

    def __ne__(self, other: typing.Any) -> bool:
        return not (self == other)

    def __hash__(self) -> int:
        return hash((self.n, self.e, self.d, self.p, self.q, self.exp1, self.exp2, self.coef))

    def _save_pkcs1_pem(self) -> bytes:

        der = self._save_pkcs1_der()
        return CryptographyPMD.save_pem(der, b"RSA PRIVATE KEY")

    def _save_pkcs1_der(self) -> bytes:
        from pyasn1.type import univ, namedtype
        from pyasn1.codec.der import encoder
        class AsnPrivKey(univ.Sequence):
            componentType = namedtype.NamedTypes(
                namedtype.NamedType("version", univ.Integer()),
                namedtype.NamedType("modulus", univ.Integer()),
                namedtype.NamedType("publicExponent", univ.Integer()),
                namedtype.NamedType("privateExponent", univ.Integer()),
                namedtype.NamedType("prime1", univ.Integer()),
                namedtype.NamedType("prime2", univ.Integer()),
                namedtype.NamedType("exponent1", univ.Integer()),
                namedtype.NamedType("exponent2", univ.Integer()),
                namedtype.NamedType("coefficient", univ.Integer()),
            )
        asn_key = AsnPrivKey()
        asn_key.setComponentByName("version", 0)
        asn_key.setComponentByName("modulus", self.n)
        asn_key.setComponentByName("publicExponent", self.e)
        asn_key.setComponentByName("privateExponent", self.d)
        asn_key.setComponentByName("prime1", self.p)
        asn_key.setComponentByName("prime2", self.q)
        asn_key.setComponentByName("exponent1", self.exp1)
        asn_key.setComponentByName("exponent2", self.exp2)
        asn_key.setComponentByName("coefficient", self.coef)
        return encoder.encode(asn_key)

    @classmethod
    def _load_pkcs1_pem(cls, keyfile: bytes) -> "PrivateKeyPMD":

        der = CryptographyPMD.load_pem(keyfile, b"RSA PRIVATE KEY")
        return cls._load_pkcs1_der(der)

    @classmethod
    def _load_pkcs1_der(cls, keyfile: bytes) -> "PrivateKeyPMD":
        from pyasn1.codec.der import decoder

        (priv, _) = decoder.decode(keyfile)
        if priv[0] != 0:
            raise ValueError("Unable to read this file, version %s != 0" % priv[0])

        as_ints = map(int, priv[1:6])
        key = cls(*as_ints)

        exp1, exp2, coef = map(int, priv[6:9])

        if (key.exp1, key.exp2, key.coef) != (exp1, exp2, coef):
            warnings.warn(
                "You have provided a malformed keyfile. Either the exponents "
                "or the coefficient are incorrect. Using the correct values "
                "instead ><",
                UserWarning,
            )

        return key

    def blinded_decrypt(self, encrypted: int) -> int:
        blinded, blindfac_inverse = self.blind(encrypted)
        s1 = pow(blinded, self.exp1, self.p)
        s2 = pow(blinded, self.exp2, self.q)
        h = ((s1 - s2) * self.coef) % self.p
        decrypted = s2 + self.q * h
        return self.unblind(decrypted, blindfac_inverse)

class CryptographyPMD:

    def EncryptionPMD(message: bytes, pub_key: PublicKeyPMD) -> bytes:
        keylength = CryptographyPMD.ByteSize(pub_key.n)
        padded = CryptographyPMD.PadForEncryption(message, keylength)
        payload = CryptographyPMD.Bytes2Int(padded)
        encrypted = CryptographyPMD.EncryptInt(payload, pub_key.e, pub_key.n)
        block = CryptographyPMD.Int2Bytes(encrypted, keylength)
        return block

    def DecryptionPMD(crypto: bytes, priv_key: PrivateKeyPMD) -> bytes:
        blocksize = CryptographyPMD.ByteSize(priv_key.n)
        encrypted = CryptographyPMD.Bytes2Int(crypto)
        decrypted = priv_key.blinded_decrypt(encrypted)
        cleartext = CryptographyPMD.Int2Bytes(decrypted, blocksize)
        if len(crypto) > blocksize:
            raise DecryptionError("Decryption failed ><")
        cleartext_marker_bad = not compare_digest(cleartext[:2], b"\x00\x02")
        sep_idx = cleartext.find(b"\x00", 2)
        sep_idx_bad = sep_idx < 10
        anything_bad = cleartext_marker_bad | sep_idx_bad
        if anything_bad:
            raise DecryptionError("Decryption failed ><")
        return cleartext[sep_idx + 1 :]

    def ByteSize(number: int) -> int:
        if number == 0:
            return 1
        return CryptographyPMD.CeilDiv(CryptographyPMD.BitSize(number), 8)

    def BitSize(num: int) -> int:
        try:
            return num.bit_length()
        except AttributeError as ex:
            raise TypeError("BitSize(num) only supports integers, not %r ~" % type(num)) from ex

    def CeilDiv(num: int, div: int) -> int:
        quanta, mod = divmod(num, div)
        if mod:
            quanta += 1
        return quanta

    def PadForEncryption(message: bytes, target_length: int) -> bytes:
        max_msglength = target_length - 11
        msglength = len(message)
        if msglength > max_msglength:
            raise OverflowError(
                "%i bytes needed for message, but there is only space for %i ~" % (msglength, max_msglength))
        padding = b""
        padding_length = target_length - msglength - 3
        while len(padding) < padding_length:
            needed_bytes = padding_length - len(padding)
            new_padding = os.urandom(needed_bytes + 5)
            new_padding = new_padding.replace(b"\x00", b"")
            padding = padding + new_padding[:needed_bytes]
        assert len(padding) == padding_length
        return b"".join([b"\x00\x02", padding, b"\x00", message])
    
    def Bytes2Int(raw_bytes: bytes) -> int:
        return int.from_bytes(raw_bytes, "big", signed=False)

    def EncryptInt(message: int, ekey: int, n: int) -> int:
        CryptographyPMD.AssertInt(message, "message")
        CryptographyPMD.AssertInt(ekey, "ekey")
        CryptographyPMD.AssertInt(n, "n")
        if message < 0:
            raise ValueError("Only non-negative numbers are supported ^^")
        if message > n:
            raise OverflowError("The message %i is too long for n=%i ~" % (message, n))
        return pow(message, ekey, n)

    def AssertInt(var: int, name: str) -> None:
        if isinstance(var, int):
            return
        raise TypeError("%s should be an integer, not %s ~" % (name, var.__class__))

    def Int2Bytes(number: int, fill_size: int = 0) -> bytes:
        if number < 0:
            raise ValueError("Number must be an unsigned integer: %d ~" % number)
        bytes_required = max(1, math.ceil(number.bit_length() / 8))
        if fill_size > 0:
            return number.to_bytes(fill_size, "big")
        return number.to_bytes(bytes_required, "big")

    def inverse(x: int, n: int) -> int:
        (divider, inv, _) = CryptographyPMD.extended_gcd(x, n)
        if divider != 1:
            raise NotRelativePrimeError(x, n, divider)
        return inv

    def randint(maxvalue: int) -> int:
        bit_size = CryptographyPMD.BitSize(maxvalue)
        tries = 0
        while True:
            value = CryptographyPMD.read_random_int(bit_size)
            if value <= maxvalue:
                break
            if tries % 10 == 0 and tries:
                bit_size -= 1
            tries += 1
        return value

    def _markers(pem_marker: FlexiText) -> typing.Tuple[bytes, bytes]:
        if not isinstance(pem_marker, bytes):
            pem_marker = pem_marker.encode("ascii")
        return (
            b"-----BEGIN " + pem_marker + b"-----",
            b"-----END " + pem_marker + b"-----",
        )

    def _pem_lines(contents: bytes, pem_start: bytes, pem_end: bytes) -> typing.Iterator[bytes]:
        in_pem_part = False
        seen_pem_start = False
        for line in contents.splitlines():
            line = line.strip()
            if not line:
                continue
            if line == pem_start:
                if in_pem_part:
                    raise ValueError('Seen start marker "%r" twice ~' % pem_start)
                in_pem_part = True
                seen_pem_start = True
                continue
            if not in_pem_part:
                continue
            if in_pem_part and line == pem_end:
                in_pem_part = False
                break
            if b":" in line:
                continue
            yield line
        if not seen_pem_start:
            raise ValueError('No PEM start marker "%r" found ~' % pem_start)
        if in_pem_part:
            raise ValueError('No PEM end marker "%r" found ~' % pem_end)

    def load_pem(contents: FlexiText, pem_marker: FlexiText) -> bytes:
        if not isinstance(contents, bytes):
            contents = contents.encode("ascii")
        (pem_start, pem_end) = CryptographyPMD._markers(pem_marker)
        pem_lines = [line for line in CryptographyPMD._pem_lines(contents, pem_start, pem_end)]
        pem = b"".join(pem_lines)
        return base64.standard_b64decode(pem)

    def save_pem(contents: bytes, pem_marker: FlexiText) -> bytes:
        (pem_start, pem_end) = CryptographyPMD._markers(pem_marker)

        b64 = base64.standard_b64encode(contents).replace(b"\n", b"")
        pem_lines = [pem_start]

        for block_start in range(0, len(b64), 64):
            block = b64[block_start : block_start + 64]
            pem_lines.append(block)

        pem_lines.append(pem_end)
        pem_lines.append(b"")

        return b"\n".join(pem_lines)

    def read_random_int(nbits: int) -> int:
        randomdata = CryptographyPMD.read_random_bits(nbits)
        value = CryptographyPMD.Bytes2Int(randomdata)
        value |= 1 << (nbits - 1)
        return value

    def read_random_bits(nbits: int) -> bytes:
        nbytes, rbits = divmod(nbits, 8)
        randomdata = os.urandom(nbytes)
        if rbits > 0:
            randomvalue = ord(os.urandom(1))
            randomvalue >>= 8 - rbits
            randomdata = struct.pack("B", randomvalue) + randomdata
        return randomdata

    def extended_gcd(a: int, b: int) -> typing.Tuple[int, int, int]:
        x = 0
        y = 1
        lx = 1
        ly = 0
        oa = a
        ob = b
        while b != 0:
            q = a // b
            (a, b) = (b, a % b)
            (x, lx) = ((lx - (q * x)), x)
            (y, ly) = ((ly - (q * y)), y)
        if lx < 0:
            lx += ob
        if ly < 0:
            ly += oa
        return a, lx, ly

    def get_primality_testing_rounds(number: int) -> int:
        bitsize = CryptographyPMD.BitSize(number)
        if bitsize >= 1536:
            return 3
        if bitsize >= 1024:
            return 4
        if bitsize >= 512:
            return 7
        return 10

    def miller_rabin_primality_testing(n: int, k: int) -> bool:
        if n < 2:
            return False
        d = n - 1
        r = 0

        while not (d & 1):
            r += 1
            d >>= 1
        for _ in range(k):
            a = CryptographyPMD.randint(n - 3) + 1

            x = pow(a, d, n)
            if x == 1 or x == n - 1:
                continue

            for _ in range(r - 1):
                x = pow(x, 2, n)
                if x == 1:
                    return False
                if x == n - 1:
                    break
            else:
                return False

        return True

    def is_prime(number: int) -> bool:
        if number < 10:
            return number in {2, 3, 5, 7}
        if not (number & 1):
            return False
        k = CryptographyPMD.get_primality_testing_rounds(number)
        return CryptographyPMD.miller_rabin_primality_testing(number, k + 1)

    def read_random_odd_int(nbits: int) -> int:

        value = CryptographyPMD.read_random_int(nbits)

        return value | 1

    def _find_prime(nbits: int, pipe: Connection) -> None:
        while True:
            integer = CryptographyPMD.read_random_odd_int(nbits)

            if CryptographyPMD.is_prime(integer):
                pipe.send(integer)
                return

    def getprime(nbits: int, poolsize: int) -> int:
        (pipe_recv, pipe_send) = mp.Pipe(duplex=False)
        try:
            procs = [mp.Process(target=CryptographyPMD._find_prime, args=(nbits, pipe_send)) for _ in range(poolsize)]
            for p in procs:
                p.start()

            result = pipe_recv.recv()
        finally:
            pipe_recv.close()
            pipe_send.close()

        for p in procs:
            p.terminate()
        return result

    def getprime(nbits: int) -> int:
        assert nbits > 3

        while True:
            integer = CryptographyPMD.read_random_odd_int(nbits)

            if CryptographyPMD.is_prime(integer):
                return integer

    def find_p_q(nbits: int, getprime_func: typing.Callable[[int], int] = getprime, accurate: bool = True) -> typing.Tuple[int, int]:
        total_bits = nbits * 2

        shift = nbits // 16
        pbits = nbits + shift
        qbits = nbits - shift

        log.debug("find_p_q(%i): Finding p ^^", nbits)
        p = getprime_func(pbits)
        log.debug("find_p_q(%i): Finding q ^^", nbits)
        q = getprime_func(qbits)
        def is_acceptable(p: int, q: int) -> bool:
            if p == q:
                return False

            if not accurate:
                return True

            found_size = CryptographyPMD.BitSize(p * q)
            return total_bits == found_size

        change_p = False
        while not is_acceptable(p, q):
            if change_p:
                p = getprime_func(pbits)
            else:
                q = getprime_func(qbits)

            change_p = not change_p

        return max(p, q), min(p, q)

    def calculate_keys_custom_exponent(p: int, q: int, exponent: int) -> typing.Tuple[int, int]:
        phi_n = (p - 1) * (q - 1)

        try:
            d = CryptographyPMD.inverse(exponent, phi_n)
        except NotRelativePrimeError as ex:
            raise NotRelativePrimeError(exponent, phi_n, ex.d, msg="e (%d) and phi_n (%d) are not relatively prime (divider=%i)" % (exponent, phi_n, ex.d)) from ex

        if (exponent * d) % phi_n != 1:
            raise ValueError("e (%d) and d (%d) are not mult. inv. modulo " "phi_n (%d)" % (exponent, d, phi_n))

        return exponent, d

    def gcd(p: int, q: int) -> int:
        while q != 0:
            (p, q) = (q, p % q)
        return p

    def are_relatively_prime(a: int, b: int) -> bool:
        d = CryptographyPMD.gcd(a, b)
        return d == 1

    def gen_keys(nbits: int, getprime_func: typing.Callable[[int], int], accurate: bool = True, exponent: int = DEFAULT_EXPONENT) -> typing.Tuple[int, int, int, int]:
        while True:
            (p, q) = CryptographyPMD.find_p_q(nbits // 2, getprime_func, accurate)
            try:
                (e, d) = CryptographyPMD.calculate_keys_custom_exponent(p, q, exponent=exponent)
                break
            except ValueError:
                pass

        return p, q, e, d

    def newkeys(nbits: int, accurate: bool = True, poolsize: int = 1, exponent: int = DEFAULT_EXPONENT) -> typing.Tuple[PublicKeyPMD, PrivateKeyPMD]:
        if nbits < 16:
            raise ValueError("Key too small ><")
        if poolsize < 1:
            raise ValueError("Pool size (%i) should be >= 1" % poolsize)
        if poolsize > 1:
            def getprime_func(nbits: int) -> int:
                return CryptographyPMD.getprime(nbits, poolsize=poolsize)
        else:
            getprime_func = CryptographyPMD.getprime
        (p, q, e, d) = CryptographyPMD.gen_keys(nbits, getprime_func, accurate=accurate, exponent=exponent)
        n = p * q
        return (PublicKeyPMD(n, e), PrivateKeyPMD(n, e, d, p, q))

class AsnPubKey(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType("modulus", univ.Integer()),
        namedtype.NamedType("publicExponent", univ.Integer()),
    )

class Tag(object):
    def __init__(self, tagClass, tagFormat, tagId):
        if tagId < 0:
            raise error.PyAsn1Error('Negative tag ID (%s) not allowed ~' % tagId)
        self.__tagClass = tagClass
        self.__tagFormat = tagFormat
        self.__tagId = tagId
        self.__tagClassId = tagClass, tagId
        self.__hash = hash(self.__tagClassId)

    def __repr__(self):
        representation = '[%s:%s:%s]' % (
            self.__tagClass, self.__tagFormat, self.__tagId)
        return '<%s object, tag %s>' % (
            self.__class__.__name__, representation)

    def __eq__(self, other):
        return self.__tagClassId == other

    def __ne__(self, other):
        return self.__tagClassId != other

    def __lt__(self, other):
        return self.__tagClassId < other

    def __le__(self, other):
        return self.__tagClassId <= other

    def __gt__(self, other):
        return self.__tagClassId > other

    def __ge__(self, other):
        return self.__tagClassId >= other

    def __hash__(self):
        return self.__hash

    def __getitem__(self, idx):
        if idx == 0:
            return self.__tagClass
        elif idx == 1:
            return self.__tagFormat
        elif idx == 2:
            return self.__tagId
        else:
            raise IndexError()

    def __iter__(self):
        yield self.__tagClass
        yield self.__tagFormat
        yield self.__tagId

    def __and__(self, otherTag):
        return self.__class__(self.__tagClass & otherTag.tagClass,
                              self.__tagFormat & otherTag.tagFormat,
                              self.__tagId & otherTag.tagId)

    def __or__(self, otherTag):
        return self.__class__(self.__tagClass | otherTag.tagClass,
                              self.__tagFormat | otherTag.tagFormat,
                              self.__tagId | otherTag.tagId)

    @property
    def tagClass(self):
        return self.__tagClass

    @property
    def tagFormat(self):
        return self.__tagFormat

    @property
    def tagId(self):
        return self.__tagId

class PubKeyHeader(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType("oid", univ.ObjectIdentifier()),
        namedtype.NamedType("parameters", univ.Null()),
    )

class OpenSSLPubKey(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType("header", PubKeyHeader()),
        namedtype.NamedType(
            "key",
            univ.OctetString().subtype(implicitTag=Tag(tagClass=0, tagFormat=0, tagId=3)),
        ),
    )

class CryptoError(Exception):...

class DecryptionError(CryptoError):...

class VerificationError(CryptoError):...

class NotRelativePrimeError(ValueError):

    def __init__(self, a: int, b: int, d: int, msg: str = "") -> None:
        super().__init__(msg or "%d and %d are not relatively prime, divider=%i" % (a, b, d))
        self.a = a
        self.b = b
        self.d = d
