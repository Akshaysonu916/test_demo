""""
def modify(a):    
    def inner_modification(name):
        result=a(name)
        return result.upper()
    return inner_modification

def bolding(b):
    def inner_modification(name):
        result=b(name)
        return result.capitalize()
    return inner_modification

        


@modify
def full_name(name):
    return "akshay" + name
print(full_name("aneesh"))

@bolding
def full_names(name):
    return "akshay" + name
print(full_names("aneesh"))

"""
class area:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def display(self):
        
        print(self.length*self.width)
A=area(5,10)
B=area(20,30)
C=area(30,20)
A.display()
B.display()
C.display()
print(id(A))