#자판기
try :
    money = int(input('돈을 넣어주세요 : '))
except :
    print('숫자만 입력해주세요')
    money = int(input('돈을 넣어주세요 : '))
while True :
    drink = '1'
    if drink == '0' : break
    elif drink == '1' :
        if money >= 0 :
            print('1번 콜라 1000원  2번 환타 1300원  3번 파워에이드 1500원 4번 레쓰비 600원 5번 물 500원 6번 금액추가 0번 주문그만하기')
            drink = input('구입하실 음료의 버튼을 눌러주세요 : ')
            if drink == '1' :
                money = money - 1000
            elif drink == '2' :
                money = money - 1300
            elif drink == '3' :
                money = money - 1500
            elif drink == '4' :
                money = money - 600
            elif drink == '5' :
                money = money - 500
            elif drink != '0' or '1' or '2' or '3' or '4' or '5' or '6' :
                 print('메뉴에 있는 숫자만 입력해주세요')
            if money < 0 :
                print('금액이 부족합니다')
                money = money + int(input('돈을 넣어주세요 : '))
            if drink == '0' : break
            if drink == '6' :
               money = money + int(input('돈을 넣어주세요 : '))

print('잔돈은', money, '원입니다.')
print('이용해주셔서 감사합니다')
