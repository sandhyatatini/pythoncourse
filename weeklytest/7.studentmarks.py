n=int(input())
data={}
max_val=0
res=''
for i in range(n): 
    name,mark=input().split()
    mark=int(mark)
    if mark>max_val:
       res=name
    data[name]=mark
print(data)
print(res)