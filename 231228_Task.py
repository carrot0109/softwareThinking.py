'''
날짜 : 12월 28일
작성자 : 유근오
과제 내용 : 점심 메뉴 선택
'''

import turtle as t
import random as r

s = t.Screen()

image1 = "치킨.gif"
image2 = "피자.gif"
image3 = "족발.gif"
image4 = "초밥.gif"

s.addshape(image1)
s.addshape(image2)
s.addshape(image3)
s.addshape(image4)

lunch = r.randrange(4)

if lunch == 0:
    t.shape(image1)
elif lunch == 1:
    t.shape(image2)
elif lunch == 2:
    t.shape(image3)
else:
    t.shape(image4)
