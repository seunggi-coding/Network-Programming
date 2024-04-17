from random import randint

total_money = 50  # 플레이어의 초기 자본은 $50

# 플레이어의 자본이 $0 초과이고 $100 미만일 때 게임 계속
while(total_money > 0 and total_money < 100):
    user_choice = int(input("앞면(1) 또는 뒷면(2)을 맞추시오. >> "))  # 사용자로부터 앞면 또는 뒷면 선택 입력 받음
    coin = randint(1, 2)  # 동전 던지기 결과를 무작위로 결정(1: 앞면, 2: 뒷면)

    # 사용자의 선택이 유효한 경우(1 또는 2)
    if(user_choice == 1 or user_choice == 2):
        # 사용자가 결과를 정확히 맞춘 경우
        if((coin == 1 and user_choice == 1) or (coin == 2 and user_choice == 2)):
            total_money += 9  # 정확히 맞추면 $9 획득
            print(f"현재 플레이어가 가진 돈은 총 ${total_money}입니다.")
        # 사용자가 결과를 틀린 경우
        elif((coin == 1 and user_choice == 2) or (coin == 2 and user_choice == 1)):
            total_money -= 10  # 틀리면 $10 손실
            print(f"현재 플레이어가 가진 돈은 총 ${total_money}입니다.")
        # 그 외의 경우는 발생하지 않으므로, 이 else 절은 필요 없음
    else:
        # 사용자가 1 또는 2 이외의 값을 입력한 경우
        print("잘못 입력했습니다.")
        continue  # 다시 입력받기 위해 반복문의 처음으로 돌아감
# 게임 종료 후 최종 자본 금액 출력
print(f"플레이어가 소지한 최종 금액은 ${total_money}입니다.")
