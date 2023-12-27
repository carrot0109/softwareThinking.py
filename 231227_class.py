
'''
날짜 : 12월 27일
작성자 : 유근오
실습내용 : 조건문
'''

#####################################################################################

'''조건문'''

# 형식 1. if 조건식:
#               조건이 참일 때 실행될 문장

# ex1. 정수를 입력받아 짝수인지 홀수인지 판단하는 예제
num_judged = int(input("정수를 입력하세요 : "))
if num_judged % 2 == 0:
    print("짝수입니다.\n")
    
# ex2. 학교 이름을 입력받아 국민대학교 학생인지 판단하는 예제
univ = input("학교 이름을 입력하세요 : ")
if univ == "국민대학교" or univ == "국민대":
    print(univ, "학생입니다.",'\n')

# 형식 2. if 조건식:
#               조건이 참일 때 실행될 문장
#         else:
#               조건이 거짓일 때 실행될 문장

# ex3. 정수를 입력받아 짝수인지 홀수인지 판단하는 예제
# 입력받은 정수가 짝수이면 ??은 짝수입니다. 혹은 홀수이면 ??은 홀수입니다. 출력
num_judged = int(input("정수를 입력하세요 : "))
if num_judged % 2 == 0:
    print(str(num_judged) + "은(는) 짝수입니다.",'\n')
else:
    print(str(num_judged) + "은(는) 홀수입니다.",'\n')

# ex4. 학교 이름을 입력받아 국민대학교 학생인지 판단하는 예제
# 국민대 학생이면 ???님은 국민대 학생입니다. 출력
# 아닌 경우에는 ???님은 국민대 학생이 아닙니다.
univ = input("학교 이름을 입력하세요 : ")
name = input("이름을 입력하세요 : ")
if univ == "국민대학교" or univ == "국민대":
    print(name + "님은",univ, "학생입니다.",'\n')
else:
    print(name + "님은","국민대학교 학생이 아닙니다.")
    print(name + "님은",univ, "학생입니다.",'\n')

# ex5. 아이디와 패스워드를 입력받아 저장된 아이디와 패스워드가 일치할 경우
# 로그인 성공! 출력. 그렇지 않은 경우에는 로그인 실패! 출력하는 예제
number = "carrot"
pw = "0109"

Number = input("아이디 입력 : ")
Pw = input("패스워드 입력 : ")

if Number == number and pw == Pw:
    print("로그인 성공!",'\n')
else:
    print("로그인 실패!",'\n')

# 형식 3. if 조건식:
#               조건이 참일 때 실행될 문장
#         elif 새로운 조건식:
#               if 조건식을 제외하고 새로운 조건이 참일 때 실행될 문장
#         else:
#               조건이 거짓일 때 실행될 문장

# ex6. 이름과 혈액형을 입력받아 A 또는 a 이면 ???님은 A형 입니다. 출력 예제. 그외도 동일
name = input("이름 입력 : ")
blood = input("혈액형 입력 : ")

if blood == "A" or blood == "a":    # blood == 'a' 대신 'a' 만 입력했을 경우 정확하지 않은 값 출력
    print(name,'님은 A형 입니다.\n')
elif blood == "B" or blood == "b":
    print(name,'님은 B형 입니다.\n')
elif blood == "O" or blood == "o":
    print(name,'님은 O형 입니다.\n')
elif blood == "AB" or blood == "ab":
    print(name,'님은 AB형 입니다.\n')
else:
    print("혈액형을 입력해주세요.\n")

# ex7. 소프트웨어사고 성적을 입력받아 90점 이상이면 A 학점, 80점 이상이면 B 학점, 70점 이상이면 C 학점
# 60점 이상이면 D학점, 그 외에는 F 학점 출력 예제
score = int(input("소프트웨어 성적 입력란 : "))
if score >= 90:
    print("A 학점")
elif score >= 80:
    print("B 학점")
elif score >= 70:
    print("C 학점")
elif score >= 60:
    print("D 학점")
else:
    print("F 학점")









































