
'''
날짜 : 1월 10일
작성자 : 유근오
실습 내용 : 파일 입출력, 문자열
'''

###########################################
'''
# ex1. split()함수
# 학교와 학과를 입력받기
univ,major = input('학교과 학과를 입력하세요:').split()  # 괄호 안에 공백이면 띄어쓰기로 구분
print(univ,major)

# ex2. split()함수, split('구분자')
univ,major = input('학교과 학과를 입력하세요:').split(',') 
print(univ,major)

# ex3. 두 정수를 입력받아 합을 구하는 예제
num1,num2 = input('정수 2개를 입력하세요:').split()  # 이 상태로는 정수형, 실수형으로 입력받을 수 없음 
print(int(num1)+int(num2))

# ex4. 두 실수의 합을 구하는 예제 : map( 자료형, input().split() ) 함수
a,b = map(float,input('실수 2개 입력:').split())
print('%.1f'%(a+b)) # 그냥 %f로 출력 시 소수점 6자리 출력
'''
###########################################

'''암호화/복호화'''
'''
# ex5. ord('문자 1개') / chr(숫자)
print(ord('유'))
print(chr(50976))

num = ord('유')
print(chr(num + 200))

num = ord('쟨')
print(chr(num - 200))
'''
# 암호 / 복호 프로그램
while True:
    which = int(input('1.암호화 2. 암호 해석 중 선택 : '))

    infilename = input('입력 파일명을 입력하세요 : ')
    infile = open(infilename,'r',encoding='utf8')

    outfilename = input('출력 파일명을 입력하세요 : ')
    outfile = open(outfilename,'w',encoding='utf8')

    if which == 1:
        choice = 100
    else:
        choice = -100

    instr = infile.readline()

    if not instr:
        break

    outstr = ''

    for i in range(0,len(instr)):
        ch = instr[i]
        chNum = ord(ch)
        chNum += choice
        ch2 = chr(chNum)
        outstr += ch2

    outfile.write(outstr)

    infile.close()
    outfile.close()







    
