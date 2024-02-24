def take_grades(file,turkish_grades,mat_grades):
    std_no=file.readline()
    while std_no!="":
        turkish_grade=int(file.readline())
        mat_grade=int(file.readline())
        turkish_grades[int(std_no)-1]=turkish_grade
        mat_grades[int(std_no)-1]=mat_grade
        std_no=file.readline()

def display_chart(std_count,turkish_grades,mat_grades):
    print("Std_no    Turkish Grade    Mat Grade")
    print("------    -------------    ---------")
    for i in range(std_count):
        print(f"{i+1:^6}{turkish_grades[i]:^21}{mat_grades[i]:^9}")
def main():
    file=open("a.txt","r")
    std_count=int(file.readline())
    turkish_grades=[0]*std_count
    mat_grades=[0]*std_count
    take_grades(file,turkish_grades,mat_grades)
    display_chart(std_count,turkish_grades,mat_grades)
main()