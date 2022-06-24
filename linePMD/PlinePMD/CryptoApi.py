from PlinePMD.Aeskeys import (
    AES_CTR,
    AES_CBC,
    AES_CFB,
    AES_OFB,
    AES_ECB,
    Encrypter,
    Decrypter
)
from PlinePMD.Deskeys import (
    DES,
    DES3,
    PAD_NORMAL,
    PAD_PKCS5,
    ECB,
    CBC
)
from PlinePMD.Rsakeys import (
    PublicKeyPMD,
    PrivateKeyPMD,
    CryptographyPMD
)
from base64 import (
    b16encode,
    b16decode,
    b32encode,
    b32decode,
    b64encode,
    b64decode,
    b85encode,
    b85decode
)
from json import (
    load,
    dump,
    loads,
    dumps
)
from PlinePMD.Canvas import Printf
import os
import enum
import binascii
import tempfile
import uuid

@enum.unique
class Encoding(enum.Enum):
    ASCII               = 1
    UTF8                = 2
    UTF16               = 3
    UTF32               = 4
    UTF7                = 5
    IDNA                = 6
    MBCS                = 7
    OEM                 = 8
    PALMOS              = 9
    PUNYCODE            = 10
    RAW_UNICODE_ESCAPE  = 11
    UNICODE_ESCAPE      = 12

@enum.unique
class Errors(enum.Enum):
    strict              = 0x01
    ignore              = 0x02
    replace             = 0x04
    backslashreplace    = 0x08
    surrogateescape     = 0x10
    xmlcharrefreplace   = 0x20
    namereplace         = 0x40
    surrogatepass       = 0x80

class File:

    def __init__(self,path,value=None) -> None:
        self.path = path
        self.value = value

    def read(self) -> str:
        with open(self.path,'rb') as reader:
            data = reader.read()
            reader.close()
            return data

    def write(self) -> None:
        if not self.value:
            raise ValueError('Writing a file requires a string')
        if isinstance(self.value,str):
            self.value = self.value.encode('utf-8')
        with open(self.path,'wb') as writer:
            writer.write(self.value)
            writer.close()

