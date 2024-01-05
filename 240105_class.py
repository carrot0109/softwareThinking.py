
'''
날짜 : 1월 5일
작성자 : 유근오
실습 내용 : 함수
'''

#######################################

'''함수'''
'''
# ex1. 두 수의 합을 구하는 함수
def hap(a,b):
    return a+b

a = 10
b = 20
c = hap(a,b)    # 반환값을 저장하는 변수
print(c)

a = 5
b = 10
print(hap(a,b)) # 바로 출력

# ex2. 입력받은 두 수의 곱을 구하는 함수
def gop(a,b):
    return a*b

a = int(input("첫 번째 수 : "))
b = int(input("두 번째 수 : "))

c = gop(a,b)
print(a,'*',b,'=',c)

# ex3. 국민대학교 문자열을 출력하는 함수
def kookmin():
    return '국민대학교'

print(kookmin())

# ex4. ex2번을 반환값이 없도록 바꿈
def gop(a,b):
    print('%d * %d = %d'%(a,b,a*b)) # c언어와 마찬가지로 %형식 사용(대신 %()를 통해 사용) 

a = int(input("첫 번째 수 : "))
b = int(input("두 번째 수 : "))
print(gop(a,b)) # 출력값이 없기 때문에 None이 출력됨

# ex5. 사용자로부터 단을 입력받아 구구단을 출력하는 함수
def Dan(dan):
    for i in range(1,10):
        print('%d X %d = %d'%(dan,i,dan*i))

dan = int(input("단을 입력하세요 : "))
Dan(dan)

# ex6. 1에서 100까지 합을 구하는 함수(리턴값이 없는 경우)
def hap(a,b):
    sum = 0
    for i in range(a,b+1):
        sum += i
    print('\n합 = %d'%(sum))

hap(1,100)
        
'''
# ex7. 딕셔너리 추가 예제
# 재고관리 프로그램
goods = {'노트북':1, '키보드':2, '마우스':5, '메모리':7, '그래픽 카드':4}

# for 변수명 in sorted(딕셔너리명.keys())
# 딕셔너리 항목을 키를 기준으로 오름차순으로 정렬
# 항목 업데이트 : 딕셔너리명.update({key:value})
while True:
    print('### 재고 목록 ###')
    for key in sorted(goods.keys()):    # 정리된 키 값 순서대로 key 변수에 저장
        print(key,goods[key])

    print('===================')
    print('0.종료')
    print('1.재고 추가')
    print('2.재고 삭제')
    print('===================')

    choice = int(input('무엇을 하시겠습니까?'))
    if choice == 0:
        print('프로그램 종료')
        break
    elif choice == 1:
        name = input('어떤 물건을 추가하시겠습니까? : ')
        much = int(input('추가할 수량을 입력하세요 : '))
        if name in goods:
            goods[name] += much
        else:
            goods.update({name:much})   # update 함수 활용
            # goods[name] = much
    elif choice == 2:
        name = input('어떤 물건을 삭제하시겠습니까? : ')
        much = int(input('삭제할 수량을 입력하세요 : '))
        goods[name] -= much
    else:
        continue
        

    





