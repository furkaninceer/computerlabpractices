number=int(input("number:"))
while number>1:
    for i in range(2,int(number**0.5)+1):
        if number%i==0:
            print("asal değil")
            break
    else:
        print("asal")
    
    break
        
