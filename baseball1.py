import random

def refree(aw1, aw2, aw3, ent) :
    if ent == aw1  :
        print('Strike')
    elif ent == aw2 :
        print('Ball')
    elif ent == aw3 :
        print('Ball')
    else :
        print('Out')

one_more_trial = "1"
while True :
    if one_more_trial == "0" : break
    a = str(random.randint(100,1000))
    print(a)
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
