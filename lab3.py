from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from sympy import randprime
# 1. odbiorca
p = randprime(pow(2, 128), pow(2, 129))
q = randprime(pow(2, 128), pow(2, 129))
n = p * q
fi = (p-1)*(q-1)
e = 65537
d = pow(e, -1, fi)
# 2. nadawca (nadawca dostaje e i n)
w = b"hello"
kl = get_random_bytes(32)
cipher = AES.new(kl, AES.MODE_EAX)
nonce = cipher.nonce
krypto, tag = cipher.encrypt_and_digest(pad(w, 32))
klt = pow(int.from_bytes(kl), e, n)
#3. odbiorca dostaje
klo = pow(klt, d, n)
cipher = AES.new(klo.to_bytes(32), AES.MODE_EAX, nonce=nonce)
w2 = cipher.decrypt(krypto)
print(unpad(w2, 32))

