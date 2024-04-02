# 인덱스를 이용하여 문자열의 문자를 역순으로

outStr = ""
count, i = 0, 0

inStr = input("Type string :")
count = len(inStr)

for i in range(0, count):
    outStr += inStr[count - (i + 1)]
print("Reversed string : %s" % outStr)