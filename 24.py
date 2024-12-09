class Flyable:
    def fly(self):
        print("I can fly")
class Swimmable:
        def swim(self):
             print("I can swim")
class Duck(Flyable,Swimmable):
        pass
duck=Duck()
duck.fly()
duck.swim()