# class Quadrangle:
#     def __init__(self, width, height, color):
#         self.width = width
#         self.height = height
#         self.color = color
#         if width == height:
#             print("길이 {0}, {1} 색의 정사각형이 생성되었습니다.".format(self.width, self.color))
#         else:
#             print("가로 {0}, 세로 {1}, {2} 색의 직사각형이 생성되었습니다.".format(self.width, self.height, self.color))

# class Quadrangle:
#     def __init__(self, width, height, color):
#         self.width = width
#         self.height = height
#         self.color = color
    
#     def get_area(self):
#         area = self.width * self.height
#         return area

# square1 = Quadrangle(10, 5, "red")
# square2 = Quadrangle(7, 7, "blue")

# area1 = square1.get_area()
# area2 = square2.get_area()

# print(area1)
# print(area2)

class Quadrangle:
    width = 0
    height = 0
    color = "black"

    def set_area(self,width,height,color):
        self.width = width
        self.height = height
        self.color = color

    def get_area(self):
        return self.width * self.height, self.color

square1 = Quadrangle()
square2 = Quadrangle()

square1.set_area(10, 5, "red")
square2.set_area(7, 7, "blue")

print(square1.get_area())
print(square2.get_area())



# square1.width = 10
# square1.height = 5
# square1.color = "red"

# square2.width = 7
# square2.height = 7
# square2.color = "blue"

# print(square1.width, square1.height, square1.color)
# print(square2.width, square2.height, square2.color)


# - 직사각형 1개 객체 속성: width=10, height=5, color='red'
# - 정사각형 1개 객체 속성: width=7, height=7, color='blue'