class CryptoAES:

    class AESNEW(object):

        def __init__(self,value:int) -> None:
            self.value = value

        def newkey(self):
            if isinstance(self.value,str):
                if self.value.casefold().strip() == 'iv':
                    return os.urandom(16)
                else:
                    raise ValueError('To get the iv brightened, enter \'iv\'')
            else:
                assert self.value in [16,24,32,128,192,256],'The bytes size can only be (16,24,32) or key format size in (128,192,256)'
                if self.value > 32:
                    return os.urandom(self.value // 8)
                else:
                    return os.urandom(self.value)

    class CTR(object):

        def __init__(self,text,key) -> None:
            self.text = text
            self.key = key

        def encrypt(self):
            aes = AES_CTR(self.key)
            return aes.encrypt(self.text)

        def decrypt(self):
            aes = AES_CTR(self.key)
            return aes.decrypt(self.text)

    class CBC(object):

        def __init__(self,text,key,iv,padding=False) -> None:
            self.text = text
            self.key = key
            self.iv = iv
            self.padding = padding

        def encrypt(self):
            aes = AES_CBC(self.key,iv=self.iv)
            if self.padding:
                encrypter = Encrypter(aes)
                text = encrypter.feed(self.text)
                text += encrypter.feed()
                return text
            else:
                return aes.encrypt(self.text)

        def decrypt(self):
            aes = AES_CBC(self.key,iv=self.iv)
            if self.padding:
                decrypter = Decrypter(aes)
                text = decrypter.feed(self.text)
                text += decrypter.feed()
                return text
            else:
                return aes.decrypt(self.text)

    class CFB(object):

        def __init__(self,text,key,iv,size=1) -> None:
            self.text = text
            self.key = key
            self.iv = iv
            self.size = size

        def encrypt(self):
            assert len(self.text) % self.size == 0
            aes = AES_CFB(self.key,iv=self.iv,segment_size=self.size)
            return aes.encrypt(self.text)

        def decrypt(self):
            aes = AES_CFB(self.key,iv=self.iv,segment_size=self.size)
            return aes.decrypt(self.text)

    class OFB(object):

        def __init__(self,text,key,iv) -> None:
            self.text = text
            self.key = key
            self.iv = iv

        def encrypt(self):
            aes = AES_OFB(self.key,iv=self.iv)
            return aes.encrypt(self.text)

        def decrypt(self):
            aes = AES_OFB(self.key,iv=self.iv)
            return aes.decrypt(self.text)

    class ECB(object):

        def __init__(self,text,key,padding=False) -> None:
            self.text = text
            self.key = key
            self.padding = padding

        def encrypt(self):
            aes = AES_ECB(self.key)
            if self.padding:
                encrypter = Encrypter(aes)
                text = encrypter.feed(self.text)
                text += encrypter.feed()
                return text
            else:
                return aes.encrypt(self.text)

        def decrypt(self):
            aes = AES_ECB(self.key)
            if self.padding:
                decrypter = Decrypter(aes)
                text = decrypter.feed(self.text)
                text += decrypter.feed()
                return text
            else:
                return aes.decrypt(self.text)

    class File(object):

        def __init__(self,path,value=None) -> None:
            self.path = path
            self.value = value

        def read(self):
            with open(self.path,'rb') as reader:
                data = reader.read()
                reader.close()
                return data

        def write(self):
            if not self.value:...
            if isinstance(self.value,str):
                self.value = self.value.encode('utf-8')
            with open(self.path,'wb') as writer:
                writer.write(self.value)
                writer.close()

class CryptoDES:

    class DESNEW(object):
        
        def __init__(self):...

        def newkey(self):
            return os.urandom(8)

    class DES3NEW(object):

        def __init__(self,value:int) -> None:
            self.value = value

        def newkey(self):
            if isinstance(self.value,str):
                if self.value.casefold().strip() == 'iv':
                    return os.urandom(8)
                else:
                    raise ValueError('To get the iv brightened, enter \'iv\'')
            else:
                assert self.value in [16,24,128,192],'The bytes size can only be (16,24) or key format size in (128,192)'
                if self.value > 24:
                    return os.urandom(self.value // 8)
                else:
                    return os.urandom(self.value)

    class CBC(object):

        def __init__(self,text,key,iv,padding=False) -> None:
            self.text = text
            self.key = key
            self.iv = iv
            self.padding = PAD_PKCS5 if padding else PAD_NORMAL

        def encrypt(self) -> bytes:
            des = DES(self.key,CBC,self.iv,None,self.padding)
            return des.encrypt(self.text)

        def decrypt(self) -> bytes:
            des = DES(self.key,CBC,self.iv,None,self.padding)
            return des.decrypt(self.text)

    class ECB(object):

        def __init__(self,text,key,padding=False) -> None:
            self.text = text
            self.key = key
            self.padding = PAD_PKCS5 if padding else PAD_NORMAL

        def encrypt(self) -> bytes:
            des = DES(self.key,ECB,None,None,self.padding)
            return des.encrypt(self.text)

        def decrypt(self) -> bytes:
            des = DES(self.key,ECB,None,None,self.padding)
            return des.decrypt(self.text)

    class DES3CBC(object):

        def __init__(self,text,key,iv,padding=False) -> None:
            self.text = text
            self.key = key
            self.iv = iv
            self.padding = PAD_PKCS5 if padding else PAD_NORMAL

        def encrypt(self) -> bytes:
            des = DES3(self.key,CBC,self.iv,None,self.padding)
            return des.encrypt(self.text)

        def decrypt(self) -> bytes:
            des = DES3(self.key,CBC,self.iv,None,self.padding)
            return des.decrypt(self.text)

    class DES3ECB(object):

        def __init__(self,text,key,padding=False) -> None:
            self.text = text
            self.key = key
            self.padding = PAD_PKCS5 if padding else PAD_NORMAL

        def encrypt(self) -> bytes:
            des = DES3(self.key,ECB,None,None,self.padding)
            return des.encrypt(self.text)

        def decrypt(self) -> bytes:
            des = DES3(self.key,ECB,None,None,self.padding)
            return des.decrypt(self.text)

    class File(object):

        def __init__(self,path,value=None) -> None:
            self.path = path
            self.value = value

        def read(self):
            with open(self.path,'rb') as reader:
                data = reader.read()
                reader.close()
                return data

        def write(self):
            if not self.value:...
            if isinstance(self.value,str):
                self.value = self.value.encode('utf-8')
            with open(self.path,'wb') as writer:
                writer.write(self.value)
                writer.close()

class CryptoRSA:

    class RSANEW(object):

        def __init__(self,size:int) -> int:
            self.size = size

        def newkey(self):
            new = CryptographyPMD
            if isinstance(self.size,int):
                assert self.size in [128,256,512,1024,2048,4096],'Invalid size,Size can only be given(128,256,512,1024,2048,4096)'
                (pubkey,privkey) = new.newkeys(self.size)
                return pubkey,privkey
            else:
                raise ValueError('Invalid input,Please enter an integer')

    class Encrypt(object):

        def __init__(self,msg,publickey) -> ...:
            self.msg = msg
            self.publickey = publickey

        def encrypt(self):
            if isinstance(self.msg,str):
                self.msg = self.msg.encode('utf-8')
            en = CryptographyPMD
            return en.EncryptionPMD(self.msg,self.publickey)

    class Decrypt(object):

        def __init__(self,msg,privatekey) -> None:
            self.msg = msg
            self.privatekey = privatekey

        def decrypt(self):
            if isinstance(self.msg,str):
                raise TypeError('Invalid type')
            de = CryptographyPMD
            return de.DecryptionPMD(self.msg,self.privatekey)

    class File(object):

        def __init__(self,PublicPath=None,PrivatePath=None,PublicKey=None,PrivateKey=None) -> None:
            self.PublicPath = PublicPath
            self.PrivatePath = PrivatePath
            self.PublicKey = PublicKey
            self.PrivateKey = PrivateKey

        def read(self):
            try:
                with open(self.PublicPath,'rb') as pub:
                    data = pub.read()
                    pub.close()
                    public = PublicKeyPMD.load_pkcs1(data)
            except:public = None
            try:
                with open(self.PrivatePath,'rb') as priv:
                    data = priv.read()
                    priv.close()
                    private = PrivateKeyPMD.load_pkcs1(data)
            except:private = None
            return public,private

        def write(self):
            assert (self.PublicKey,self.PrivateKey) != None
            if isinstance(self.PublicKey,object) and isinstance(self.PrivateKey,object):
                Public = PublicKeyPMD(self.PublicKey.n,self.PublicKey.e).save_pkcs1()
                Private = PrivateKeyPMD(self.PrivateKey.n,self.PrivateKey.e,self.PrivateKey.d,self.PrivateKey.p,self.PrivateKey.q).save_pkcs1()
                with open(self.PublicPath,'wb') as pub:
                    pub.write(Public)
                    pub.close()
                with open(self.PrivatePath,'wb') as priv:
                    priv.write(Private)
                    priv.close()

    class TextFile(object):

        def __init__(self,textpath,value=None) -> None:
            self.path = textpath
            self.value = value

        def read(self):
            with open(self.path,'rb') as reader:
                data = reader.read()
                reader.close()
                return data

        def write(self):
            if not self.value:...
            if isinstance(self.value,str):
                self.value = self.value.encode('utf-8')
            with open(self.path,'wb') as writer:
                writer.write(self.value)
                writer.close()

class CryptoBase64:

    class Base16(object):

        def __init__(self,text,encoding:str=Encoding.UTF8.name,errors:str=Errors.backslashreplace.name) -> None:
            self.text = text
            self.encoding = encoding
            self.errors = errors

        def encrypt(self):
            if isinstance(self.text,str):
                return b16encode(self.text.encode(self.encoding,self.errors))
            elif isinstance(self.text,bytes):
                return b16encode(self.text)
            else:
                raise AttributeError('Attribute error')

        def decrypt(self):
            if isinstance(self.text,bytes):
                return b16decode(self.text.decode(self.encoding,self.errors))
            else:
                raise AttributeError('Attribute error')

    class Base32(object):

        def __init__(self,text,encoding:str=Encoding.UTF8.name,errors:str=Errors.backslashreplace.name) -> None:
            self.text = text
            self.encoding = encoding
            self.errors = errors

        def encrypt(self):
            if isinstance(self.text,str):
                return b32encode(self.text.encode(self.encoding,self.errors))
            elif isinstance(self.text,bytes):
                return b32encode(self.text)
            else:
                raise AttributeError('Attribute error')

        def decrypt(self):
            if isinstance(self.text,bytes):
                return b32decode(self.text.decode(self.encoding,self.errors))
            else:
                raise AttributeError('Attribute error')

    class Base64(object):

        def __init__(self,text,encoding:str=Encoding.UTF8.name,errors:str=Errors.backslashreplace.name) -> None:
            self.text = text
            self.encoding = encoding
            self.errors = errors

        def encrypt(self):
            if isinstance(self.text,str):
                return b64encode(self.text.encode(self.encoding,self.errors))
            elif isinstance(self.text,bytes):
                return b64encode(self.text)
            else:
                raise AttributeError('Attribute error')

        def decrypt(self):
            if isinstance(self.text,bytes):
                return b64decode(self.text.decode(self.encoding,self.errors))
            else:
                raise AttributeError('Attribute error')

    class Base85(object):

        def __init__(self,text,encoding:str=Encoding.UTF8.name,errors:str=Errors.backslashreplace.name) -> None:
            self.text = text
            self.encoding = encoding
            self.errors = errors

        def encrypt(self):
            if isinstance(self.text,str):
                return b85encode(self.text.encode(self.encoding,self.errors))
            elif isinstance(self.text,bytes):
                return b85encode(self.text)
            else:
                raise AttributeError('Attribute error')

        def decrypt(self):
            if isinstance(self.text,bytes):
                return b85decode(self.text.decode(self.encoding,self.errors))
            else:
                raise AttributeError('Attribute error')

class CryptoCarry:
    
    encode = [
        'array_decimal',
        'array_string',
        'array_prefix',
        'string_space',
        'string_prefix'
    ]
    decode = [
        'array_decimal',
        'array_string',
        'string_decimal',
        'string'
    ]

    class Binary(object):
        
        def __init__(self,text=None,enmode=None,demode=None) -> None:
            self.ENALL = CryptoCarry.encode
            self.DEALL = CryptoCarry.decode
            self.text = text
            if isinstance(enmode,str):
                assert enmode.casefold() in self.ENALL,'invalid mode,Enter the following:\n' + '\n'.join([f'{i}.{self.ENALL[i]}' for i in range(len(self.ENALL))])
                self.enmode = enmode
            elif isinstance(enmode,int):
                assert enmode < len(self.ENALL) and enmode >= 0,'invalid mode,Enter the following:\n' + '\n'.join([f'{i}.{self.ENALL[i]}' for i in range(len(self.ENALL))])
                self.enmode = self.ENALL[enmode]
            if isinstance(demode,str):
                assert demode.casefold() in self.DEALL,'invalid mode,Enter the following:\n' + '\n'.join([f'{i}.{self.DEALL[i]}' for i in range(len(self.DEALL))])
                self.demode = demode
            elif isinstance(demode,int):
                assert demode < len(self.DEALL) and demode >= 0,'invalid mode,Enter the following:\n' + '\n'.join([f'{i}.{self.DEALL[i]}' for i in range(len(self.DEALL))])
                self.demode = self.DEALL[demode]

        def encrypt(self):
            ints : list = []
            if isinstance(self.text,str):
                ints = [ord(i) for i in self.text]
            elif isinstance(self.text,int):
                ints = [self.text]
            elif isinstance(self.text,(list,tuple)):
                for i in self.text:
                    if isinstance(i,str):
                        if i.startswith('0b'):
                            ints.append(int(i.lstrip('0b'),2))
                        elif i.isdecimal():
                            ints.append(int(i,2))
                        else:
                            ints.append(ord(i))
                    elif isinstance(i,int):
                        ints.append(i)
                    else:
                        raise ValueError('invalid content')
            else:
                raise TypeError('Can only provide type\nstring,interger,list,tuple')
            if self.enmode == self.ENALL[0]:
                return ints
            elif self.enmode == self.ENALL[1]:
                return [bin(i).lstrip('0b') for i in ints]
            elif self.enmode == self.ENALL[2]:
                return [bin(i) for i in ints]
            elif self.enmode == self.ENALL[3]:
                return ' '.join([bin(i).lstrip('0b') for i in ints])
            elif self.enmode == self.ENALL[4]:
                return ' '.join([bin(i) for i in ints])

        def decrypt(self):
            ints : list = []
            if isinstance(self.text,str):
                if '\x20' in self.text:
                    for i in self.text.split('\x20'):
                        if i.startswith('0b'):
                            ints.append(int(i.lstrip('0b'),2))
                        else:
                            ints.append(int(i,2))
                else:
                    raise ValueError('Strings need to be separated by spaces')
            elif isinstance(self.text,(list,tuple)):
                for i in self.text:
                    if isinstance(i,str):
                        if i.startswith('0b'):
                            ints.append(int(i.lstrip('0b'),2))
                        else:
                            ints.append(int(i,2))
                    elif isinstance(i,int):
                        ints.append(i)
                    else:
                        raise ValueError('A list or tuple can only join strings or integers')
            if self.demode == self.DEALL[0]:
                return ints
            elif self.demode == self.DEALL[1]:
                return [str(i) for i in ints]
            elif self.demode == self.DEALL[2]:
                return ','.join([str(i) for i in ints])
            elif self.demode == self.DEALL[3]:
                return ''.join([chr(i) for i in ints])

    class Octal(object):

        def __init__(self,text=None,enmode=None,demode=None) -> None:
            self.ENALL = CryptoCarry.encode
            self.DEALL = CryptoCarry.decode
            self.text = text
            if isinstance(enmode,str):
                assert enmode.casefold() in self.ENALL,'invalid mode,Enter the following:\n' + '\n'.join([f'{i}.{self.ENALL[i]}' for i in range(len(self.ENALL))])
                self.enmode = enmode
            elif isinstance(enmode,int):
                assert enmode < len(self.ENALL) and enmode >= 0,'invalid mode,Enter the following:\n' + '\n'.join([f'{i}.{self.ENALL[i]}' for i in range(len(self.ENALL))])
                self.enmode = self.ENALL[enmode]
            if isinstance(demode,str):
                assert demode.casefold() in self.DEALL,'invalid mode,Enter the following:\n' + '\n'.join([f'{i}.{self.DEALL[i]}' for i in range(len(self.DEALL))])
                self.demode = demode
            elif isinstance(demode,int):
                assert demode < len(self.DEALL) and demode >= 0,'invalid mode,Enter the following:\n' + '\n'.join([f'{i}.{self.DEALL[i]}' for i in range(len(self.DEALL))])
                self.demode = self.DEALL[demode]

        def encrypt(self):
            ints : list = []
            if isinstance(self.text,str):
                ints = [ord(i) for i in self.text]
            elif isinstance(self.text,int):
                ints = [self.text]
            elif isinstance(self.text,(list,tuple)):
                for i in self.text:
                    if isinstance(i,str):
                        if i.startswith('0o'):
                            ints.append(int(i.lstrip('0o'),8))
                        elif i.isdecimal():
                            ints.append(int(i,8))
                        else:
                            ints.append(ord(i))
                    elif isinstance(i,int):
                        ints.append(i)
                    else:
                        raise ValueError('invalid content')
            else:
                raise TypeError('Can only provide type\nstring,interger,list,tuple')
            if self.enmode == self.ENALL[0]:
                return ints
            elif self.enmode == self.ENALL[1]:
                return [oct(i).lstrip('0o') for i in ints]
            elif self.enmode == self.ENALL[2]:
                return [oct(i) for i in ints]
            elif self.enmode == self.ENALL[3]:
                return ' '.join([oct(i).lstrip('0o') for i in ints])
            elif self.enmode == self.ENALL[4]:
                return ' '.join([oct(i) for i in ints])

        def decrypt(self):
            ints : list = []
            if isinstance(self.text,str):
                if '\x20' in self.text:
                    for i in self.text.split('\x20'):
                        if i.startswith('0o'):
                            ints.append(int(i.lstrip('0o'),8))
                        else:
                            ints.append(int(i,2))
                else:
                    raise ValueError('Strings need to be separated by spaces')
            elif isinstance(self.text,(list,tuple)):
                for i in self.text:
                    if isinstance(i,str):
                        if i.startswith('0o'):
                            ints.append(int(i.lstrip('0o'),8))
                        else:
                            ints.append(int(i,8))
                    elif isinstance(i,int):
                        ints.append(i)
                    else:
                        raise ValueError('A list or tuple can only join strings or integers')
            if self.demode == self.DEALL[0]:
                return ints
            elif self.demode == self.DEALL[1]:
                return [str(i) for i in ints]
            elif self.demode == self.DEALL[2]:
                return ','.join([str(i) for i in ints])
            elif self.demode == self.DEALL[3]:
                return ''.join([chr(i) for i in ints])

    class Hex(object):

        def __init__(self,text=None,enmode=None,demode=None) -> None:
            self.ENALL = CryptoCarry.encode
            self.DEALL = CryptoCarry.decode
            self.text = text
            if isinstance(enmode,str):
                assert enmode.casefold() in self.ENALL,'invalid mode,Enter the following:\n' + '\n'.join([f'{i}.{self.ENALL[i]}' for i in range(len(self.ENALL))])
                self.enmode = enmode
            elif isinstance(enmode,int):
                assert enmode < len(self.ENALL) and enmode >= 0,'invalid mode,Enter the following:\n' + '\n'.join([f'{i}.{self.ENALL[i]}' for i in range(len(self.ENALL))])
                self.enmode = self.ENALL[enmode]
            if isinstance(demode,str):
                assert demode.casefold() in self.DEALL,'invalid mode,Enter the following:\n' + '\n'.join([f'{i}.{self.DEALL[i]}' for i in range(len(self.DEALL))])
                self.demode = demode
            elif isinstance(demode,int):
                assert demode < len(self.DEALL) and demode >= 0,'invalid mode,Enter the following:\n' + '\n'.join([f'{i}.{self.DEALL[i]}' for i in range(len(self.DEALL))])
                self.demode = self.DEALL[demode]

        def encrypt(self):
            ints : list = []
            if isinstance(self.text,str):
                ints = [ord(i) for i in self.text]
            elif isinstance(self.text,int):
                ints = [self.text]
            elif isinstance(self.text,(list,tuple)):
                for i in self.text:
                    if isinstance(i,str):
                        if i.startswith('0x'):
                            ints.append(int(i.lstrip('0x'),16))
                        elif i.isdecimal():
                            ints.append(int(i,16))
                        else:
                            ints.append(ord(i))
                    elif isinstance(i,int):
                        ints.append(i)
                    else:
                        raise ValueError('invalid content')
            else:
                raise TypeError('Can only provide type\nstring,interger,list,tuple')
            if self.enmode == self.ENALL[0]:
                return ints
            elif self.enmode == self.ENALL[1]:
                return [hex(i).lstrip('0x') for i in ints]
            elif self.enmode == self.ENALL[2]:
                return [hex(i) for i in ints]
            elif self.enmode == self.ENALL[3]:
                return ' '.join([hex(i).lstrip('0x') for i in ints])
            elif self.enmode == self.ENALL[4]:
                return ' '.join([hex(i) for i in ints])

        def decrypt(self):
            ints : list = []
            if isinstance(self.text,str):
                if '\x20' in self.text:
                    for i in self.text.split('\x20'):
                        if i.startswith('0x'):
                            ints.append(int(i.lstrip('0x'),16))
                        else:
                            ints.append(int(i,16))
                else:
                    raise ValueError('Strings need to be separated by spaces')
            elif isinstance(self.text,(list,tuple)):
                for i in self.text:
                    if isinstance(i,str):
                        if i.startswith('0x'):
                            ints.append(int(i.lstrip('0x'),16))
                        else:
                            ints.append(int(i,16))
                    elif isinstance(i,int):
                        ints.append(i)
                    else:
                        raise ValueError('A list or tuple can only join strings or integers')
            if self.demode == self.DEALL[0]:
                return ints
            elif self.demode == self.DEALL[1]:
                return [str(i) for i in ints]
            elif self.demode == self.DEALL[2]:
                return ','.join([str(i) for i in ints])
            elif self.demode == self.DEALL[3]:
                return ''.join([chr(i) for i in ints])

class CryptoConvert(object):

    class HEX(object):

        def __init__(self,text,encoding=Encoding.UTF8.name,errors:str=Errors.backslashreplace.name) -> Encoding:
            self.text = text
            self.encoding = encoding
            self.errors = errors

        def encrypt(self):
            if isinstance(self.text,str):
                return binascii.b2a_hex(self.text.encode(self.encoding,self.errors))
            elif isinstance(self.text,bytes):
                return binascii.b2a_hex(self.text)
            else:
                raise TypeError('This definition can only be given bytes or str\nBut you give %s' % str(type(self.text)))

        def decrypt(self):
            if isinstance(self.text,bytes):
                return binascii.a2b_hex(self.text.decode(self.encoding,self.errors))
            else:
                raise TypeError('This definition can only be given bytes\nBut you give %s' % str(type(self.text)))

    class BASE64(object):

        def __init__(self,text,encoding=Encoding.UTF8.name,errors:str=Errors.backslashreplace.name) -> Encoding:
            self.text = text
            self.encoding = encoding
            self.errors = errors

        def encrypt(self):
            if isinstance(self.text,str):
                return binascii.b2a_base64(self.text.encode(self.encoding,self.errors))
            elif isinstance(self.text,bytes):
                return binascii.b2a_base64(self.text)
            else:
                raise TypeError('This definition can only be given bytes or str\nBut you give %s' % str(type(self.text)))

        def decrypt(self):
            if isinstance(self.text,bytes):
                return binascii.a2b_base64(self.text.decode(self.encoding,self.errors))
            else:
                raise TypeError('This definition can only be given bytes\nBut you give %s' % str(type(self.text)))

    class QP(object):

        def __init__(self,text,encoding=Encoding.UTF8.name,errors:str=Errors.backslashreplace.name) -> Encoding:
            self.text = text
            self.encoding = encoding
            self.errors = errors

        def encrypt(self):
            if isinstance(self.text,str):
                return binascii.b2a_qp(self.text.encode(self.encoding,self.errors))
            elif isinstance(self.text,bytes):
                return binascii.b2a_qp(self.text)
            else:
                raise TypeError('This definition can only be given bytes or str\nBut you give %s' % str(type(self.text)))

        def decrypt(self):
            if isinstance(self.text,bytes):
                return binascii.a2b_qp(self.text.decode(self.encoding,self.errors))
            else:
                raise TypeError('This definition can only be given bytes\nBut you give %s' % str(type(self.text)))

    class UU(object):

        def __init__(self,text,encoding=Encoding.UTF8.name,errors:str=Errors.backslashreplace.name) -> Encoding:
            self.text = text
            self.encoding = encoding
            self.errors = errors

        def encrypt(self):
            if isinstance(self.text,str):
                return binascii.b2a_uu(self.text.encode(self.encoding,self.errors))
            elif isinstance(self.text,bytes):
                return binascii.b2a_uu(self.text)
            else:
                raise TypeError('This definition can only be given bytes or str\nBut you give %s' % str(type(self.text)))

        def decrypt(self):
            if isinstance(self.text,bytes):
                return binascii.a2b_uu(self.text.decode(self.encoding,self.errors))
            else:
                raise TypeError('This definition can only be given bytes\nBut you give %s' % str(type(self.text)))

class CryptoJson:

    class FP(object):
        
        def __init__(self,fp) -> None:
            self.fp = fp
            
        def Load(self):
            return load(self.fp)

        def Dump(self):
            return dump(self.fp)

    class OBJ(object):
        
        def __init__(self,obj) -> None:
            self.obj = obj
            
        def Load(self):
            return loads(self.obj)

        def Dump(self):
            return dumps(self.obj)

class CryptoCanvas:

    class Print:

        def attr(method):
            return Printf.attr(method)

        def fg(color):
            return Printf.fg(color)

        def bg(color):
            return Printf.bg(color)

        def red():
            return Printf.fg(1)

        def orange():
            return Printf.fg(202)

        def yellow():
            return Printf.fg(3)

        def green():
            return Printf.fg(2)

        def cyan():
            return Printf.fg(6)

        def blue():
            return Printf.fg(4)

        def purple():
            return Printf.fg(140)

        def black():
            return Printf.fg(0)

        def grey():
            return Printf.fg(239)

        def white():
            return Printf.fg(15)

class CryptoFiles:

    class Get(object):
        
        def __init__(self) -> None:
            pass

        def tempdir(self):
            return tempfile.gettempdir()

class CryptoUid:

    class Get(object):

        def __init__(self,NameSpace=None,Name:str=None) -> None:
            self.NameSpace = [
                'DNS',
                'URL',
                'OID',
                'X500'
            ]
            if isinstance(Name,str):
                self.Name = Name
            if isinstance(NameSpace,str):
                if NameSpace.upper() in self.NameSpace:
                    self.NameSpace = NameSpace.upper()
                else:raise ValueError('The entered string is no longer selected')
            elif isinstance(NameSpace,int):
                if NameSpace < len(self.NameSpace):
                    self.NameSpace = self.NameSpace[NameSpace]
                else:raise ValueError('The entered number exceeds the selectable range')
            if self.NameSpace in [0,'DNS']:self.NameSpace = uuid.NAMESPACE_DNS
            elif self.NameSpace in [1,'URL']:self.NameSpace = uuid.NAMESPACE_URL
            elif self.NameSpace in [2,'OID']:self.NameSpace = uuid.NAMESPACE_OID
            elif self.NameSpace in [3,'X500']:self.NameSpace = uuid.NAMESPACE_X500

        def date(self):
            return uuid.uuid1()

        def md5(self):
            return uuid.uuid3(self.NameSpace, self.Name)

        def random(self):
            return uuid.uuid4()

        def sha1(self):
            return uuid.uuid5(self.NameSpace, self.Name)