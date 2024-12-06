list1=[1,-3,4,-2,-7]
def negative(num):
    if num<0:
        print("negative numbers",num)
    else:
        print("positive numbers",num)
print(list(filter(negative,list1)))
    