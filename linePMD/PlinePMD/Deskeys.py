# Supported modes of operation:
#   ECB - Electronic Codebook
#   CBC - Cipher-Block Chaining

import sys

_pythonMajorVersion = sys.version_info[0]

ECB =	0
CBC =	1

PAD_NORMAL = 1
PAD_PKCS5 = 2

class baseDes(object):
	def __init__(self, mode=ECB, IV=None, pad=None, padmode=PAD_NORMAL):
		if IV:
			IV = self._guardAgainstUnicode(IV)
		if pad:
			pad = self._guardAgainstUnicode(pad)
		self.block_size = 8
		if pad and padmode == PAD_PKCS5:
			raise ValueError("Cannot use a pad character with PAD_PKCS5 ^^")
		if IV and len(IV) != self.block_size:
			raise ValueError("Invalid Initial Value (IV), must be a multiple of " + str(self.block_size) + " bytes ^^")

		self._mode = mode
		self._iv = IV
		self._padding = pad
		self._padmode = padmode

	def getKey(self):
		return self.__key

	def setKey(self, key):
		key = self._guardAgainstUnicode(key)
		self.__key = key

	def getMode(self):
		return self._mode

	def setMode(self, mode):
		self._mode = mode

	def getPadding(self):
		return self._padding

	def setPadding(self, pad):
		if pad is not None:
			pad = self._guardAgainstUnicode(pad)
		self._padding = pad

	def getPadMode(self):
		return self._padmode
		
	def setPadMode(self, mode):
		self._padmode = mode

	def getIV(self):
		return self._iv

	def setIV(self, IV):
		if not IV or len(IV) != self.block_size:
			raise ValueError("Invalid Initial Value (IV), must be a multiple of " + str(self.block_size) + " bytes ~")
		IV = self._guardAgainstUnicode(IV)
		self._iv = IV

	def _padData(self, data, pad, padmode):
		if padmode is None:
			padmode = self.getPadMode()
		if pad and padmode == PAD_PKCS5:
			raise ValueError("Cannot use a pad character with PAD_PKCS5 ~")

		if padmode == PAD_NORMAL:
			if len(data) % self.block_size == 0:
				return data

			if not pad:
				pad = self.getPadding()
			if not pad:
				raise ValueError("Data must be a multiple of " + str(self.block_size) + " bytes in length. Use padmode=PAD_PKCS5 or set the pad character ~")
			data += (self.block_size - (len(data) % self.block_size)) * pad
		
		elif padmode == PAD_PKCS5:
			pad_len = 8 - (len(data) % self.block_size)
			if _pythonMajorVersion < 3:
				data += pad_len * chr(pad_len)
			else:
				data += bytes([pad_len] * pad_len)

		return data

	def _unpadData(self, data, pad, padmode):
		if not data:
			return data
		if pad and padmode == PAD_PKCS5:
			raise ValueError("Cannot use a pad character with PAD_PKCS5 ><")
		if padmode is None:
			padmode = self.getPadMode()

		if padmode == PAD_NORMAL:
			if not pad:
				pad = self.getPadding()
			if pad:
				data = data[:-self.block_size] + \
				       data[-self.block_size:].rstrip(pad)

		elif padmode == PAD_PKCS5:
			if _pythonMajorVersion < 3:
				pad_len = ord(data[-1])
			else:
				pad_len = data[-1]
			data = data[:-pad_len]

		return data

	def _guardAgainstUnicode(self, data):
		if isinstance(data, str):
			try:
				return data.encode('ascii')
			except UnicodeEncodeError:...
			raise ValueError("Can only work with encoded strings, not Unicode ^^")
		return data

