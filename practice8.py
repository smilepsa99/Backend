# 함수와 메소드의 차이점
# https://velog.io/@yejin20/Python-%ED%95%A8%EC%88%98%EC%99%80-%EB%A9%94%EC%86%8C%EB%93%9C%EC%9D%98-%EC%B0%A8%EC%9D%B4%EC%A0%90

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