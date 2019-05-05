import random

def refree(num1, num2, num3, answer) :
    if num1 == answer :
        print('strike')
    else :
        if num1 > answer :
            print('big')
        else :
            print('small')
    if num2 == answer :
        print('ball')
    elif num3 == answer :
        print('ball')
    elif num1 != answer :
        print('out')


print('숫자가 일치하면 strike, 일치하지 않으면 out 만약 다른 위치의 숫자와 동일하다면 ball을 표시해줍니다. ')
print('같은 위치의 숫자보다 더 크면 big 작으면 small을 표시해줍니다.')
print('만약 다른위치의 숫자와 일치한다면 big&small을 먼저 알려준뒤 다음 줄에 다른위치의 숫자와 일치 여부를 알려줍니다.')

one_more_trial = "1"
while True :
    if one_more_trial == "0" : break
    a = str(random.randint(100,1000))
    while True :
        try :
            q = input('Enter the three number :  ')
            refree(a[0], a[1], a[2], q[0])
            refree(a[1], a[2], a[0], q[1])
            refree(a[2], a[0], a[1], q[2])
            if a == q :
                print('Strike Out')
                one_more_trial = input("게임을 한번 더 하고 싶으시면 0이 아닌 숫자를 써주세요")
                break
            else :
                continue
        except Exception as e :
            print(e)
            print('There was a Error. Please Enter the three number')
