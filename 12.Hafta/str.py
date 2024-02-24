a="abcba"
Flag=True
for i in range(0,5):
    j=4-i
    if a[i]==a[j]:
        Flag= True
    else:
        Flag= False

print(Flag)
