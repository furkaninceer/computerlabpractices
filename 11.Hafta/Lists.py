file=open("web.txt","r")
a=[]
for i in file:
    a.append(int(i.strip()))
num=int(input("charge num:"))
if num in a:
    print("the Charge Num is valid.")
else:
    print("the Charge Num is not valid.")

