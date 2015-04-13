
import sys
from Crypto.PublicKey import RSA

class RSAToFile:
	key=None
	
	def generate(self):
		self.key=RSA.generate(1024)
	
	def loadrsa(self, import_key):
		self.key=RSA.importKey(import_key)

	def private(self):
		f = open('private','w')
		private = self.key.exportKey('PEM')
		f.write(private)
		f.close()
		return private

	def public(self):
		f = open('public', 'w')
		public = self.key.publickey().exportKey('PEM')
		f.write(public)
		f.close()

	def encrypt(self, plain):
		cipher = open('cipher','w')
		encrypted = self.key.encrypt(plain,"")
		cipher.write(encrypted[0])
		cipher.close()

	def decrypt(self, cipher):
		decrypted = self.key.decrypt(cipher)
		return decrypted


rsa=RSAToFile()
if len(sys.argv)>2:
	mode = sys.argv[1]
	text = sys.argv[2]
	key = open(sys.argv[3], 'r').read()
	if mode == 'e':
		rsa.loadrsa(key)
		rsa.encrypt(text)
	elif mode == 'd':
		rsa.loadrsa(key)
		text = open(text,'r').read()
		rsa.decrypt(text)
		print rsa.decrypt(text)
else:
	rsa.generate()
	rsa.private()
	rsa.public()
