kg=float(input("enter the weight: "))
h=float(input("enter the height: "))
def bmi(weight,height):
    bmi=(kg)/(h/100)**2
    return bmi
b=(bmi(kg,h))
print("bmi is",b)
