a = 1
b = a.to_bytes(4, 'big')
print(b)
c = a.to_bytes(4, 'little')
print(c)

d = int.from_bytes(b, 'big')
print(d)
e = int.from_bytes(c, 'little')
print(e)