#CONSTRUCTORS
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def move(self):
        print("here i move ")

    def write(self):
        print("okay i do")

point1=Point(10,20)
print(point1.x)