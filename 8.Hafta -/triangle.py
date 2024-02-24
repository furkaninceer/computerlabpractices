def fibbonaci(num):
    if num==1:
        return 1
    elif num==2:
        return 1
    else:
        return fibbonaci(num-1)+fibbonaci(num-2)
print(fibbonaci(4))