midterm1=int(input("midterm1(0,100)"))
midterm2=int(input("midterm2(0,100)"))
avarage_of_midterms=(midterm1+midterm2)/2
midterm_rate=0.4
final_rate=0.6
if avarage_of_midterms>=75:
    print(f"the course is passed and your grade is {avarage_of_midterms}")
else:
    final=int(input("final(0,100)"))
    result=avarage_of_midterms*midterm_rate+final*final_rate
    if result>=50:
        print(f"the course is passed and your grade is {result}")
    else:
        print(f"the course is not passed and your grade is {result}")

