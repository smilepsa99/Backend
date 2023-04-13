# 자료형 - 숫자
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(3*(3+1))


# 자료형 - 문자열
print('풍선')
print('나비')
print('ㅋㅋㅋㅋㅋㅋㅋㅋㅋ')
print('ㅋ'*9)


# 자료형 - boolean(참/거짓)
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True) # not 은 not 다음에 오는 값의 반대를 말함
print(not False)
print(not (5 > 10))


# 애완동물을 소개해주세요!
animal = '강아지'
name = '연탄이'
age = 4
hobby = '산책'
is_adult = age >= 3

print('우리집 ' + animal + '의 이름은 ' + name + '예요')
print(name + '는 ' + str(age) + '살이며, ' + hobby + '을 아주 좋아해요')
print(name + '는 어른일까요? ' + str(is_adult))


# [퀴즈] 변수를 이용하여 다음 문장을 출력하시오.
# 변수명 : station
# 변숫값 : "사당", "신도림", "인천공항" 순서대로 입력
# 출력문장 : XX 행 열차가 들어오고 있습니다.

station = '사당'
print(station + '행 열차가 들어오고 있습니다.')
station = '신도림'
print(station + '행 열차가 들어오고 있습니다.')
station = '인천공항'
print(station + '행 열차가 들어오고 있습니다.')
