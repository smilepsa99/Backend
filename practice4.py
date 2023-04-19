# list : [], 순서가 있는 객체의 집합

subway = ["a","b","c"]

# b는 몇 번째 칸에 타고 있는가?
print(subway.index("b")) # 1
# index 1 칸에 누가 타고 있는가?
print(subway[1]) # b

# d가 다음 정류장에서 다음 칸에 탐
subway.append("d")
print(subway) #['a', 'b', 'c', 'd']

# e가 a와 b 사이의 칸에 탐
subway.insert(1,"e")
print(subway) #['a', 'e', 'b', 'c', 'd']

# 지하철에 있는 사람을 한 명씩 뒷 칸부터 꺼냄
print(subway.pop()) # d
print(subway) #['a', 'e', 'b', 'c']

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("a")
print(subway) # ['a', 'e', 'b', 'c', 'a']
print(subway.count("a")) # 2

# 정렬
num_list = [5,2,4,3,1]

# 순서대로 정렬
num_list.sort()
print(num_list) # [1, 2, 3, 4, 5]

# 역순으로 정렬
num_list.reverse()
print(num_list) # [5, 4, 3, 2, 1]

# 모두 지우기
num_list.clear()
print(num_list) # []

# list 에는 다양한 자료형을 함께 넣어 사용가능
mix_list = ["a", 20, True]
print(mix_list) # ['a', 20, True]

# list 확장
num_list = [5,2,4,3,1]
mix_list = ["a", 20, True]
num_list.extend(mix_list)
print(num_list) # [5, 2, 4, 3, 1, 'a', 20, True]

#################################################################################################################

# dictionary : {key : value}

dict = {"이름" : "상아", "나이" : 25, "성별" : "여성"}

# 해당 value 출력 (key가 dictionary에 있을 경우)
print(dict["이름"]) # 상아
print(dict.get("이름")) # 상아

# 해당 value 출력 (key가 dictionary에 없을 경우)
print(dict["취미"]) # error 발생
print(dict.get("취미")) # None
 # key의 기본값 설정(key가 dictionary에 없을 경우, 기본값 출력)
print(dict.get("취미","내용없음"))

# key가 dictionary에 있는지 확인
print("나이" in dict) # True
print("취미" in dict) # False

# key 추가 (기존 key의 값 재설정도 가능)
dict["취미"] = "그림"
print(dict) # {"이름" : "상아", "나이" : 25, "성별" : "여성", "취미" : "그림"}
dict["나이"] = 26
print(dict) # {"이름" : "상아", "나이" : 26, "성별" : "여성"}
# key 삭제
del dict["나이"]
print(dict) # {"이름" : "상아", "성별" : "여성"}

# key 만 출력
print(dict.keys()) # dict_keys(['이름', '성별'])
# value 만 출력
print(dict.values()) # dict_values(['상아', '여성'])
# key 와 value를 쌍으로 출력
print(dict.items()) # dict_items([('이름', '상아'), ('성별', '여성')])

# 모든 key 삭제
# dict.clear()
# print(dict) # {}

#################################################################################################################

# tuple : (), list와 달리, 내용 변경 및 추가가 불가능하지만, 속도가 더 빠름
# 변경되지 않는 목록을 쓸 때 사용

menu = ("돈까스","치즈까스") 
print(menu[0]) # 돈까스
print(menu[1]) # 치즈돈까스
menu.add("생선까스") # error 발생(tuple은 내용수정 불가)

name = "박상아"
age = 25
hobby = "코딩"
print(name, age, hobby) # 박상아 25 코딩
# tuple을 활용해서, 여러 변수 한줄에 선언하기
name, age, hobby = ("박상아", 25, "코딩") 
print(name, age, hobby) # 박상아 25 코딩

#################################################################################################################

# set(집합)
# 중복 안됨, 순서 없음

myset = {1,2,3,3,3}
print(myset) # {1, 2, 3}

java = {'유재석', '김태호', '양세형'}
python = set(['유재석', '박명수'])

# 교집합 (java 와 python 을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))
# => {'유재석'}

# 합집합 (java 할 수 있거나 python 할 수 있는 개발자)
print(java | python)
print(java.union(python))
# => {'김태호', '양세형', '유재석', '박명수'} (*순서는 랜덤, 이하동일)

# 차집합 (java 할 수 있지만 python은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))
# => {'김태호', '양세형'}


# 값 추가 (python 할 줄 아는 사람이 늘어남)
python.add('김태호')
print(python)
# => {'유재석', '박명수', '김태호'}


