import secrets
import hmac
import hashlib

class KeyGenerator:
    def __init__(self):
        self.key = secrets.token_hex(32).upper().encode()

class HMACGenerator:
    def __init__(self, key, msg):
        self.hmac = hmac.new(key, bytearray(msg), digestmod=hashlib.sha3_256)
        self.digest = self.hmac.hexdigest().upper()