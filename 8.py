name=input("enter the username: ")
x=name.isalnum()
y=len(name)
if x==True or 6<=y<=15:
    print("user is valied")