# p = 1
# q = 2
#
# n = p*q
#
# fi = (p-1) * (q-1)
# e = 65537
#
# NWD(e,fi) = 1
#
# d = e^(-1) mod fi
#
# y = x^e mod n
#
# x = y^d mod n

import random
import sympy
import math
import numpy

# def isprime(x):
#     for i in range(1, x):
#         if x % i == 0:
#             return False
#     return True
#
#
# p = random.randint(256, 512)
# q = random.randint(256, 512)
#
# while 1:
#     p = random.randint(256, 512)
#     if isprime(p):
#         break
#     #print("p = ", p)
#
# while 1:
#     q = random.randint(256, 512)
#     if isprime(q):
#         break
#     #print("q = ", q)
# print(p, q)

p = sympy.randprime(2 ** 16, 2 ** 17)
q = sympy.randprime(2 ** 16, 2 ** 17)

n = p * q
fi = (p - 1) * (q - 1)
e = 65537
print("gdc before:", math.gcd(e, fi))
while math.gcd(fi, e) != 1:
    p = sympy.randprime(2 ** 16, 2 ** 17)
    q = sympy.randprime(2 ** 16, 2 ** 17)
    fi = (p - 1) * (q - 1)
    print("gdc:", math.gcd(e, fi))
print(p, q, fi)
d = pow(e, -1, fi)
print("d:", d)
x = 23
y = (x ** e) % n
print(y)
print("decoded:", pow(y, d, n))
