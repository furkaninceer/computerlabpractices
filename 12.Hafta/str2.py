a="abcbaevf"
num_of_letters=0
letters=[]
for i in a:
    if i in letters:
        pass
    else:
        letters.append(i)
        num_of_letters+=1
print(num_of_letters)