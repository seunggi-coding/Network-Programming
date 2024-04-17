def sum(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + i
    return sum

def power(x, n):
    prod = 1
    for i in range(1, n+1):
        prod = prod * x
    return prod

# 이 파일은 사용자 정의 모듈인데 모듈을 독립된 프로그램으로 사용할 때만 실행된다.
if __name__ == '__main__':
    print(sum(5))
    print(power(2, 3))