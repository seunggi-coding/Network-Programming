def Squares(n):
    return n**2
numbers = [1, 3, 5, 9]
print(list(map(Squares, numbers)))


# 위의 코드를 람다로 변환
print("결과는 ", list(map(lambda x: x**2, [1, 3, 5, 9])))