# and 와 & 의 차이

x = None
y = 1

if x == None and y == 1:
    print("succeed")

# if x == None & y == 1:
#     print("succeed")  # => 에러발생


if (x == None) & (y == 1):
    print("succeed")

# [참고] 비슷한 연산자의 차이 https://velog.io/@kkiyou/py0040
############################################################################

# 리스트 슬라이싱

data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list1 = data_list[1:]
print(list1)
print(list1[0])
print(list1[1])

list2 = list1[1:]
print(list2)
print(list2[0])
print(list2[1])

# [참고] 파이썬 리스트 슬라이싱https://vision-ai.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-

############################################################################

# 람다(lambda)식 : 함수를 따로 선언하지 않고, lambda식으로 대체할 수 있음
# [참고] lambda 로 sorted key 정하기 https://pearlluck.tistory.com/462
# 함수 sorted() https://www.daleseo.com/python-sorted/

def plusTen(x):
    return x + 10
print(plusTen(5))

plusTen2 = lambda x : x + 10
print(plusTen2(5))

list = [(1, 2), (0, 1), (5, 1), (5, 2), (3, 0)]
list.sort(key = lambda x : x[0])
print(list)
list2 = sorted(list, key = lambda x : x[1])
print(list2)