#calculator without argument and without return type
def addition(): 
    print("sum is =",a+b)


def subtraction():
    print("difference is =",a-b)


def multiplication():
    print("product is =",a*b)

def division():
     try:
            print("division is =",a/b)
     except:
            print("number cannot divided by zero")


a=float(input("enter the 1st number: "))
b=float(input("enter the 2nd number: "))
for i in range(5):
    print("1.addition\n  2.subtraction\n  3.multiplication\n  4.division\n  5.exit\n")
    choice=int(input("enter the choice: "))
    if choice==1:
        addition()
    elif choice==2:
        subtraction()
    elif choice==3:
        multiplication()
    elif choice==4:
        division()
    elif choice==5:
        print("exit")
        break
    else:
        print("invalied choice")
