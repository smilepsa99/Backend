# 함수
# def 함수이름() :
#       실행 명령문

def open_account() :
    print("새로운 계좌가 생성되었습니다.")

################################################################################################################

# 전달값과 반환값

def deposit (balance , money) : # 입금
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
    return balance + money

# def withdraw(balance , money) :
#     if balance < money :
#         print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
#         return balance
#     else :
#         print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
#         return balance - money

def withdraw_night(balance , money) :
    if balance < money :
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
        return balance
    else :
        commission = 100
        return commission , balance - money - commission

balance = 0
balance = deposit(balance,1000)
# balance = withdraw(balance,500)
commission , balance = withdraw_night(balance,500)
print("출금이 완료되었습니다. 수수료는 {0} 원이며, 잔액은 {1} 원입니다.".format(commission,balance))

################################################################################################################

# 기본값

def profile(name , age , main_lang) :
    print("이름 : {0} \t 나이 : {1} \t 언어 : {2}" \
          .format(name,age,main_lang))          # \ 를 써서 한 코드를 줄바꿈해서 쓸 수 있음

profile("유재석" , 20 , "파이썬")
profile("김태호" , 25 , "자바")

# 유재석과 김태호가 같은 학년에 같은 언어를 배운다면..

def profile(name , age=17 , main_lang="파이썬") :
    print("이름 : {0} \t 나이 : {1} \t 언어 : {2}" \
          .format(name , age , main_lang))

profile("유재석")
profile("김태호")

################################################################################################################

# 키워드 값

def profile(name , age , main_lang) :
    print("이름 : {0} \t 나이 : {1} \t 언어 : {2}".format(name,age,main_lang))

profile(name="박상아", main_lang="파이썬", age=25)
profile(main_lang="파이썬", age=25, name="박상아")
# => 키워드에 값을 직접 입력할 수 있음

################################################################################################################

# 가변인자

# def profile (name, age, lang1, lang2, lang3, lang4, lang5) :
#     print("이름 : {0} \t 나이 : {1} \t".format(name,age), end=" ")
#     # end=" "를 print() 내용 끝에 넣어주면 아래 print() 내용과 한줄에 출력할 수 있음
#     print(lang1, lang2, lang3, lang4, lang5)

# profile("유재석" , 20 , "Python", "Java", "C", "C++", "C#")
# profile("김태호" , 25 , "Kotlin", "Swift", "", "", "")

def profile (name, age, *language) : # 변수 앞에 *을 붙여서 가변인자를 만들 수 있음
    print("이름 : {0} \t 나이 : {1} \t".format(name,age), end=" ")
    for lang in language :
        print(lang, end=" ")
    print()

profile("유재석" , 20 , "Python", "Java", "C", "C++", "C#", "Javascript")
profile("김태호" , 25 , "Kotlin", "Swift")

################################################################################################################

# 지역변수와 전역변수

gun = 10

def checkpoint(soldiers) :
    global gun # 전역 변수 : 전역 공간에 있는 변수 gun의 값 사용(but 코드관리하기 불편해서 보통 잘 안쓴다고 함)
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_return(gun,soldiers) :
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
# checkpoint(2)
gun = checkpoint_return(gun,2)
print("남은 총 : {0}".format(gun))

################################################################################################################

# 퀴즈

# 답안 1
def std_weight (height, gender) :
    if gender == "남자" :
        return height**2 * 22
    else : 
        return height**2 * 21

height = float(input("키(m)를 입력해주세요 : "))
gender = input("성별 입력해주세요 : ")
weight = std_weight(height,gender)

print("키 {0}cm {1}의 표준 체중은 {2:.2f}kg 입니다.".format(int(height*100), gender, weight))


# 답안 2
def std_weight (height, gender) :
    if gender == "남자" :
        return height**2 * 22
    else : 
        return height**2 * 21

height = int(input("키(cm)를 입력해주세요 : "))
gender = input("성별(남자/여자)를 입력해주세요 : ")
weight = std_weight(height/100,gender)

print("키 {0}cm {1}의 표준 체중은 {2:.2f}kg 입니다.".format(height, gender, weight))
                                  # :.2f → 소수점 둘째자리까지 반올림해서 표시


# 답안 3(선생님 답안)
def std_weight (height, gender) :
    if gender == "남자" :
        return height**2 * 22
    else : 
        return height**2 * 21

# height = 175
# gender = "남자"
# weight = std_weight(height/100,gender)

# print("키 {0}cm {1}의 표준 체중은 {2:.2f}kg 입니다.".format(height, gender, weight))

height = 175
gender = "남자"
weight = round(std_weight(height/100,gender), 2)  # round (숫자, 2) → 소수점 둘째자리까지 반올림해서 표시

print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))