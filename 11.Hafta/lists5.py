def two_dimensional_list(two_dimensional_list):
    Flag=True
    for i in range(3):
        column_sum=two_dimensional_list[i][0]+two_dimensional_list[i][1]+two_dimensional_list[i][2]
        if column_sum==15:
            pass
        else:
            Flag=False
    for i in range(3):
        row_sum=two_dimensional_list[0][i]+two_dimensional_list[1][i]+two_dimensional_list[2][i]
        if row_sum==15:
            pass
        else:
            Flag=False
    
    cross_sum=two_dimensional_list[0][0]+two_dimensional_list[1][1]+two_dimensional_list[2][2]
    if column_sum==15:
        pass
    else:
        Flag=False
    if Flag==True:
        print("Lo Shu Magic Square")
    else:
        print("Not Lo Shu Magic Square")
two_dimensional_list([[4,9,2],
[3,5,7],
[8,1,6]
])
    
