import math

def cir_area(r):
    return math.pi * r**2

def cir_circum(r):
    return 2 * math.pi * r

area = cir_area(3.5)
circum = cir_circum(3.5)

print("원의 면적: %.1f" %(area))
print("원의 둘레: %.1f" % (circum))