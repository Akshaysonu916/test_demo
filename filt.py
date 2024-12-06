from functools import reduce # type: ignore
def addition(x,y):
    return x+y
print(reduce(addition,[1,2,3,4]))