import hashlib

# print(hashlib.__all__)
a = 'string'
print(a, a.encode())
print(type(a), type(a.encode()))
print()
print(hashlib.sha1(a.encode()).hexdigest())
