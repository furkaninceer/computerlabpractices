exam_count=2
def get_accident(file,all_std_grades,all_std_grades_count):
    a=file.readline()
    while a!="":
        b=int(file.readline())
        c=int(file.readline())
        all_std_grades[int(a)-1][b-1]+=c
        all_std_grades_count[int(a)-1][b-1]+=1

        a=file.readline()

def display(all_std_grades,all_std_grades_count,alist):
    for i in alist:
        print(f"   {i}",end="")
    for i in alist:
        print(f"   {i} count",end="")
    print()

    for i in range(exam_count):
        print("   ------",end="")
    for i in range(exam_count):
        print("   --------------",end="")
    print()
    for i in range(3):
        print(f"{i+1}:  ",end="")
        for j in range(exam_count):
            print(all_std_grades[i][j],end="       ")
        for j in range(exam_count):
            print(all_std_grades_count[i][j],end="                   ")
        print()
        print(sum(all_std_grades[i]))

def main():
    alist=["birinci","ikinci"]
    file=open("b.txt","r")
    all_std_grades=[]
    all_std_grades_count=[]
    for i in range(3):
        a_std_grades=[0]*exam_count
        all_std_grades.append(a_std_grades)
        a_std_grades_count=[0]*exam_count
        all_std_grades_count.append(a_std_grades_count)
    get_accident(file,all_std_grades,all_std_grades_count)
    display(all_std_grades,all_std_grades_count,alist)
main()

