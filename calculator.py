a=int(input("enter 1st number: "))
b=int(input("enter 2nd number: "))
for i in range(5):
    print("menu\n 1.addition\n 2.subtraction\n 3.multiplication\n 4.divition\n 5.exit\n")
    choice=int(input("enter the choice: "))
    if choice==1:
        sum=a+b
        print("sum is",sum)
    elif choice==2:
        diff=a-b
        print("difference is",diff)
    elif choice==3:
        product=a*b
        print("the product is",product)
    elif choice==4:
        if b!=0:
            division=a/b
            print("the divition is",division)
        else:
            print("cannot divisible")
    elif choice==5:
        exit()
    else:
        print("invalied choice")