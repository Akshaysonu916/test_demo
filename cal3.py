#calculator without argument and with return type
a=float(input("enter the 1st number: "))
b=float(input("enter the 2nd number: "))
def addition():
    sum=a+b
    return sum

def subtraction():
    difference=a-b
    return difference


def multiplication():
    product=a*b
    return product

def division():
    try:
        division=a/b
        return division
    except:
        print("number cannot divided by zero")



for i in range(5):
    print("1.addition\n  2.subtraction\n  3.multiplication\n  4.division\n  5.exit\n")
    choice=int(input("enter the choice: "))
    if choice==1:
       x= addition()
       print("sum is: ",x)
        
    elif choice==2:
        x=subtraction()
        print("difference is: ",x)
    elif choice==3:
        x=multiplication()
        print("product is : ",x)
    elif choice==4:
        x=division()
        print("division is: ",x)
    elif choice==5:
        print("exit")
        break
    else:
        print("invalied choice")
