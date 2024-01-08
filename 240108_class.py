
'''
날짜 : 1월 8일
작성자 : 유근오
실습 내용 : 문자열
'''

##################################
'''
# ex1. 인덱싱
# 본인의 영문 이름을 저장한 후 인덱싱하기    # 본인의 이름 첫 문자 출력
name = 'Yu geuno'
print(name[3])

# ex2. 인덱싱(본인 이름의 마지막 문자 출력)
name = 'Yu geuno'
print(name[-1])
print(name[7])

# ex3. 슬라이싱(본인 성 출력)
name = 'Yu geuno'
print(name[0:2])
print(name[:2])
print(name[:2:1])

# ex4. 슬라이싱(본인 이름 출력)
name = 'Yu geuno'
print(name[3:])
print(name[3:8])
print(name[3:8:1])

# ex5. 문자열 함수 7개 적용
a = 'software thinking'
print(a.upper())
print(a.lower())    
print(a.title())    # 문자열의 모든 단어의 앞글자를 대문자로 변환
print(a.capitalize())
print(a.count('ing'))   # 문자가 아닌 문자열이 들어가도 상관 없음
print(a.isdigit())   
print(a.startswith('s'))    # 문자가 아닌 문자열이 들어가도 상관 없음

# ex6. 이름과 키를 입력받아 출력하는 예제(형식(서식)지정자 사용)
# 키는 소수점 첫째자리까지 출력
name = input('이름을 입력해주세요:')
ki = float(input('키를 입력해주세요:'))
print('이름 : %s / 키 : %.1f'%(name,ki))   # 원래는 소수점 6자리까지 출력되는 것이 원칙

# ex7. 문자, 정수 형식지정자 사용
print('%c %d'%('A',51))

# 변수에 저장된 값 출력
bl = 'A'
year = 2024
print('%c %d'%(bl,year))

# ex8. format() 함수 
print('{} {}'.format('A',2024))

blood = 'A'
year = 2024
grade = 3.754
print('{0} {1} {2:.2f}'.format(blood,year,grade))   # 실수형 출력 유의

# ex9. 패딩
# 전체 자리수 5개(숫자 3개 삽입)
print('%d'%123) # 비교 코드 
print('%5d'%123)    # 5개의 칸을 비우고 오른쪽부터 정렬
print('%-5d'%123)   # '-'부호 사용 시, 왼쪽부터 정렬

# 전체 자리수 10개(실수, 소수점 둘째 자리까지 출력)
print('%f'%3.1415)
print('%10f'%3.1415)
print('%10.2f'%3.1415)
print('%-10.2f'%3.1415)
'''

##################################


'''파일 입출력'''
'''
# ex10. readline() 함수 사용
File = open('test_file.txt',encoding='utf8')
result = File.readline()    # 파일 열기 : open()
print(result)   # ENTER도 인식되기 때문에 한 줄 띄고 출력

result = File.readline()
print(result,end="")    # end를 통해 연이어 출력

File.close()

# ex11. 반복문 사용
File = open('test_file.txt',encoding='utf8')
while True:
    str = File.readline()
    if str == "":   # 읽어낸 행이 NULL값이면 정지
        break
    print(str,end="")       

File.close()

# ex12. readlines() (각각의 라인이 리스트 안에 저장)
File = open('test_file.txt',encoding='utf8')
result = File.readlines()
print(result)   # 출력 결과 : ['2024.01.08\n', '계절학기 수업\n', '\n', '20232093']
File.close()
'''
# ex13. readlines() 반복문 사용
File = open('test_file.txt',encoding='utf8')
result = File.readlines()   # result는 리스트
for i in result:
    print(i,end='')
File.close()






