a=int(input("number of months"))
if 0<a<=12:
    if a==2:
        print(28)
    elif a==4 or a==6 or a==9 or a==11 :
        print(30)
    else:
        print(31)
            

else:
    print("error")