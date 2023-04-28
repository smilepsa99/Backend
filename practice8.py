# class 없이 스타크래프트 만들기 : 유닛을 만들 때마다 변수를 만들어야해서 너무 번거로움

# 마린 : 공격 유닛, 군인. 총을 쏠 수 있음
name = "마린" # 유닛의 이름
hp = 40 # 유닛의 체력
damage = 5 # 유닛의 공격력
print("{0} 유닛이 생성되었습니다.".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# 탱크 : 공격 유닛, 탱크. 포를 쏠 수 있는데, 일반모드 / 시즌모드
tank_name = "탱크"
tank_hp = 150
tank_damage = 35
print("{0} 유닛이 생성되었습니다.".format(tank_name))
print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(name, location, damage))

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)

################################################################################################################

# class를 활용해서 스타크래프트 만들기

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# 레이스 : 공중 유닛, 비행기. 클로킹(상대방에게 보이지 않는 모드)
wraith1  = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것(빼앗음)
wraith2  = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True # 클래스 외부에서 원하는 변수를 새로 만들어 확장할 수 있음(단, 확장된 객체(wraith2)에서만 사용가능)

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

################################################################################################################
# [참고글] 함수와 메소드의 차이점
# https://velog.io/@yejin20/Python-%ED%95%A8%EC%88%98%EC%99%80-%EB%A9%94%EC%86%8C%EB%93%9C%EC%9D%98-%EC%B0%A8%EC%9D%B4%EC%A0%90

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed): # 클래스 안에서 method(함수)를 쓸 땐 항상 self를 써줘야 함
        self.name = name # self.name은 클래스 안에서 정의된 변수, 멤버변수임.
        self.hp = hp
        self.speed = speed
    def move (self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))


# 공격 유닛
class AttackUnit(Unit): # 클래스 AttackUnit은 클래스 Unit 을 상속받겠다는 의미(자식 클래스: AttackUnit / 부모 클래스 : Unit)
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed) # 클래스 Unit의 내용을 가져옴
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp == 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 파이어뱃 : 공격 유닛, 화염방사기 
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

# # 공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)

# 메딕 : 의무병, 다른 유닛 회복 (공격력 X)
# 드랍쉽 : 공중 유닛, 수송기, 다른 유닛 이동시켜줌 (공격력 X)

# 날 수 있는 기능을 가지는 클래스
class Flyable:
    def __init__(self, flyingspeed):
        self.flyingspeed = flyingspeed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flyingspeed))

# 공중 공격유닛
class FlyableAttack(AttackUnit, Flyable): # 클래스 AttackUnit 과 클래스 Flyable 을 상속받음(다중상속)
    def __init__(self, name, hp, damage, flyingspeed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 스피드는 0
        Flyable.__init__(self, flyingspeed)

    def move(self, location): # 메소드 오버로딩 : 클래스 Unit의 move() 함수를 재정의함
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# # 발키리 : 공중 공격유닛, 한번에 14발 미사일 발사
valkyrie = FlyableAttack("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")

# # 벌쳐 : 지상 유닛, 기동성이 좋음
vulture = AttackUnit("벌쳐", 80, 10, 20)

# # 배틀크루저 : 공중유닛, 체력도 공격력도 굉장히 좋음
battlecruiser = FlyableAttack("배틀크루저", 500, 25, 3)

vulture.move("11시")
# battlecruiser.fly(battlecruiser.name, "9시")
battlecruiser.move("9시")


# 건물
# 서플라이 디폿 : 건물, 1개 당 8 유닛 생성

class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass # 코드가 완성되지 않았어도 일단 넘어가라

supply_depot = BuildingUnit("서플라이 디폿", 500, "7시") # 출력 X

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass

game_start() # 출력됨
game_over() # 출력 X

class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        #Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0) # super를 써서 부모 클래스를 부를 수 있음(단, 다중상속일 땐 불가(아래 참고))
        self.location = location

################################################################################################################
# super

# 클래스명.__init__(self)  →  super().__init__()  로 쓸 수 있음
# 단, 두개 이상의 부모클래스를 모두 초기화(__init__)할 때는 부모 클래스 이름을 따로 다 명시해야 함

class happy:
    def __init__(self):
        print("행복해요")
class sad:
    def __init__(self):
        print("슬퍼요")

# class emotion(happy, sad):
#     def __init__(self):
#         super().__init__()

# me = emotion() # "행복해요" 만 출력됨

# class emotion(sad, happy):
#     def __init__(self):
#         super().__init__()

# me = emotion() # "슬퍼요" 만 출력됨

class emotion(happy, sad):
    def __init__(self):
        happy.__init__(self)
        sad.__init__(self)

me = emotion() # "행복해요" / "슬퍼요" 모두 출력됨
################################################################################################################

# 퀴즈
# 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.

# (출력 예제)
# 총 3대의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

# [코드]
class House:
    # 매물 초기화 : 위치, 건물 종류, 매물 종류, 가격, 준공년도
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    # 매물 정보 표시
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

a = House("강남", "아파트", "매매", "10억", "2010년")
b = House("마포", "오피스텔", "전세", "5억", "2007년")
c = House("송파", "빌라", "월세", "500/50", "2000년")
house_list = [a, b, c]

print("총 {}대의 매물이 있습니다.".format(len(house_list)))

# a.show_detail()
# b.show_detail()
# c.show_detail()
# ↳ 선생님 아이디어
for i in house_list:
    i.show_detail()


# 기능 추가한 답안
class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

house_list = []

while True:
    lo = input("매물의 위치를 입력하세요 : ")
    ht = input("매물의 건물종류를 입력하세요 : ")
    dt = input("매물의 종류를 입력하세요 : ")
    pr = input("매물의 가격을 입력하세요 : ")
    cy = input("매물의 준공년도를 입력하세요 : ")

    x = House(lo, ht, dt, pr, cy)
    house_list.append(x)
    print("\n매물이 정상적으로 등록되었습니다.\n")
    print("총 {}대의 매물이 있습니다.".format(len(house_list)))
    print("----------------------------------------------------")
    for i in house_list:
        print("({})".format(house_list.index(i)+1), end=" ")
        i.show_detail()
    print("----------------------------------------------------")
    
    while True:
        answer = input("\n매물을 계속 추가하시겠습니까? (네/아니오) : ")
        if answer == "네" or answer == "아니오": 
            break
        else:
            print("네 또는 아니오로 입력해주세요")

    if answer == "네":
        continue
    elif answer == "아니오":
        print("\n프로그램을 종료합니다.")
        break