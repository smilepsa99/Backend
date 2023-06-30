# import random
# import time

# menu = ["너구리 해물라면", "한식", "배달음식", "기타"]

# answer = input("메뉴를 뽑기를 실행하시겠습니까?(o/x) : ")
# if answer == "o":
#     print("\n===================")
#     for food in menu:
#         print(food)
#     print("===================")
#     print("\n다음의 메뉴 후보 중에서 랜덤 선정하겠습니다.")
#     time.sleep(1)

#     print("\n메뉴 뽑는 중")
#     time.sleep(1)
#     for i in range(3):
#         print(".")
#         time.sleep(1)

#     food_index = random.randrange(len(menu))
#     print("\n오늘의 메뉴는 {0}(으)로 선정되었습니다.".format(menu[food_index]))
# else:
#     print("메뉴 뽑기를 종료합니다.")

##################################################################################
import random
import time

class Menu:
    def __init__(self):
        self.menu = []

    def read(self):
        return self.menu
    
    def add(self, food):
        self.menu.append(food)

    def select(self):
        self.index = random.randrange(len(self.menu))
        return self.menu[self.index]

menu = Menu()
while True:
    add_food = input("메뉴 후보를 추가해주세요 : ")
    menu.add(add_food)
    while True:
        a1 = input("\n계속 추가하시겠습니까?(예/아니오) : ")
        if a1 == "예":
            break
        elif a1 == "아니오":
            print("\n최종 메뉴 후보 리스트입니다.")
            print("===================")
            for food in menu.read():
                print(food)
            print("===================")
            break
        else:
            print("'예' 또는 '아니오'를 입력해주세요")
    if a1 == "아니오":
        break
    else:
        continue

while True:
    a2 = input("\n메뉴를 뽑기를 실행하시겠습니까?(예/아니오) : ")
    if a2 == "예":
        print("\n메뉴 뽑는 중")
        time.sleep(1)
        for i in range(3):
            print(".")
            time.sleep(1)
        print("\n오늘의 메뉴는 {0}(으)로 선정되었습니다.".format(menu.select()))
        break
    elif a2 == "아니오":
        print("\n프로그램을 종료합니다.")
        break
    else:
        print("'예' 또는 '아니오'를 입력해주세요")
