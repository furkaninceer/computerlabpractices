
def finding_max_height(g,t):
    max_h=1/2*g*t**2
    return max_h
    
def finding_max_range(Vx,t):
    range=Vx*2*t
    return range
def finding_height_at_given_second(Vy,g,T):
    h=Vy*T-1/2*g*T**2
    while Vy/g*2<T:
        print("Verdiğiniz değerlerin gerçekleşmesi gerçek hayatta imkansız lütfen 2*(Hızın y bileşeni)/(yerçekimi ivmesi)'nin süreden büyük olmasını sağlayarak değerleri tekrar giriniz.")
        Vy=int(input("Hızın y bileşenini giriniz."))
        g=int(input("Yer çekimi ivmesini giriniz."))
        T=int(input("Zamanı giriniz."))
    
    h=Vy*T-1/2*g*T**2
    return h
def finding_range_at_given_second(Vx,T):
    R=Vx*T
    return R
        

Vx=int(input("Hızın x bileşenini giriniz."))
Vy=int(input("Hızın y bileşenini giriniz."))
g=int(input("Yer çekimi ivmesini giriniz."))
t=Vy/g
T=int(input("Zamanı giriniz."))
max_h=finding_max_height(g,t)
range=finding_max_range(Vx,t)
h=finding_height_at_given_second(Vy,g,T)
R=finding_range_at_given_second(Vx,T)
print(f"Maximum yükseklik:{max_h}")
print(f"Maximum Range:{range}")
print(f"Verilen Zamanda yükseklik:{h}")
print(f"Verilen Zamanda range:{R}")



