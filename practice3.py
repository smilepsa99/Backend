# 문자열
sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)


# 슬라이싱 : 자료에서 필요한 만큼을 잘라서 사용하는 것
jumin = "990709-2345678"

x = int(jumin[7])
if x == 2 :
    x = "여자"
else:
    x = "남자"    
print("성별 : " + x)

print("성별 : " + jumin[7]) # 2
print("연 : " + jumin[0:2]) # 99 / index(순서)는 0부터 시작, 0:2는 0번째 이상 2번째 미만을 말함
print("월 : " + jumin[2:4]) # 07
print("일 : " + jumin[4:6]) # 09

print("생년월일 : " + jumin[:6]) # 처음부터 6번째 미만(처음 번째(0) 생략가능)
print("뒤 7자리 : " + jumin[7:]) # 7번째부터 끝까지(끝 번째(14) 생략가능)
print("뒤 7자리 (뒤에부터) : " + jumin[-7:]) # 맨 뒤에서 7번째부터 끝까지(맨 뒤부터 -1번째로 셈)