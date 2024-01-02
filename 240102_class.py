
'''
날짜 : 1월 2일
작성자 : 유근오
실습 내용 : 반복문 예제, 리스트
'''

#############################################################################################

'''1.달리기 경주'''
import turtle
import random

t1 = turtle.Turtle()
t2 = turtle.Turtle()

s = turtle.Screen()

s.title("달리기 경주")
s.bgpic("배경.png")

image1 = "마리오.gif"
image2 = "루이지.gif"

s.addshape(image1)
s.addshape(image2)

t1.shape(image1)
t2.shape(image2)

t1.up()
t2.up()

t1.speed(0)
t2.speed(0)

t1.goto(-350,-20)
t2.goto(-350,-200)

t1.speed(1)
t2.speed(1)

for i in range(30):
    t1.fd(random.randint(1,40))
    t2.fd(random.randint(1,40))

###############################################################################################

'''2.영화 예매 프로그램'''
print("--좌석 예매 프로그램--")
seat = [0,0,0,0,0,0,0,0,0,0]
while True:
    print("좌석을 예약하시겠습니까?(YES or NO)")
    movie = input('')
    if movie == 'YES' or movie == 'yes':
        print("원하는 좌석을 선택하세요 :")
        pick = int(input("1번~10번"))
        if pick >= 1 and pick <= 10:
            if(seat[pick-1]) == 0:
                seat[pick-1] = 1
                print(pick,"번 좌석이 예매되었습니다.!!!")
                print("-------------------------------------")
                print(seat)
                print("-------------------------------------")

            else:
                print("이미 예약된 자리입니다.")
    elif movie == 'NO' or movie == 'no':
        print("좌석예매를 종료합니다.")
        break
    else:
        continue
