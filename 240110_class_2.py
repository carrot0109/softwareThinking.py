
'''
날짜 : 1월 10일
작성자 : 유근오
실습 내용 : 웹스크래핑
'''

##############################

import re
import urllib.request
url = "http://goo.gl/U7mSQl"    # 접속할 웹 페이지
html = urllib.request.urlopen(url)  # 웹 페이지 열기
html_contents = str(html.read())    # 웹 페이지의 내용을 문자열로
id_results = re.findall(r"([A-Za-z0-9]+\*\*\*)",html_contents)
# findall 전체 찾기, 정규 표현식 패턴대로 데이터 찾기
for i in id_results:    
    print(i)
