# 조건문 if

# if 조건 :
#     실행 명령문

weather = input("오늘 날씨는 어때요? ") # weather 라는 변수에, 사용자로부터 받은 입력값을 넣어라

if weather == "비" or weather == "눈":
    print("우산을 챙기세요") # 입력값이 비 or 눈 이면, 우산을 챙기세요 출력
elif weather == "미세먼지":
    print("마스크를 챙기세요") # 입력값이 미세먼지 이면, 마스크를 챙기세요 출력
else:
    print("준비물 필요 없어요") # 입력값이 그 외(맑아요) 이면, 준비물 필요 없어요 출력


temp = int(input("기온은 어때요? ")) # temp 라는 변수에, 사용자로부터 받은 입력값을 정수(int)로 변환해서 넣어라
if 30 <= temp:
    print("너무 더워요. 나가지 마세요") # 입력값이 30 이상일때 출력
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨에요") # 입력값이 10 이상 30미만 일때 출력
elif 0 <= temp <10:
    print("외투를 챙기세요")  # 입력값이 0 이상 10미만 일때 출력
else:
    print("너무 추워요. 나가지 마세요") # 입력값이 0미만 일때 출력

################################################################################################################

# 반복문 for

print("대기번호 : 1")
print("대기번호 : 2")
print("대기번호 : 3")
print("대기번호 : 4")

for waiting_no in [0,1,2,3,4]: # waiting_no 라는 변수에 0을 넣고 아래 코드를 실행하고, 1을 넣고 실행, ... 4를 넣고 실행
    print("대기번호 : {0}".format(waiting_no)) # 대기번호 : 0 / 대기번호 : 1 / ... / 대기번호 : 4

for waiting_no in range(5): # waiting_no 라는 변수에 0부터 5미만의 정수(0,1,2,3,4)를 넣으며 아래 코드 반복실행
    print("대기번호 : {0}".format(waiting_no)) # 대기번호 : 0 / 대기번호 : 1 / ... / 대기번호 : 4

for waiting_no in range(1,6): # waiting_no 라는 변수에 1부터 6미만의 정수(1,2,3,4,5)를 넣으며 아래 코드 반복실행
    print("대기번호 : {0}".format(waiting_no)) # 대기번호 : 1 / 대기번호 : 2 / ... / 대기번호 : 5


starbucks = ["아이언맨", "토르", "그루트"] # starbucks라는 변수에 다믐과 같은 리스트를 넣음
for customer in starbucks: # starbucks의 요소들을 하나씩 customer라는 변수에 넣으며 아래 코드 반복실행
    print("{0}, 커피가 준비되었습니다.".format(customer)) # 아이언맨, 커피가~ / 토르, 커피가~ / 그루트, 커피가~

################################################################################################################

# 반복문 while : 어떤 조건을 만족할 떄까지 반복하라

customer = "토르"
index = 5

while index >= 1: # 변수 index 가 1 이상 일때까지 아래 코드 반복실행 
    print("{0}, 커피가 준비되었습니다. {1} 번 남았어요.".format(customer,index)) # 토르, ~5번~ / ... / 토르, ~1번~  
    index -= 1 # 변수 index의 값에 1을 빼서 다시 변수 index에 넣음 (index = 5 → 4 → 3 ...)
    if index == 0:
        print("커피가 폐기처분되었습니다.") # 변수 index = 0 이 됐을 때, 출력 후 종료
# (추가) for문으로 만들기
for index in reversed(range(6)) : # index라는 변수에 0부터 6미만의 역순대로(5,4,3,2,1,0) 숫자를 넣으며 아래 코드 반복실행
    if index == 0: # index 가 0이 아닐 때: 실행 X, 66번줄 코드로 / index가 0일 때 : 아래코드 실행
        print("커피가 폐기처분되었습니다.") 
        break # 반복문 종료
    print("{0}, 커피가 준비되었습니다. {1} 번 남았어요.".format("토르",index)) 
    # (0이 아닌) 변수 index마다, "토르, 커피가 준비되었습니다. index 번 남았어요. 출력


# customer = "아이언맨"
# index = 1
# while True: # 무한루프
#      print("{0}, 커피가 준비되었습니다. 호출 {1} 회".format(customer,index)) 
#      index += 1 # 실행될 때마다 변수 index의 값을 1씩 더함 (index = 1 → 2 → 3 ...)
#      # 아이언맨, 커피가 ~. 호출 1회 / 아이언맨, 커피가 ~. 호출 2회 / ...(무한)
#      # 무한루프 중지하는 법 : Ctrl + c (터미널 화면에서) 

customer = "토르"
person = "Unknown" # for문과 달리, while문에서 쓸 변수는 미리 선언해야함

