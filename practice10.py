# [참고글] 라이브러리, 패키지, 모듈의 차이
# https://aliencoder.tistory.com/20

# 모듈 
# : 함수 정의나 클래스 등 서로 관련이 있거나 비슷한 기능을 하는 파이썬 문장들을 담고 있는 파일
# 모듈의 확장자는 py (*확장자란? 컴퓨터 파일의 이름에서 파일의 종류와 그 역할을 표시하기 위해 사용하는 부분)

import theater_module
theater_module.price(3) # 3명이서 영화보러 갔을 때 가격
theater_module.price_morning(4) # 4명이서 조조 할인 영화보러 갔을 때 가격
theater_module.price_soldier(5) # 5명이서 군인 할인 영화보러 갔을 때 가격

import theater_module as mv # 모듈 theater_module 을 mv 로 줄여서 호출하겠다는 의미(mv 라고 별명 설정)
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

from theater_module import *  # theater_module의 전부(*)를 가져와라
price(3)
price_morning(4)
price_soldier(5)

from theater_module import price, price_morning  # theater_module의 일부(price, price_morning 함수)만 가져와라
price(5)
price_morning(6)
# price_soldier(5)  # import 안한 price_soldier 함수는 사용불가(오류발생)

from theater_module import price_soldier as price
# 모듈 theater_module 에서 함수 price_soldier 를 가져다 쓰는데, 별명을 price로 한다는 의미
price(5) # 모듈 theater_module 의 price 함수와 다름 주의

##############################################################################################################

# 패키지 : 모듈을 모아놓은 집합, 하나의 디렉토리에 여러 모듈 파일들을 모아놓은 것 
# [참고글] 폴더와 디렉토리의 차이 https://technote.kr/287

import travel.thailand                      # import 패키지.ㅁㅁ 
# import travel.thailand.ThailandPackage    # ㅁㅁ 에는 모듈이나 패키지만 가능 (클래스나 함수는 불가)
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

from travel.thailand import ThailandPackage   # from 패키지.모듈이나 패키지 import 클래스나 함수 : 이건 가능
trip_to = ThailandPackage()
trip_to.detail()

from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()

##############################################################################################################

# __all__ : 사용권한을 주는 역할
# __all__ = ["모듈 이름"] → 해당 모듈을 사용할 수 있게 함

# from random import *  # random 모듈의 (사용권한이 있는) 모든 것을 가져와라
from travel import *    # travel 패키지의 (사용권한이 있는) 모든 것을 가져와라 (사용 권한이 없으면 모듈 사용불가)
                        # 사용 권한은 패키지 안의 __init__.py 파일에서 __all__ 을 활용해서 설정
trip_to = vietnam.VietnamPackage()
trip_to = thailand.ThailandPackage()
trip_to.detail()

##############################################################################################################

# 모듈 직접실행 
# 패키지 않의 모듈 파일 안에서 직접 실행해 볼 수 있음 (모듈이 잘 작동하는지 테스트하는 용도)
# (thailand.py 파일에서 코드 작성함)

from travel import *
trip_to = thailand.ThailandPackage()
trip_to.detail()

##############################################################################################################

# 패키지, 모듈 위치
# 1) 현재 작성중인 스크립트가 있는 폴더(동일한 경로의 폴더)
# 2) 파이썬 내의 라이브러리들이 모여있는 폴더(C:\Python311\Lib)
# => 패키지나 모듈이 둘 중 하나에는 위치해야 이를 호출할 수 있음


import inspect # inspect 모듈 호출(*inspect : 조사하다, 검사하다)

import random
print(inspect.getfile(random)) # C:\Python311\Lib\random.py
                               # inspect 모듈에서 gefile(모듈명)을 쓰면, 해당 모듈 파일의 위치를 알 수 있음

from travel import *
print(inspect.getfile(thailand)) # c:\Users\smile\Desktop\개발 공부\Python\travel\thailand.py

##############################################################################################################

# pip install : pip 로 패키지(라이브러리) 설치하는 법
# 1. pypi 웹사이트에서 패키지 검색
# 2. 터미널에 pip install 패키지명, 작성 후 실행

# pip list                       : 설치된 패키지 목록 보기
# pip show 패키지명               : 패키지 정보 보기
# pip install --upgrade 패키지명  : 패키지 업그레이드
# pip uninstall 패키지명          : 패키지 삭제

# [실습] beautifulsoup4 설치 후 예시코드
# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())

##############################################################################################################

# 내장 함수 : import 없이 사용가능

# input : 사용자 입력을 받는 함수
language = input("무슨 언어를 좋아하세요? ")
print(f"{language}은 아주 좋은 언어입니다!")

# dir : 어떤 객체를 넘겨줬을 때, 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
print(dir())
import random # 외장 함수 호출
print(dir()) # random 이 추가되서 출력
import pickle
print(dir()) # pickle이 추가되서 출력

# print(dir(random)) # random 모듈에서 쓸 수 있는 것들이 출력됨(randint, randrange, shuffle 등등)
lst = [1, 2, 3]
print(dir(lst)) # 리스트 lst 에서 쓸 수 있는 것들이 출력됨(append, count, index 등등)
name = "Sang"
print(dir(name)) # 문자열 name 에서 쓸 수 있는 것들이 출력됨(isupper, islower, split 등등)

# 파이썬 내장함수 목록 사이트
# https://docs.python.org/ko/3/library/functions.html

##############################################################################################################

# 외장 함수 : import 해야 사용가능

# 파이썬 외장함수 목록 사이트
# https://docs.python.org/ko/3/py-modindex.html#cap-a


# glob : 현재 경로 내의 폴더나 파일 목록 조회 (윈도우 dir)
import glob
print(glob.glob("*.py")) # 현재 경로 내에서, 확장자가 py 인 모든 파일을 출력해라


# os : 운영체제에서 제공하는 기본 기능(ex. 폴더 생성, 폴더 삭제 등)

import os
print(os.getcwd()) # 현재 디렉토리 표시
                   # [참고글1] 경로와 디렉토리 https://wikidocs.net/141353
                   # [참고글2] 폴더와 디렉토리 https://technote.kr/287

folder = "sample_dir"
if os.path.exists(folder): # sample_dir 라는 폴더가 존재한다면..
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder)
    print(folder, "폴더를 삭제하였습니다.")
else:
    os.makedirs(folder) # sample_dir 라는 폴더 생성
    print(folder, "폴더를 생성하였습니다.")

print(os.listdir()) # 현재 작업 디렉토리 내의 폴더와 파일 목록 출력(glob 모듈의 glob() 함수와 비슷)


# time, datetime : 시간 관련 함수를 제공하는 모듈
import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S")) # "년-월-일 시:분:초" 형태로 시간 출력

import datetime
print("오늘 날짜는", datetime.date.today())
# timedelta : 두 날짜 사이의 간격
today = datetime.date.today() # today : 오늘 날짜
td = datetime.timedelta(days=100) # td : 100일
print("우리가 만난지 100일은", today + td) # today + td : 오늘부터 100일 후 날짜

##############################################################################################################

# 퀴즈
# 프로젝트 내에 나만의 시그니처를 남기는 모듈을 만드시오

# 조건: 모듈 파일명은 byme.py 로 작성

# (모듈 사용 예제)
# import byme
# byme.sign()

# (출력 예제)
# 이 프로그램은 나도코딩에 의해 만들어졌습니다.
# 유튜브: http://youtube.com
# 이메일: nadocoding@gmail.com

import byme
byme.sign()