height=int(input("height:"))
for i in range(1,height+1):
    for j in range(height-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()
