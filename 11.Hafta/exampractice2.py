def two_dimensional_list2(two_dimensional_list3):
    flag=False
    for i in range(3):
        result=two_dimensional_list3[i][1]+two_dimensional_list3[i][2]+two_dimensional_list3[i][3]
        if result==15:
            flag=True
    result2=0
    for i in range(3):
        result2+=two_dimensional_list3[i][i]
    if result2==15:
        flag=True
    result3=0
    for i in range(3):
        result3+=two_dimensional_list3[i][2-i]
    if result3==15:
        flag=True
    if flag:
        print("Lo Shu Magic Square")
    else:
        print("Not Lo Shu Magic Square")
two_dimensional_list2([3,4,5],
                      [1,8,6],
                      [2,9,4])
    