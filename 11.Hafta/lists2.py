import random
dice=[0,0,0,0,0,0]
for i in range(1,7):
    num=random.randint(1,6)
    for j in range(1,7):
        if j==num:
            dice[j-1]+=1
print(dice)