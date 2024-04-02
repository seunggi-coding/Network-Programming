def sum(n):
    hab = 0
    for i in range(1, n+1):
        hab += i
    return hab

a = sum(50)
b = sum(1000)
print(a)
print(b)