class DES(baseDes):


	__pc1 = [
        0x38, 0x30, 0x28, 0x20, 0x18, 0x10, 0x08,
        0x00, 0x39, 0x31, 0x29, 0x21, 0x19, 0x11,
        0x09, 0x01, 0x3a, 0x32, 0x2a, 0x22, 0x1a,
        0x12, 0x0a, 0x02, 0x3b, 0x33, 0x2b, 0x23,
        0x3e, 0x36, 0x2e, 0x26, 0x1e, 0x16, 0x0e,
        0x06, 0x3d, 0x35, 0x2d, 0x25, 0x1d, 0x15,
        0x0d, 0x05, 0x3c, 0x34, 0x2c, 0x24, 0x1c,
        0x14, 0x0c, 0x04, 0x1b, 0x13, 0x0b, 0x03
    ]

	__left_rotations = [
        0x1, 0x1, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x1, 0x2, 0x2, 0x2, 0x2, 0x2, 0x2, 0x1
    ]

	__pc2 = [
        0x0d, 0x10, 0x0a, 0x17, 0x00, 0x04,
        0x02, 0x1b, 0x0e, 0x05, 0x14, 0x09,
        0x16, 0x12, 0x0b, 0x03, 0x19, 0x07,
        0x0f, 0x06, 0x1a, 0x13, 0x0c, 0x01,
        0x28, 0x33, 0x1e, 0x24, 0x2e, 0x36,
        0x1d, 0x27, 0x32, 0x2c, 0x20, 0x2f,
        0x2b, 0x30, 0x26, 0x37, 0x21, 0x34,
        0x2d, 0x29, 0x31, 0x23, 0x1c, 0x1f
    ]

	__ip = [
        0x39, 0x31, 0x29, 0x21, 0x19, 0x11, 0x9, 0x1,
        0x3b, 0x33, 0x2b, 0x23, 0x1b, 0x13, 0xb, 0x3,
        0x3d, 0x35, 0x2d, 0x25, 0x1d, 0x15, 0xd, 0x5,
        0x3f, 0x37, 0x2f, 0x27, 0x1f, 0x17, 0xf, 0x7,
        0x38, 0x30, 0x28, 0x20, 0x18, 0x10, 0x8, 0x0,
        0x3a, 0x32, 0x2a, 0x22, 0x1a, 0x12, 0xa, 0x2,
        0x3c, 0x34, 0x2c, 0x24, 0x1c, 0x14, 0xc, 0x4,
        0x3e, 0x36, 0x2e, 0x26, 0x1e, 0x16, 0xe, 0x6
    ]

	__expansion_table = [
        0x1f, 0x0, 0x1, 0x2, 0x3, 0x4,
        0x3, 0x4, 0x5, 0x6, 0x7, 0x8,
        0x7, 0x8, 0x9, 0xa, 0xb, 0xc,
        0xb, 0xc, 0xd, 0xe, 0xf, 0x1,
        0xf, 0x10, 0x11, 0x12, 0x13, 0x14,
        0x13, 0x14, 0x15, 0x16, 0x17, 0x1,
        0x17, 0x18, 0x19, 0x1a, 0x1b, 0x1c,
        0x1b, 0x1c, 0x1d, 0x1e, 0x1f, 0x0
    ]

	__sbox = [
		# S1
		[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
		 0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
		 4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
		 15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],

		# S2
		[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
		 3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
		 0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
		 13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],

		# S3
		[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
		 13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
		 13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
		 1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],

		# S4
		[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
		 13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
		 10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
		 3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],

		# S5
		[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
		 14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
		 4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
		 11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],

		# S6
		[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
		 10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
		 9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
		 4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],

		# S7
		[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
		 13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
		 1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
		 6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],

		# S8
		[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
		 1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
		 7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
		 2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
	]


	__p = [
        0x0f, 0x06, 0x13, 0x14, 0x1c, 0x0b,
        0x1b, 0x10, 0x00, 0x0e, 0x16, 0x19,
        0x04, 0x11, 0x1e, 0x09, 0x01, 0x07,
        0x17, 0x0d, 0x1f, 0x1a, 0x02, 0x08,
        0x12, 0x0c, 0x1d, 0x05, 0x15, 0x0a,
        0x03, 0x18
    ]

	__fp = [
        0x27, 0x07, 0x2f, 0x0f, 0x37, 0x17, 0x3f, 0x1f,
        0x26, 0x06, 0x2e, 0x0e, 0x36, 0x16, 0x3e, 0x1e,
        0x25, 0x05, 0x2d, 0x0d, 0x35, 0x15, 0x3d, 0x1d,
        0x24, 0x04, 0x2c, 0x0c, 0x34, 0x14, 0x3c, 0x1c,
        0x23, 0x03, 0x2b, 0x0b, 0x33, 0x13, 0x3b, 0x1b,
        0x22, 0x02, 0x2a, 0x0a, 0x32, 0x12, 0x3a, 0x1a,
        0x21, 0x01, 0x29, 0x09, 0x31, 0x11, 0x39, 0x19,
        0x20, 0x00, 0x28, 0x08, 0x30, 0x10, 0x38, 0x18
    ]

	ENCRYPT =	0x00
	DECRYPT =	0x01

	# Initialisation
	def __init__(self, key, mode=ECB, IV=None, pad=None, padmode=PAD_NORMAL):
		if len(key) != 8:
			raise ValueError("Invalid DES key size. Key must be exactly 8 bytes long ~")
		baseDes.__init__(self, mode, IV, pad, padmode)
		self.key_size = 8

		self.L = []
		self.R = []
		self.Kn = [ [0] * 48 ] * 16
		self.final = []

		self.setKey(key)

	def setKey(self, key):
		baseDes.setKey(self, key)
		self.__create_sub_keys()

	def __String_to_BitList(self, data):
		if _pythonMajorVersion < 3:
			data = [ord(c) for c in data]
		l = len(data) * 8
		result = [0] * l
		pos = 0
		for ch in data:
			i = 7
			while i >= 0:
				if ch & (1 << i) != 0:
					result[pos] = 1
				else:
					result[pos] = 0
				pos += 1
				i -= 1

		return result

	def __BitList_to_String(self, data):
		result = []
		pos = 0
		c = 0
		while pos < len(data):
			c += data[pos] << (7 - (pos % 8))
			if (pos % 8) == 7:
				result.append(c)
				c = 0
			pos += 1

		if _pythonMajorVersion < 3:
			return ''.join([ chr(c) for c in result ])
		else:
			return bytes(result)

	def __permutate(self, table, block):
		return list(map(lambda x: block[x], table))
	
	def __create_sub_keys(self):
		key = self.__permutate(DES.__pc1, self.__String_to_BitList(self.getKey()))
		i = 0
		self.L = key[:28]
		self.R = key[28:]
		while i < 16:
			j = 0
			while j < DES.__left_rotations[i]:
				self.L.append(self.L[0])
				del self.L[0]

				self.R.append(self.R[0])
				del self.R[0]

				j += 1

			self.Kn[i] = self.__permutate(DES.__pc2, self.L + self.R)

			i += 1

	def __des_crypt(self, block, crypt_type):
		block = self.__permutate(DES.__ip, block)
		self.L = block[:32]
		self.R = block[32:]

		if crypt_type == DES.ENCRYPT:
			iteration = 0
			iteration_adjustment = 1
		else:
			iteration = 15
			iteration_adjustment = -1

		i = 0
		while i < 16:
			tempR = self.R[:]

			self.R = self.__permutate(DES.__expansion_table, self.R)

			self.R = list(map(lambda x, y: x ^ y, self.R, self.Kn[iteration]))
			B = [self.R[:6], self.R[6:12], self.R[12:18], self.R[18:24], self.R[24:30], self.R[30:36], self.R[36:42], self.R[42:]]

			j = 0
			Bn = [0] * 32
			pos = 0
			while j < 8:
				m = (B[j][0] << 1) + B[j][5]
				n = (B[j][1] << 3) + (B[j][2] << 2) + (B[j][3] << 1) + B[j][4]

				v = DES.__sbox[j][(m << 4) + n]

				Bn[pos] = (v & 8) >> 3
				Bn[pos + 1] = (v & 4) >> 2
				Bn[pos + 2] = (v & 2) >> 1
				Bn[pos + 3] = v & 1

				pos += 4
				j += 1

			self.R = self.__permutate(DES.__p, Bn)

			self.R = list(map(lambda x, y: x ^ y, self.R, self.L))
			self.L = tempR

			i += 1
			iteration += iteration_adjustment
		
		self.final = self.__permutate(DES.__fp, self.R + self.L)
		return self.final


	def crypt(self, data, crypt_type):

		if not data:
			return ''
		if len(data) % self.block_size != 0:
			if crypt_type == DES.DECRYPT:
				raise ValueError("Invalid data length, data must be a multiple of " + str(self.block_size) + " bytes\n.")
			if not self.getPadding():
				raise ValueError("Invalid data length, data must be a multiple of " + str(self.block_size) + " bytes\n. Try setting the optional padding character ^^")
			else:
				data += (self.block_size - (len(data) % self.block_size)) * self.getPadding()

		if self.getMode() == CBC:
			if self.getIV():
				iv = self.__String_to_BitList(self.getIV())
			else:
				raise ValueError("For CBC mode, you must supply the Initial Value (IV) for ciphering ~")

		i = 0
		result = []
		while i < len(data):
				
			block = self.__String_to_BitList(data[i:i+8])

			if self.getMode() == CBC:
				if crypt_type == DES.ENCRYPT:
					block = list(map(lambda x, y: x ^ y, block, iv))

				processed_block = self.__des_crypt(block, crypt_type)

				if crypt_type == DES.DECRYPT:
					processed_block = list(map(lambda x, y: x ^ y, processed_block, iv))
					iv = block
				else:
					iv = processed_block
			else:
				processed_block = self.__des_crypt(block, crypt_type)

			result.append(self.__BitList_to_String(processed_block))
			i += 8

		if _pythonMajorVersion < 3:
			return ''.join(result)
		else:
			return bytes.fromhex('').join(result)

	def encrypt(self, data, pad=None, padmode=None):
		data = self._guardAgainstUnicode(data)
		if pad is not None:
			pad = self._guardAgainstUnicode(pad)
		data = self._padData(data, pad, padmode)
		return self.crypt(data, DES.ENCRYPT)

	def decrypt(self, data, pad=None, padmode=None):
		data = self._guardAgainstUnicode(data)
		if pad is not None:
			pad = self._guardAgainstUnicode(pad)
		data = self.crypt(data, DES.DECRYPT)
		return self._unpadData(data, pad, padmode)

class DES3(baseDes):

	def __init__(self, key, mode=ECB, IV=None, pad=None, padmode=PAD_NORMAL):
		baseDes.__init__(self, mode, IV, pad, padmode)
		self.setKey(key)

	def setKey(self, key):
		self.key_size = 24
		if len(key) != self.key_size:
			if len(key) == 16:
				self.key_size = 16
			else:
				raise ValueError("Invalid triple DES key size. Key must be either 16 or 24 bytes long ><")
		if self.getMode() == CBC:
			if not self.getIV():
				self._iv = key[:self.block_size]
			if len(self.getIV()) != self.block_size:
				raise ValueError("Invalid IV, must be 8 bytes in length ><")
		self.__key1 = DES(key[:8], self._mode, self._iv,
				  self._padding, self._padmode)
		self.__key2 = DES(key[8:16], self._mode, self._iv,
				  self._padding, self._padmode)
		if self.key_size == 16:
			self.__key3 = self.__key1
		else:
			self.__key3 = DES(key[16:], self._mode, self._iv,
					  self._padding, self._padmode)
		baseDes.setKey(self, key)

	def setMode(self, mode):
		baseDes.setMode(self, mode)
		for key in (self.__key1, self.__key2, self.__key3):
			key.setMode(mode)

	def setPadding(self, pad):
		baseDes.setPadding(self, pad)
		for key in (self.__key1, self.__key2, self.__key3):
			key.setPadding(pad)

	def setPadMode(self, mode):
		baseDes.setPadMode(self, mode)
		for key in (self.__key1, self.__key2, self.__key3):
			key.setPadMode(mode)

	def setIV(self, IV):
		baseDes.setIV(self, IV)
		for key in (self.__key1, self.__key2, self.__key3):
			key.setIV(IV)

	def encrypt(self, data, pad=None, padmode=None):
		ENCRYPT = DES.ENCRYPT
		DECRYPT = DES.DECRYPT
		data = self._guardAgainstUnicode(data)
		if pad is not None:
			pad = self._guardAgainstUnicode(pad)
		data = self._padData(data, pad, padmode)
		if self.getMode() == CBC:
			self.__key1.setIV(self.getIV())
			self.__key2.setIV(self.getIV())
			self.__key3.setIV(self.getIV())
			i = 0
			result = []
			while i < len(data):
				block = self.__key1.crypt(data[i:i+8], ENCRYPT)
				block = self.__key2.crypt(block, DECRYPT)
				block = self.__key3.crypt(block, ENCRYPT)
				self.__key1.setIV(block)
				self.__key2.setIV(block)
				self.__key3.setIV(block)
				result.append(block)
				i += 8
			if _pythonMajorVersion < 3:
				return ''.join(result)
			else:
				return bytes.fromhex('').join(result)
		else:
			data = self.__key1.crypt(data, ENCRYPT)
			data = self.__key2.crypt(data, DECRYPT)
			return self.__key3.crypt(data, ENCRYPT)

	def decrypt(self, data, pad=None, padmode=None):
		ENCRYPT = DES.ENCRYPT
		DECRYPT = DES.DECRYPT
		data = self._guardAgainstUnicode(data)
		if pad is not None:
			pad = self._guardAgainstUnicode(pad)
		if self.getMode() == CBC:
			self.__key1.setIV(self.getIV())
			self.__key2.setIV(self.getIV())
			self.__key3.setIV(self.getIV())
			i = 0
			result = []
			while i < len(data):
				iv = data[i:i+8]
				block = self.__key3.crypt(iv,    DECRYPT)
				block = self.__key2.crypt(block, ENCRYPT)
				block = self.__key1.crypt(block, DECRYPT)
				self.__key1.setIV(iv)
				self.__key2.setIV(iv)
				self.__key3.setIV(iv)
				result.append(block)
				i += 8
			if _pythonMajorVersion < 3:
				data = ''.join(result)
			else:
				data = bytes.fromhex('').join(result)
		else:
			data = self.__key3.crypt(data, DECRYPT)
			data = self.__key2.crypt(data, ENCRYPT)
			data = self.__key1.crypt(data, DECRYPT)
		return self._unpadData(data, pad, padmode)
