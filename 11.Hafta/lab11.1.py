def take_grades(grades):
    another="y"
    while another=="Y" or another=="y":
        grade=int(input("grade"))
        grades.append(grade)
        another=input("another")
def statistic(grades):
    std_count=len(grades)
    class_GPA=sum(grades)/std_count
    square_of_difference_total=0
    for grade in grades:
        square_of_difference_total+=(class_GPA-grade)**2
    num_of_grades_above_GPA=0
    for grade in grades:
        if grade>class_GPA:
            num_of_grades_above_GPA+=1
    try:
        standart_dev=(square_of_difference_total/(std_count-1))**(1/2)
        print(f"standart_dev:{standart_dev}")
    except ZeroDivisionError:  
        print("standart_dev can not be calculated")  
    print(f"class_GPA:{class_GPA}")
    print(f"num_of_grades_above_GPA:{num_of_grades_above_GPA}")
    print(f"percantages of num_of_grades_above_GPA:{num_of_grades_above_GPA/(std_count)*100}")
    print(f"minumum grade:{min(grades)}")
    print(f"maximum grade:{max(grades)}")

def main():
    grades=[]
    take_grades(grades)
    statistic(grades)
main()

