#CONSTURCTOR TASK
class Person:
    def __init__(self,name):
        self.name = name


    def talk(self):
        print(f"Hi, i'am {self.name}")


one = Person("Amrit Thapa")
bob = Person("Bob smith")
one.talk()
bob.talk()


