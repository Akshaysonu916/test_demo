class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_info(self):
        print(f"name:{self.name}\nage:{self.age}")
        
p1=Person("Akshay",19)
p1.display_info()