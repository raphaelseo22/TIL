#자판기
money = int(input('돈을 넣어주세요 : '))
while True :
    left_money = '1'
    if left_money == '0' : break
    elif left_money == '1' :
        if money > 0 :
            print('1번 콜라 1000원  2번 환타 1300원  3번 파워에이드 1500원 4번 레쓰비 600원 5번 물 500원')
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
            if money < 0 :
                print('금액이 부족합니다')
                money = money + int(input('돈을 넣어주세요 : '))
            left_money = input('주문을 그만 하시려면 0 더 하시려면 1 금액을 추가하고 싶으시면 2를 입력해주세요 : ')
            if left_money == '0' : break
            if left_money == '2' :
               money = money + int(input('돈을 넣어주세요 : '))

print('잔돈은', money, '원입니다.')
print('이용해주셔서 감사합니다')
