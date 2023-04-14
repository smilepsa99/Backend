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


# 문자열 처리함수
sen = "Python is Amazing"
print(sen.lower()) # python is amazing (소문자로 변경)
print(sen.upper()) # PYTHON IS AMAZING (대문자로 변경)
print(sen[0].isupper()) # True (0번째 문자가 대문자인지 판별)

print(sen.replace("Python","Java")) # .replace("a","b") : a를 b로 문자 변경

print(len(sen)) # 문자 총 개수(띄어쓰기 포함)
count = sen.count("n") # .count("n") : n이 몇 개 있는지
print(count) # 2

index = sen.index("n") # .index("n") : n이 몇번째에 있는지
print(index) # 5

index = sen.index("n",index + 1) # .index("n",5 + 1) : 6번째 문자부터 그 이후에 나온 n이 몇번째에 있는지
print(index) # 15

print(sen.find("Java")) # -1 : "Java"가 없어도 사용 가능
# print(sen.index("Java")) # error : "Java"가 없으면 사용 불가능


# 문자열 포맷

# 기본 방법
print("a" + "b") # ab
print("a" , "b") # a b

# 방법 1 : %
print("나는 %d살입니다" %20) # %d → 정수
print("나는 %s을 좋아해요" %"Python") # %s → 문자열
print("Apple은 %c로 시작해요" %"A") # %c → 문자 한개
# %s는 정수, 문자 한개 또한 모두 가능
print("나는 %s살입니다." %20)
print("Apple은 %s로 시작해요" %"A")
# ()를 활용해서 값을 두 개 이상 쓸 수 있음
print("나는 %s색과 %s색을 좋아해요" %("파란","빨간"))

# 방법 2 : {} 와 .format()
print("나는 {}살입니다".format(20))
print("나는 {}색과 {}색을 좋아해요".format("파란","빨간"))
print("나는 {1}색과 {0}색을 좋아해요".format("파란","빨간")) # {} 안에 index(위치값)을 써서 값을 넣는 순서를 바꿀 수 있음

# 방법 3 : {변수} 와 .format(변수=값)
print("나는 {age}살이며, {color}색을 좋아해요".format(age = 20, color = "빨간"))
print("나는 {age}살이며, {color}색을 좋아해요".format(color = "빨간", age = 20)) # format() 안의 순서와 상관없이, 지정한 변수의 값이 넣어짐

# 방법 4(버전 3.6부터 가능) : f"~{변수}~"
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요")


# 탈출 문자

# \n : 줄바꿈
print("백문이 불여일견\n백견이 불여일타")

# \" \' : 문장 내에서 따옴표 표기
# 저는 "나도코딩"입니다. → 이 문장을 출력하려면?
print('저는 "나도코딩"입니다.') # 탈출문자 없이
print("저는 \"나도코딩\"입니다.") # \" 활용
print("저는 \'나도코딩\'입니다.") # \' 활용

# \\ : 문장 내에서 \ 표기
# print("C:\Users\smile\Desktop\개발 공부") # \ 하나만 있으면 오류 발생
print("C:\\Users\\smile\\Desktop\\개발 공부")

# \r : 커서를 맨 앞으로 이동(해서 덮어쓰기)
print("Red Apple\rPine") # PineApple

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple") # RedApple

# \t : 탭
print("Red\tApple") # Red   Apple


# [퀴즈] 사이트별로 비밀번호를 만들어주는 프로그램을 작성하시오

# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성
#                  (nav)             (5)              (1)        (!)
# 예) 생성된 비밀번호 : nav51!


# 나의 답
link = input("사이트의 주소를 입력하세요 : ")

x = link.index("//") + 2
y = link.index(".")

name = link[x:y]
psw = name[:3] + str(len(name)) + str(name.count("e")) + "!"
print("{0} 의 비밀번호는 {1} 입니다.".format(link , psw))


# 선생님 답
url = "http://naver.com"
my_str = url.replace("http://","") # 규칙 1
my_str = my_str[:my_str.index(".")] # 규칙 2
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0} 의 비밀번호는 {1} 입니다.".format(url , password))