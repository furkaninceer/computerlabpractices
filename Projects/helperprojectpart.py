import functools
#kitaptaki excersizler,pazartesi öğrenilecek şeylerin çalışılması ve denenmesi ve yeni proje haftaya cumaya kadar yapılacak.
#html,pyqt5 ve sqlite(puan tablosu) decorator,generator ve iterator ,map reduce zip filter enumerate,str de kullan.
a=map(lambda x:x**2,(1,2,3,4,5))
for i in a:
    print(i)
b=zip((1,2,3),(4,5,6))
for i in b:
    print(i)
c=filter(lambda x:x**2==25,(1,5))
for i in c:
    print(i)
d=enumerate((1,2,3,4))
for i in d:
    print(i)
d=functools.reduce(lambda x,y:x+y,(1,2,3,4,5))
print(d)
    

