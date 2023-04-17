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
print(subway.pop()) # ['d']
print(subway) #['a', 'e', 'b', 'c']

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("a")
print(subway) # ['a', 'e', 'b', 'c', 'a']
print(subway.count("a")) # 2

# 정렬
num_list = [5,2,4,3,1]

# 순서대로 정렬
num_list.sort()
print(num_list)

# 역순으로 정렬
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

# list 에는 다양한 자료형을 함께 넣어 사용가능
mix_list = ["a", 20, True]
print(mix_list)

# list 확장
num_list = [5,2,4,3,1]
mix_list = ["a", 20, True]
num_list.extend(mix_list)
print(num_list)



# dictionary : {key : value}

dict = {"이름" : "상아", "나이" : 25, "성별" : "여성"}

# 해당 value 출력 (key가 dictionary에 있을 경우)
print(dict["이름"]) # 상아
print(dict.get("이름")) # 상아

# 해당 value 출력 (key가 dictionary에 없을 경우)
# print(dict["취미"]) # error 발생
print(dict.get("취미")) # None
 # key의 기본값 설정(key가 dictionary에 없을 경우, 기본값 출력)
print(dict.get("취미","내용없음"))

# key가 dictionary에 있는지 확인
print("나이" in dict) # True
print("취미" in dict) # False

# key의 값 (재)설정
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



# tuple : (), list와 달리, 내용 변경 및 추가가 불가능하지만, 속도가 더 빠름
# 변경되지 않는 목록을 쓸 때 사용

menu = ("돈까스","치즈까스") 
print(menu[0]) # 돈까스
print(menu[1]) # 치즈돈까스
menu.add("생선까스") # error 발생(tuple은 내용수정 불가)

name = "박상아"
age = 25
hobby = "코딩"
print(name, age, hobby)
# tuple을 활용해서, 여러 변수 한줄에 선언하기
name, age, hobby = ("박상아", 25, "코딩") 
print(name, age, hobby)



# set(집합)
# 중복 안됨, 순서 없음

set = {1,2,3,3,3}
print(set)

java = {'유재석', '김태호', '양세형'}
python = set(['유재석', '박명수'])

# 교집합 (java 와 python 을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (java 할 수 있거나 python 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (java 할 수 있지만 python은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

# 값 추가 (python 할 줄 아는 사람이 늘어남)
python.add('김태호')
print(python)

# 값 삭제 (java를 까먹음)
java.remove('김태호')
print(java)



# 자료구조의 변경

menu = {'커피', '우유', '주스'}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))



# [퀴즈] 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.

# 조건1 : 편의상 댓글을 20명이 작성하였고, 아이디는 1~20 이라고 가정
# 조건2 : 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈과 shuffle 과 sample 을 활용

# 첫번째 내 답
from random import *
lst = []

for i in range(1,21):
    lst.append(i)

luck = sample(lst, 4)
coffe = sample(luck,3)
coffe.sort()
chicken = set(luck)-set(coffe)

chicken = list(map(str,chicken))
chicken = ''.join(chicken)

print("-- 당첨자 발표 --")
print("치킨 당첨자 :", chicken)
print("커피 당첨자 :", coffe)
print("-- 축하합니다 --")


# 두번째 내 답
from random import *
lst = list(range(1,21))
luck = sample(lst,4)
shuffle(luck)

chicken = luck[0]
coffe = luck[1:]
coffe.sort()

# coffe = list(map(str,coffe))
# coffe = ', '.join(coffe)

print("-- 당첨자 발표 --")
print("치킨 당첨자 :", chicken)
print("커피 당첨자 :", coffe)
print("-- 축하합니다 --")

# (추가) 문자열 포맷 활용하기
print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(chicken))
print("커피 당첨자 : {0}".format(coffe))
print("-- 축하합니다 --")





