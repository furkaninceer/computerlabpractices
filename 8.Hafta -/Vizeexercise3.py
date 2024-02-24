num1=int(input("num1:"))
num2=int(input("num2:"))
while num2%num1!=0 and num1%num2!=0:
    if num2>num1:
        num1=num2%num1
    elif num1>num2:
        num2=num1%num2
if num2>num1:
        print(num1)
elif num1>num2:
        print(num2)

    
