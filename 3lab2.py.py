min_gpa=2
gpa_factor=35
min_wage=2400
female_scolarship=150



name=input("isim:")
surname=input("soyisim:")
GPA=float(input("GPA:"))
Gender=input("Gender:")
Family_income=float(input("family_income:")) 
monthly=250
if GPA>=min_gpa:
    monthly=monthly+GPA*gpa_factor
if Gender=="Female" and Family_income<min_wage:
    monthly=monthly+female_scolarship


print(monthly)