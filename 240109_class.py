
'''
날짜 : 1월 9일
작성자 : 유근오
실습내용 : 파일 입출력
'''

###############################################
'''
# ex1. 줄바꿈 기호 삭제 : strip()
f = open('파일.txt',encoding='utf8')
line = f.readline().strip() # strip() 함수를 사용하여 공백 삭제
while line != '':
    print(line)
    line = f.readline().strip()
f.close()
# lstrip 의 경우 줄바꿈 문자가 오른쪽에 있기 때문에 소용 없이 줄이 바뀜

# ex2. writelines() 입력받은 라인 파일에 쓰기
outfile = open('new.txt','a',encoding='utf8')
while True:
    outstr = input('내용 입력 : ')
    if outstr != '':
        outfile.writelines(outstr+'\n') # '\n' 을 통해 다음줄로 넘어감
    else:
        break  
outfile.close()
# a(append)모드 사용 시 기존 파일 내용이 삭제되지 않고 계속 사용됨

# ex3. read() write() : 한 번에 읽고 한 번에 쓰기
infilename = input('입력 파일 이름 : ')
outfilename = input('출력 파일 이름 : ')

infile = open(infilename,'r',encoding='utf8')
outfile = open(outfilename,'w',encoding='utf8')

s = infile.read()   # 읽은 내용 전부 s 에 저장
outfile.write(s)    # s에 저장된 내용 전부 outfile 에 작성

infile.close()
outfile.close()
'''
######################################################
'''
# 실습 1.
filename = input('파일 이름을 입력하세요 : ')
infile = open(filename,'r',encoding='utf8')
count = 0

for line in infile:
    for c in line.replace('\n','').replace(' ','').replace('★',''):
        count += 1
    

print('파일 안에는 총',count,'개의 글자가 있습니다.')
infile.close()

# 실습 2.
filename = input('파일 이름을 입력하세요 : ')
delete = input('삭제할 문자열 입력 : ')

infile = open(filename,'r',encoding='utf8')

data = ''
for i in infile:
    data += i.replace(delete,'')

infile.close()

infile2 = open(filename,'w',encoding='utf8')
infile2.write(data)

infile2.close()
'''
# 실습 3.
filename1 = input('입력 파일 이름을 입력하세요 : ')
infile = open(filename1,'r',encoding='utf8')
filename2 = input('출력 파일 이름을 입력하세요 : ')
outfile = open(filename2,'w',encoding='utf8')

sum = 0.0
count = 0

line = infile.readline()

while line !='':
    a = float(line)
    sum += a
    count += 1
    line = infile.readline()
    
outfile.write('합계:'+str(sum)+'\n')

avg = sum / count

outfile.write('평균:'+str(avg)+'\n')

infile.close()
outfile.close()


