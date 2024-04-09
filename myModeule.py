def sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

def power(x, n):
    prod = 1
    for i in range(1, n+1):
        prod *= x
    return prod

# 모듈로 사용될 때는 실행되지 않음
if __name__ == '__main__':
    print(sum(5))
    print(power(2, 3))