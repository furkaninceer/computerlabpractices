öğrenci_sayısı=int(input("Sınıftaki öğrenci sayısı:"))
a=0
while a<=öğrenci_sayısı:
    İsim=input("İsminiz:")
    Soyad=input("Soyadınız:")
    L=int(input("laboratory grade:"))
    M=int(input("Midterm grade:"))
    F=int(input("Final grade:"))
    print(İsim,Soyad,":",L,M,F)
a+=1
