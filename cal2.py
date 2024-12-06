#calculator with argument and without return type
def addition(a,b):
    sum=a+b

    print("sum is = ",sum)


def subtraction(a,b):
    sum=a-b
    print("difference is =",sum)


def multiplication(a,b):
    sum=a*b
    print("product is =",sum)

def division(a,b):
    try:
        sum=a/b
        print("division is =",sum)
    except:
        print("number cannot divided by zero")


a=float(input("enter the 1st number: "))
b=float(input("enter the 2nd number: "))
for i in range(5):
    print("1.addition\n  2.subtraction\n  3.multiplication\n  4.division\n  5.exit\n")
    choice=int(input("enter the choice: "))
    if choice==1:
        addition(a,b)
    elif choice==2:
        subtraction(a,b)
    elif choice==3:
        multiplication(a,b)
    elif choice==4:
        division(a,b)
    elif choice==5:
        print("exit")
        break
    else:
        print("invalied choice")
