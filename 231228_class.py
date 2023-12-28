
'''
날짜 : 12월 28일
작성자 : 유근오
실습 내용 : 조거문 + 터틀그래픽
'''

#############################################################################################

'''터틀 그래픽 모듈'''
'''
# 모듈을 불러오는 형식 : import 모듈 이름
# 모듈 제공하는 함수 사용 형식 : 모듈이름.함수이름() --> ex) turtle.shape()
import turtle as t    # 터틀 그래픽 모듈을 t라는 별칭으로 사용

# fd(distance) : 전진(forward)
t.fd(300)

# shape('모양')
t.shape('turtle')

# lt(angle) : 왼쪽으로 회전(left turn)
# rt(angle) : 오른쪽으로 회전(right turn)

# color(" ") : 선 색상
# ex) t.color("black")

# 삼각형 만들기
t.speed(0)
t.color("green")
t.fd(300)
t.lt(120)
t.fd(300)
t.lt(120)
t.fd(300)
t.lt(120)

# circle(radius) : 원 그리기
t.color("red")
t.circle(150)

# speed() : 속도(1~10,0)

# down() : 펜을 그리면서 이동
# up() : 펜을 들고 이동

# pensize(크기) : 펜 크기

# fillcolor("색상") : 색상 채우기(채울 색상 선택)

# begin_fill() : 채우기 시작

# end_fill() : 채우기 끝

# shapesize() : 도형 사이즈

# ht() : 도형 숨기기

# bk(distance) : 후진

# ex1. 사각형을 그린 후 다른 위치에 육각형을 그리는 예제(터틀그래픽)
import turtle as t

t.shape('turtle')
t.shapesize(5) 
t.pensize(5)
t.speed(0)

t.color("green")
t.begin_fill()
t.fd(150)
t.lt(90)
t.fd(150)
t.lt(90)
t.fd(150)
t.lt(90)
t.fd(150)
t.end_fill()

t.up()
t.fd(100)

t.down()
t.color("red")
# t.fillcolor("green")
t.begin_fill()
t.fd(100)
t.rt(60)
t.fd(100)
t.rt(60)
t.fd(100)
t.rt(60)
t.fd(100)
t.rt(60)
t.fd(100)
t.rt(60)
t.fd(100)
t.rt(60)
t.end_fill()
t.ht()
t.bk(100)
'''

####################################################################################################

'''조건문_2'''
'''
# ex2. 학과를 입력 받아서 ???학부에 오신 것을 환영합니다. 출력
import turtle as t
t.shape("turtle")

major = t.textinput("학과","당신의 학과는?")    # textinput("제목","출력할 문자열") : 터틀그 래픽에서 문자열 입력
t.write(major + " 학부에 오신 것을 환영합니다.")    # write("문자열" + 변수) : 문자열 출력('+' 기호 사용)

# ex3. 동전 던지기 게임
import random as r

print("동전 던지기 게임 시작")
coin = r.randrange(2) # randrange(2) : 0 또는 1 난수 발생

if coin == 0:
    print("동전 앞면")
    print(coin)
else:
    print("동전 뒷면")
    print(coin)
print("게임 종료")

'''

# ex4. 휴양지 선택 예제
import turtle as t
import random as r

s = t.Screen()  # 스크린 객체 생성

image1 = "삿포로.gif"    # 추가할 이미지, gif 파일만 가능
image2 = "산토리니.gif"  # 또한 이미지 파일은 파이썬 파일과 동일한 곳에 위치
image3 = "스위스.gif"

s.addshape(image1)  # 스크린에 이미지 추가 --> 스크린에서 이미지 사용
s.addshape(image2)
s.addshape(image3)

vacation_spot = r.randint(1,3)  # randint(시작 정수, 마지막 정수) : 정수 난수를 발생 시킴

if vacation_spot == 1:
    t.shape(image1) # 이미지 설정
elif vacation_spot == 2:
    t.shape(image2)
else:
    t.shape(image3)












































