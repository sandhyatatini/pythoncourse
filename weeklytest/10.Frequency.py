n=input()
res={}
for i in n:
    if i not in res and i!=" ":
        res[i]=n.count(i)
print(res)