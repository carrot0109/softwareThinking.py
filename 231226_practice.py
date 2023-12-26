'''
날짜 : 12월 26일
작성자 : 유근오
실습 : 변수, 연산자
'''

# ex1. 논리연산자 and, or, not 사용하는 예제
a = 100
b = 200
print(a==100 and b==400)
print(a==100 and b==200)
print(a==100 or b==400)
print(a==100 or b==200)
print(not b==1000)

# ex2. 관계연산자 >=,== != 사용 예제
x = 10
y = 20
print(x>=y)
print(x==y)
print(x!=y)

# ex3. 산술연산자 %, ** 사용 예제
num1 = 10
num2 = 3
num3 = num1 % num2
num4 = num1 ** num2
print(num1,"%",num2,"=",num3)
print(num1,"**",num2,"=",num4)

# ex4. 학과와 학년을 입력받아, ???학과 ?학년 입니다. 출력
major = input("학과를 입력하세요: ")
grade = input("학년을 입력하세요: ")
print(major + "학과 " + grade + "학년 입니다.") 

# ex5. 이름과 나이를 입력받아, ???님은 ??살 입니다. 출력
name = input("이름을 입력해주세요: ")
age = input("나이를 입력해주세요: ")
print(name + "님은 " + age + "살 입니다.")

# ex6. 정수를 입력받아 짝수이면 짝수입니다. 출력, 홀수면 홀수입니다. 출력
NUM = int(input("정수를 입력하세요 : "))
if NUM % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")
