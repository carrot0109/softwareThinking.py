
'''
날짜 : 1월 11일
작성자 : 유근오
실습 내용 : 웹 스크래핑
'''

#############################################
'''
# requests module
import re
import requests     # requests.get('url').text (모듈 설치 -> pip install requests)
url ="http://goo.gl/U7mSQl"
contents = requests.get(url).text   # get 요청 --> 불필요한 코드 생략
results = re.findall(r"([\w]+\*\*\*)",contents)
for i in results:
    print(i)

# 한글 정보(requests 모듈 활용)
import re
import requests
# import urllib.request

url ="https://yugeuno.netlify.app/"   # 사이트 만들 때 폴더 형식으로 넣기
contents = requests.get(url).text
# a = urllib.request.urlopen(url)
# contents = str(a.read().decode("utf8"))
results = re.findall(r"([가-힝0-9]+\*\*)",contents)
for i in results:
    print(i)
'''
# 삼성 주식
# 튜플(tuple) : 리스트와 동일하지만 값을 변경할 수 없음 [소괄호 사용 / 콤마로 구분]
import urllib.request
import re

url = "https://finance.naver.com/item/main.naver?code=005930"
html = urllib.request.urlopen(url)
html_contents = str(html.read().decode("ms949"))  # decode("ms949") : 한글로 정확하게 출력

stock_results = re.findall("(\<dl class=\"blind\"\>)([\s\S]+?)(\<\/dl\>)",html_contents)
# \<dl class=\"blind\"\> --> <dl class="blind">
# \s\S --> 어떠한 내용이 있다면..
# \</dl\> --> </dl>
samsung_stock = stock_results[0]    # 콤마로 나뉘어진 두 개의 튜플 중 첫 번째
samsung_index = samsung_stock[1]

index_list = re.findall("(\<dd\>)([\s\S]+?)(\<\/dd\>)",samsung_index)

for i in index_list:
    print(i[1]) # 세 개의 튜플 값 중 두 번째 

