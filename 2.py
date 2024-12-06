st={1,2,3,4,5,6}
print(st)
lst=list(st)
lst.remove(5)
lst.insert(4,1)
st=set(lst)
print("after update the element",st)
