# 표준 입출력

print("상아", "미오") # 상아 미오 (,는 띄어쓰기o)
print("상아" + "미오") # 상아미오 (+는 띄어쓰기x)

print("상아", "미오", sep=",") # 상아,미오
print("상아", "미오", "나", sep=" vs ") # 상아 vs 미오 vs 나


print("상아", "미오", sep=", ") # 상아, 미오?
print("무엇이 다를까요?") # 무엇이 다를까요?
print("상아", "미오", sep=", ", end="? ")
print("무엇이 다를까요?") # 상아, 미오? 무엇이 다를까요?

import sys # sys 모듈을 가져와라
print("상아", "미오", file=sys.stdout) # 표준출력
print("상아", "미오", file=sys.stderr) # 표준에러
# [참고] https://nadocoding.tistory.com/54

scores = {"국어":0, "영어":50, "수학":100}
for subject, score in scores.items() :
    print(subject, score)
scores = {"국어":0, "영어":50, "수학":100}
for subject, score in scores.items() :
    print(subject.ljust(8), str(score).rjust(4), sep=":")

for i in range(1,21) :
    print("대기번호 : " + str(i))
for i in range(1,21) :
    print("대기번호 : " + str(i).zfill(3))

answer = input("아무거나 입력하세요 : ")
print("당신이 입력한 것은 " +  answer + "입니다.")
print(type(answer)) # <class 'str'>
                    # input을 사용하면, 사용자가 입력한 값은 문자열(str) 형태로 받아짐

################################################################################################################

# 다양한 출력포맷
# {인덱스:[[빈자리채우기]정렬][기호][확보공간][콤마][.자릿수][타입]}

print("{0}".format(500))

# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))
# 양수일 떈 + 로 표시, 음수일 땐 - 표시 추가
print("{0: >+10}".format(500))
# 왼쪽 정렬하고, 빈칸을 _로 채움
print("{0:_<10}".format(500))


print("{0}".format(100000000000))

# 3자리 마다 콤마 찍어주기
print("{0:,}".format(100000000000))
# 3자리 마다 콤마 찍어주기, +/- 부호도 추가
print("{0:+,}".format(100000000000))
# 빈자리는 ^로, 좌측정렬, +/- 부호 붙이기, 30칸의 자릿수 확보, 3자리 마다 콤마 찍어주기
print("{0:^<+30,}".format(100000000000))


# 소수점 출력
print("{0:f}".format(5/3)) # 1.666667
# 소수점 특정 자리수까지만 표시
print("{0:.2f}".format(5/3)) # 1.67(반올림해서 소수점 2째자리까지 표시)

################################################################################################################

# 파일 입출력
# 1. 파일 열기 / 2. 파일에 쓰거나 읽기 / 3. 파일 닫기
# open("파일명", "열기모드", encoding="인코딩")
# 열기모드 종류 : w(write,쓰기) a(append,이어쓰기) r(read,읽기)

score_file = open("score.txt", "w", encoding="utf8")
print("국어 : 0", file=score_file)
print("수학 : 100", file=score_file)
score_file.close()
# 파일을 열고 볼일 끝나면 꼭 닫기(안그러면 다른 위치에서 동일한 파일에 접근하려고 할 때 파일에 따라 문제가 발생할 수 있음)

score_file = open("score.txt", "a", encoding="utf8")
score_file.write("영어 : 50")
score_file.write("\n과학 : 75")
score_file.close()


score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="") # readline() : 줄별로 읽기, 한줄 읽고나면 커서 다음줄로 감
                                     # end="" : 줄바꿈 방지를 위해서 작성
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()

# 파일 내용이 몇줄인지 모를 때 읽는 방법
score_file = open("score.txt", "r", encoding="utf8")
while True :
    text = score_file.readline()
    if not text : # 더이상 읽어올 내용이 없으면..
        break # 반복문 탈출
    print(text, end="")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # 모든 줄을 읽어와서 list 형태로 저장
for line in lines :
    print(line, end="")
score_file.close()

################################################################################################################

# pickle : 프로그램에서 사용하고 있는 데이터를 파일형태로 저장하거나 불러올 수 있게 해주는 모듈
# pickle.dump(data, dest_file) : data 를 dest_file 에 저장하기
# pickle.load(src.file) : src.file 에서 데이터 불러오기

import pickle

profile_file = open("profile.pickle", "wb") # 바이너리(binary) 형태로 저장, encoding 작성 필요없음
profile = {"이름":"빅상아", "나이":25, "취미":["그림", "음악", "코딩"]}
# print(profile)
pickle.dump(profile, profile_file) # profile 데이터를 profile_file 에 저장
profile_file.close()

profile_file = open("profile.pickle", "rb") # 바이너리(binary) 형태로 읽음
profile = pickle.load(profile_file) # profile_file 에서 데이터를 불러와서 profile에 저장
print(profile)
profile_file.close()

# with 구문 : 파일을 읽고쓰는 코드를 간결하게 해주며, close() 함수 호출 안해도 됨
# with 작업 as 변수명 :
#   실행 명령문

import pickle

with open("profile.pickle", "rb") as profile_file :
    profile = pickle.load(profile_file)
    print(profile)

with open("study.txt", "w", encoding="utf8") as study_file :
    study_file.write("파이썬을 공부하고 있습니다.")

with open("study.txt", "r", encoding="utf8") as study_file :
    print(study_file.read())

################################################################################################################

# 퀴즈
# 당신의 회사에서는 매주 1회 작성해야하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

# - X 주차 주간보고 -
# 부서 : 
# 이름 : 
# 업무 요약 : 

# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

# 조건 : 파일명은 '1주차.txt', '2주차.txt', ... 와 같이 만듭니다.

# 답안
for num in range(1,51) :
    report_file = open(str(num) + "주차.txt", "w", encoding = "utf8")
    report_file.write("- " + str(num) +"주차 주간보고 -")
    report_file.write("\n부서 : ")
    report_file.write("\n이름 : ")
    report_file.write("\n업무 요약 : ")
    report_file.close()

# 답안2 (pickle 활용해서)
for num in range(1,51) :
    with open(str(num) + "주차.txt", "w", encoding = "utf8") as report_file :
        report_file.write("- " + str(num) +"주차 주간보고 -")
        report_file.write("\n부서 : ")
        report_file.write("\n이름 : ")
        report_file.write("\n업무 요약 : ")

# 답안3 (pickle, .format() 활용해서)
for num in range(1,51) :
    with open("{0}주차.txt".format(num), "w", encoding = "utf8") as report_file :
        report_file.write("- {0} 주차 주간보고 -".format(num))
        report_file.write("\n부서 : ")
        report_file.write("\n이름 : ")
        report_file.write("\n업무 요약 : ")