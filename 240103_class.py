
'''
날짜 : 1월 3일
작성자 : 유근오
실습 내용 : 딕셔너리, 함수
'''

#########################################################################

'''딕셔너리'''
'''
# 딕셔너리 : { key:value, key:value, key:value }

# ex1. 계절을 나타내는 딕셔너리 표현(영어:한글)
season = {'spring':'봄', 'summer':'여름', 'autumn':'가을'}
print(season)

# ex2. 겨울 항목 추가
season['winter'] = '겨울'
print(season)

# ex3. 여름 항목 삭제
del(season['summer'])
print(season)

# ex4. 키로 값에 접근(가을 항목에 접근)
print(season['autumn'])
print(season.get('autumn')) # get함수 이용 시 () 활용

# ex5. 딕셔너리 모든 키 반환
print(season.keys())
print(list(season.keys()))  # list() 함수를 통해 dict_keys 삭제

# ex6. 딕셔너리 모든 값 반환
print(season.values())
print(list(season.values()))

# ex7. in 연산자
print('spring' in season)
print('summer' in season)

# ex8. 간단한 재고관리 프로그램
goods = {'우유':1, '종이컵':2, '책':5, '커피':7, '콜라':4, '펜':3}

while True:
    print('### 재고 목록 ###')
    print('우유',goods['우유'])
    print('종이컵',goods['종이컵'])
    print('책',goods['책'])
    print('커피',goods['커피'])
    print('콜라',goods['콜라'])
    print('펜',goods['펜'])

    print('====================')
    print('0.종료')
    print('1.재고추가')
    print('2.재고삭제')
    print('====================')

    cho = int(input('무엇을 하시겠습니까? : '))
    if cho == 0:
        print('프로그램 종료')
        break
    elif cho == 1:
        name = input('어떤 물건을 추가하시겠습니까? : ')
        much = int(input('추가할 수량을 입력하세요 : '))
        goods[name] += much
    elif cho == 2:
        name = input('어떤 물건을 삭제하시겠습니까? : ')
        much = int(input('삭제할 수량을 입력하세요 : '))
        goods[name] -= much
    else:
        continue
'''
#########################################################################

'''함수 리스트'''
'''
# ex9. 거북이 경주
import turtle
import random

t1 = turtle.Turtle()
t2 = turtle.Turtle()

t1.shape('turtle')
t2.shape('turtle')

t1.color('pink')
t2.color('skyblue')

t1.shapesize(3)
t2.shapesize(3)

t1.up()
t2.up()

t1.speed(0)
t2.speed(0)

t1.goto(-300,100)
t2.goto(-300,0)

t1.speed(1)
t2.speed(1)

for i in range(35):
    t1.fd(random.randint(1,30))
    t2.fd(random.randint(1,30))
'''

# ex10. 눈사람 그리기

import turtle as t
import random as r

t.ht()
t.title("눈사람 그리기")

t.speed(0)
t.bgcolor("black")
def snowman(color,radius,x,y):
    t.color(color)
    t.begin_fill()
    t.up()
    t.goto(x,y)
    t.down()
    t.circle(radius)
    t.lt(180)
    t.circle(radius)
    t.end_fill()

for i in range(40):
    color = r.choice(["white","yellow","gray","skyblue"])
    radius = r.randint(5,30)
    x = r.randint(-300,380)
    y = r.randint(-300,380)
    snowman(color,radius,x,y)






