value=[]
n=int(input("enter length"))

for i in range(n):
    x=int(input("enter vals"))
    value.append(x)
print(value)
f=int(input("enter for search"))
arr=[]
for j in value:
    arr.append(j)
    if j==f:
        print(len(arr))
        break
        
   


