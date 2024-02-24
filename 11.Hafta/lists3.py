file=open("web.txt","r")
correct_count=0
for i in range(1,21):
    answer=input("answer:(a,b,c,d)")
    for line in file:
        if str(i) in line:
            ind=line.index(str(i))
            c_answer=line[ind+3]
            if answer==c_answer:
                correct_count+=1
if correct_count>=15 and correct_count<=20:
    print("The course is passed")
else:
    print("The course is not passed")