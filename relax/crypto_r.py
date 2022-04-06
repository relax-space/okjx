from base64 import b64decode, b64encode

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


class CryptoR():

    def __init__(self, key: str, iv: str):
        self.aes = AES.new(key.encode('utf8'), AES.MODE_CBC, iv.encode('utf8'))

    def encrypto(self, text: str) -> str:
        p = pad(text.encode('utf8'), AES.block_size)
        return b64encode(self.aes.encrypt(p)).decode('utf8')

    def decrypto(self, text: str) -> str:
        d = self.aes.decrypt(b64decode(text))
        return unpad(d, AES.block_size).decode('utf8')
