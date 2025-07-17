n=int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        if j==0:
            print("*",end=" ")
        elif i==0 and j<n-1:
            print("*",end=" ")
        elif i==n//2 and j<n-1:
            print("*",end=" ")
        elif i>0 and j==n-1 and i<n//2:
            print("*",end=" ")
        else:
            print(' ',end=" ")
    print()
for i in range(n):
    for j in range(n):
        if (i==0 or i==n-1) and (j!=0 and j!=n-1):
            print("*",end=" ")
        elif (j==0 or j==n-1) and (i!=0 and i!=n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(n):
    for j in range(n):
        if (i==0 or i==n-1) and (j!=0 and j!=n-1):
            print("*",end=" ")
        elif (j==0 or j==n-1) and (i!=0 and i!=n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(n):
    for j in range(n):
        if i==0 or j==n//2:
            print("*",end=" ")
        elif i==n-1 and j<n-3:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(n):
    for j in range(n):
        if i==0 or j==n//2:
            print("*",end=" ")
        elif i==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(n):
    for j in range(n):
        if i==0 or j==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(n):
    for j in range(n):
        if (i==0 or j==n-1) and (j!=0 and j!=n-1):
            print("*",end=" ")
        elif (j==0 or j==n-1) and (i!=0 and i!=n-1):
            print("*",end=" ")
        elif i==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()