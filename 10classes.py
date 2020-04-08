class Point:
    def move(self):
        print("here i move")

    def draw(self):
        print("here i draw")


point1= Point()
point1.x=10
point1.y=20
print(point1.x)
print(point1.y)
point1.draw()
point1.move()

point2=Point()
point2.x=1
print(point2.x)

