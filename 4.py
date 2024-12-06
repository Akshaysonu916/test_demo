str="Hello World From Python"[::-1]
print(str)
st=""
for char in str:
    if char not in st:
        st=st+char
print(st)
r={c:str.count(c) for c in str}
print(r)