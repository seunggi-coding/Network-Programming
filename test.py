from random import randint

total_money = 50

while(total_money > 0 and total_money < 100):
    user_choice = int(input("앞면(1) 또는 뒷면(2)을 맞추시오. >> "))
    coin = randint(1, 2)

    if(user_choice == 1 or user_choice == 2):
        if((coin == 1 and user_choice == 1) or (coin == 2 and user_choice == 2)):
            total_money += 9
            print(f"현재 플레이어가 가진 돈은 총 ${total_money}입니다.")
        elif((coin == 1 and user_choice == 2) or (coin == 2 and user_choice == 1)):
            total_money -= 10
            print(f"현재 플레이어가 가진 돈은 총 ${total_money}입니다.")
        else:
            print("잘못 입력했습니다.")
            continue
    else:
        print("잘못 입력했습니다.")
        continue
print(f"플레이어가 소지한 최종 금액은 ${total_money}입니다.")
