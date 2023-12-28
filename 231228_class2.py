
'''
날짜 : 12월 28일
작성자 : 유근오
실습 내용 : while 반복문
'''

###############################################################################

'''while 반복문'''
'''
# ex1. 본인 이름을 10번 출력하는 예제
i = 0
while i<10:
    print("유근오", end = " ") # end = " " 를 통해 옆으로 나열 
    i += 1

# ex2. 1부터 10까지 합을 구하는 예제
i = 1
sum = 0
while i <= 10:
    sum += i
    i += 1
print("합 :",sum)

# ex3. 1부터 10까지 곱을 구하는 예제
i = 1
gop = 1     # 0 으로 초기화하면 총 곱은 0 이 되어버리기 때문에 1 로 초기화
while i <= 10:
    gop *= i
    i += 1
print("1부터 10까지 곱은",gop,"입니다")

# ex4. 단을 입력받아 구구단 출력
dan = int(input("출력할 단 : "))
i = 1
while i<=9:
    print(dan,"X",i,"=",dan*i)
    i += 1
'''
# ex5. 터틀그래픽으로 육각형 그리기
import turtle as t
t.shape("turtle")
i = 0
t.color("green")
t.speed(0)
t.begin_fill()
while i < 6:
    t.fd(100)
    t.lt(60)
    i += 1
t.end_fill()






































