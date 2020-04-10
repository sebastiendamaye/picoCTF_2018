#!/usr/bin/env python
from Crypto.Util.number import inverse # pycryptodome pip package

print("=== QUESTION #1 ===")
print("Possible: YES")
q = input("q: "); q = int(q)
p = input("p: "); p = int(p)
print("n =", p*q)

print("=== QUESTION #2 ===")
print("Possible: YES")
p = input("p: "); p = int(p)
n = input("n: "); n = int(n)
print("q =", int(n/p))

print("=== QUESTION #3 ===")
print("Possible: NO")

print("=== QUESTION #4 ===")
print("Possible: YES")
q = input("q: "); q = int(q)
p = input("p: "); p = int(p)
print("totient(n) =", (p-1) * (q-1))

print("=== QUESTION #5 ===")
print("Possible: YES")
plaintext = input("plaintext: "); plaintext = int(plaintext)
e = input("e: "); e = int(e)
n = input("n: "); n = int(n)
print("answer =", pow(plaintext, e, n))

print("=== QUESTION #6 ===")
print("Possible: NO")

print("=== QUESTION #7 ===")
print("Possible: YES")
q = input("q: "); q = int(q)
p = input("p: "); p = int(p)
e = input("e: "); e = int(e)
n = p*q
totient = (p-1)*(q-1)
d = inverse(e, totient)
print("answer =", d)

print("=== QUESTION #8 ===")
print("Possible: YES")
p = input("p: "); p = int(p)
c = input("ciphertext: "); c = int(c)
e = input("e: ") ; e = int(e)
n = input("n: "); n = int(n)
q = int(n/p)
totient = (p-1) * (q-1)
d = inverse(e, totient)
m = pow(c,d,n)
print("answer =", m)

print(hex(m)[2:].decode('hex'))
