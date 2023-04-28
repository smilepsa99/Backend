# 예외 처리 : 에러에 대해서 처리하는 것
# (에러 발생 시 코드가 그냥 강제종료되지 않게 막아서, 프로그램의 완성도를 높이는 용도로 쓰임)

try:    
    print("나누기 전용 계산기입니다.")
    num1 =  int(input("첫 번째 숫자를 입력하세요 : "))
    num2 =  int(input("두 번째 숫자를 입력하세요 : "))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError: # [예외처리] 에러명에 따라 아래코드 실행
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err: # [예외처리] 에러명에 따른 err 메세지를 받아오고, 아래코드 실행
    print(err)
except: # [예외처리] 위의 경우 외에 모든 에러에 대해서 아래코드 실행
    print("알 수 없는 에러가 발생하였습니다.")

try:    
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    # nums.append(int(nums[0] / nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except Exception as err: # [예외처리] (위의 경우 외에) 모든 에러에 대해서 err 메시지를 받아오고, 아래코드 실행
    print("알 수 없는 에러가 발생하였습니다.")
    print(err)

################################################################################################################

# 에러 발생시키기

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("첫 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise ValueError # raise 에러명 : 해당 에러 발생
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")


################################################################################################################

# 사용자 정의 예외처리 : err 이름과 메세지를 직접 정하기

class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg
    # [참고글] __init__, __str__ 메서드
    # https://velog.io/@tbnsok40/%ED%8C%8C%EC%9D%B4%EC%8D%AC-str-init-%EB%A9%94%EC%84%9C%EB%93%9C

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
    print(err) # 입력값 : (첫번째숫자), (두번째숫자) -> 59번줄에서 직접 정한 err 메세지 출력

# finally (에러 발생여부와 상관없이 무조건 실행됨)
finally:
    print("계산기를 이용해주셔서 감사합니다.")

################################################################################################################

# 퀴즈

# 대기 손님의 치킨 요리 시간을 줄이고자 자동 주문 시스템을 제작하였습니다.
# 시스템 코드를 확인하고 적절한 예외처리 구문을 넣으시오.

# 조건1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError 로 처리
#         출력 메세지 : "잘못된 값을 입력하였습니다."
# 조건2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
#         치킨 소진 시 사용자 정의 에러[SoldOutError]를 발생시키고 프로그램 종료
#         출력 메세지 : "재고가 소진되어 더 이상 주문을 받지 않습니다."

# 내 답안
chicken = 10 # 남은 치킨 수
waiting = 1 # 홀 안에는 현재 만석. 대기번호 1부터 시작

class SoldOutError(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg

try:
    while(True):
        print("[남은 치킨 : {0}]".format(chicken))
        if chicken == 0:
            raise SoldOutError("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        else:
            order = int(input("치킨 몇 마리 주문하시겠습니까? "))
            if order <= 0:
                raise ValueError
            else:
                if order > chicken: # 남은 치킨보다 주문량이 많을 때
                    print("재료가 부족합니다.")            
                else:
                    print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다.".format(waiting, order))
                    waiting += 1 # 대기번호 증가
                    chicken -= order # 주문 수 만큼 남은 치킨 감소
except ValueError:
    print("잘못된 값을 입력하였습니다.")
except SoldOutError as err:
    print(err)


# 선생님 답안
chicken = 10 # 남은 치킨 수
waiting = 1 # 홀 안에는 현재 만석. 대기번호 1부터 시작

class SoldOutError(Exception):
    pass


while(True):
    try:
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까? "))
        if order > chicken: # 남은 치킨보다 주문량이 많을 때
            print("재료가 부족합니다.")
        elif order <= 0:
            raise ValueError            
        else:
            print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다.".format(waiting, order))
            waiting += 1 # 대기번호 증가
            chicken -= order # 주문 수 만큼 남은 치킨 감소
        
        if chicken == 0:
            raise SoldOutError()
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except SoldOutError:
        print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        break