while person != customer: # 변수 person의 값이 변수 customer의 값과 일치하지 않으면 계속 실행해라(일치하면 종료)
      print("{0}, 커피가 준비되었습니다.".format(customer)) # 토르, 커피가 준비되었습니다.
      person = input("이름이 어떻게 되세요? ") # person 이라는 변수에 사용자로부터 받은 입력값을 넣음

################################################################################################################

# continue 와 break

absent = [2,5] # 결석
no_book = [7] # 책을 깜빡했음

for student in range(1,11): # student 라는 변수에 1부터 11미만의 정수(1~10)를 넣으며 아래 코드 반복실행
    if student in absent: # 변수 student의 값이 변수 absent의 요소에 해당되면...
        continue # 아래 코드 건너뛰고 다음 순번의 loop 수행
    elif student in no_book: # 변수 student의 값이 변수 no_book의 요소에 해당되면...
         print("오늘 수업 여기까지. {0}는 교무실로 따라와.".format(student)) # 오늘 수업 여기까지. 7는 교무실로 따라와.
         break # 반복문 중료 (이후 loop 밖으로 나가 다음 코드 실행)
    print("{0}, 책을 읽어봐".format(student)) # if와 elif의 조건과 무관한 student의 값일 때 실행

################################################################################################################

# 한 줄 for문 : [결과 for 반복문], 간단한 리스트 만들 떄 활용(?)

# 출석번호가 1,2,3,4 앞에 100을 붙이기로 함 -> 101,102,103,104
students = [1,2,3,4,5]
students = [i+100 for i in students] # 변수 i에 100을 더한 것을 리스트에 넣어라, i는 변수 students의 요소들을 반복해 넣으면서.
print(students) # [101,102,103,104,105]

# 학생 이름을 문자길이로 변환
students = ["Iron man", "Thor", "I am groot"] 
students = [len(i) for i in students] # 변수 i의 문자길이 값을 리스트에 넣어라, i는 변수 students의 요소들을 반복해 넣으면서.
print(students) # [8, 4, 10]

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]  # 대문자로 변환한 변수 i를 리스트에 넣어라, i는 변수 students의 요소들을 반복해 넣으면서.
print(students) # ['IRON MAN', 'THOR', 'I AM GROOT']

################################################################################################################

# [퀴즈] 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조선1 : 승객별 운행 소요시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건2 : 당신은 소요시간 5분  ~ 15분 사이의 승객만 매칭해야 합니다.

# (출력문 예제)
# [O] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [O] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)

# 총 탑승 승객 : 2 명

import random # random 모듈 가져오기
# [참고글] from random import * 와 import random 차이점
# https://www.inflearn.com/questions/26706/from-random-import-%EC%99%80-import-random-%EC%B0%A8%EC%9D%B4%EC%A0%90
count = 0

for customer in range(1,51) : # customer 라는 변수에 1부터 51미만의 정수를 넣으며 아래 코드 반복실행
    time = random.randrange(5,51) # time 라는 변수에 5 이상 51 미만의 임의의 값을 생성해 넣음
    if 5 <= time <= 15 : # time의 값이 5 이상 15 이하일 경우 아래코드 실행
        check = "O" # check라는 변수에 "O"를 넣음
        count += 1 # 변수 count의 값에 1을 더해서 다시 변수 count에 넣음
    else : # time의 값이 5 이상 15 이하가 아닐 경우 아래코드 실행
        check = " " # check라는 변수에 " "를 넣음
    print("[" + check + "] " + str(customer) + "번째 손님 (소요시간 : " + str(time) + "분)")
    # print("[{0}] {1}번째 손님 (소요시간 : {2}분)".format(check,customer,time)) 
    # → 2개 이상의 변수를 문자열이랑 같이 출력할 땐 .format() 쓰는 게 가독성이 더 좋아보임 

print("\n총 탑승 승객 :", count, "명") # \n : 줄바꿈


# (추가) while문으로 만들기
import random # random 모듈 가져오기

customer = 1
count = 0

while customer <= 50 : # 변수 customer의 값이 50 이하일 때까지 아래코드 반복실행(customer = 51일때, 반복문 종료)
    time = random.randrange(5,51)
    if 5 <= time <= 15 :
        check = "O"
        count += 1 
    else :
        check = " "
    print("[{0}] {1}번째 손님 (소요시간 : {2}분)".format(check,customer,time))
    customer += 1 # 변수 customer의 값에 1을 더해서 다시 변수 customer에 넣음 (customer = 1 → 2 → 3 ...)

print("\n총 탑승 승객 :", count, "명")

# [참고글] "[Python] for과 while문의 차이" https://poew.tistory.com/m/739