# 값 삭제 (java를 까먹음)
java.remove('김태호')
print(java)
# => {'유재석', '양세형'}

#################################################################################################################

# 자료구조의 변경

menu = {'커피', '우유', '주스'}
print(menu, type(menu)) # {'커피', '우유', '주스'} <class 'set'>

menu = list(menu)
print(menu, type(menu)) # ['커피', '우유', '주스'] <class 'list'>

menu = tuple(menu)
print(menu, type(menu)) # ('커피', '우유', '주스') <class 'tuple'>

menu = set(menu)
print(menu, type(menu)) # {'커피', '우유', '주스'} <class 'set'>

#################################################################################################################

# [퀴즈] 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.

# 조건1 : 편의상 댓글을 20명이 작성하였고, 아이디는 1~20 이라고 가정
# 조건2 : 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈과 shuffle 과 sample 을 활용

# 첫번째 내 답
from random import * # random 모듈 사용(shuffle, sample 사용하기 위해)
lst = [] # lst 라는 변수 = 텅 빈 리스트

for i in range(1,21): # i에 1이상 21미만 숫자를 넣을건데
    lst.append(i) # 그때마다 i를 lst에 추가해라
# => lst = [1, 2, 3, ... , 19, 20] 생성

luck = sample(lst, 4) # luck 라는 변수 = lst에서 4개를 무작위로 뽑아 만든 리스트
coffe = sample(luck,3) # coffe 라는 변수 = luck에서 3개를 무작위로 뽑아 만든 리스트
coffe.sort() # coffe 의 요소를 순서대로 정렬
chicken = set(luck)-set(coffe) # chicken 라는 변수 = 집합으로 바꾼 luck과 coffe의, 차집합

chicken = list(map(str,chicken)) # chicken 의 요소를 문자열로 바꾸고(map()), 자료구조를 집합에서 리스트로 변환(list())
chicken = ''.join(chicken) # chicken 의 요소를 합쳐서 문자열로 변환(ex. chicken = [1] → chicken = '1')

print("-- 당첨자 발표 --") # -- 당첨자 발표 --
print("치킨 당첨자 :", chicken) # 치킨 당첨자 : 1 (lst에서 뽑은 4개의 요소 중 3개의 요소를 뽑아 뺀 나머지 한개)
print("커피 당첨자 :", coffe) # 커피 당첨자 : [2, 3, 4] (lst에서 뽑은 4개의 요소 중 3개의 요소를 뽑은 것)
print("-- 축하합니다 --") # -- 축하합니다 --


# 두번째 내 답(첫번째 답이 너무 복잡하게 나와서 다시 함)
from random import * # random 모듈 사용(shuffle, sample 사용하기 위해)
lst = list(range(1,21)) # lst 라는 변수 = 1이상 21미만의 range를 list로 변환한 것
                        # range() : 연속된 숫자(정수)를 만들어주는 함수
luck = sample(lst,4) # luck 라는 변수 = lst에서 4개를 무작위로 뽑아 만든 리스트
shuffle(luck) # luck의 요소들의 순서를 섞어라

chicken = luck[0] # chicken 라는 변수 = luck 의 요소 중 index 값이 0인 요소(type : int)
coffe = luck[1:] # coffe 라는 변수 = luck 의 요소 중 index 값이 1인 요소부터 끝 요소까지(type : list)
coffe.sort() # coffe 의 요소를 순서대로 정렬

# coffe = list(map(str,coffe)) # chicken 의 요소를 문자열로 바꾸고(map()), 자료구조를 집합에서 리스트로 변환(list())
# coffe = ', '.join(coffe) # chicken 의 요소 사이사이에 ', '를 넣고 합쳐서 문자열로 변환
                           # (ex. coffe = ['2', '3', '4'] → chicken = '2, 3, 4')

print("-- 당첨자 발표 --")
print("치킨 당첨자 :", chicken) # 치킨 당첨자 : 1 (lst에서 뽑은 4개의 요소 중 index 값이 0인 요소)
print("커피 당첨자 :", coffe) # 커피 당첨자 : 2, 3, 4 (lst에서 뽑은 4개의 요소 중 index 값이 1 이상인 요소들)
print("-- 축하합니다 --")

# (추가) 문자열 포맷 활용하기
print("-- 당첨자 발표 --")
print("치킨 당첨자 : {}".format(chicken))
print("커피 당첨자 : {}".format(coffe))
print("-- 축하합니다 --")





