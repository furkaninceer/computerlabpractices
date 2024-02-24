number_of_std=int(input("number_of_std:"))
midterm_rate=0.4
final_rate=0.6
while number_of_std>0:
    midterm=int(input("midterm(0,100)"))
    final=int(input("final(0,100)"))
    term_grade=midterm*midterm_rate+final*final_rate
    if term_grade>=60:
        print(f"the course is passed and your grade is {term_grade} ")
    else:
        print(f"the course is not passed and your grade is {term_grade} ")
    number_of_std-=1