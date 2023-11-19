def draw_rectangle(v,h):
    for i in range(v):
        for i in range(h):
            print("*",end="")
        print("")
def calculate_rectangle_info(v,h):
    return v*h,2*(v+h)
def get_number():
    num=int(input("num:"))
    while num>4 or num<0:
        num=int(input("num:"))


def fact(a):
    product=1
    for i in range(2,a+1):
        product*=i
    return product
def combination(n,k):
    return fact(n)/fact(k)*fact(n-k)
def show_menu():
    print("1 Draw rectangle")
    print("2 Rectangle info")
    print("3 Factorial")
    print("4 combination")
    print("0 Exit")
def main():
    exit="n"
    while exit=="n" or exit=="N":
        show_menu()
        b=input("insert a func")
        if b=="1":
            v=int(input("v:"))
            h=int(input("h:"))
            draw_rectangle(v,h)
        elif b=="2":
            v=int(input("v:"))
            h=int(input("h:"))
            area,perimeter=calculate_rectangle_info(v,h)
            print(area,perimeter)     
        elif b=="3":
            n=int(input("n:"))
            c=fact(n)
            print(c)
        elif b=="4":
            n=int(input("n:"))
            k=int(input("n:"))
            a=combination(n,k)
            print(a)
        else:
            exit=input("y,Y,N,n")
            while exit not in ["y","Y","N","n"]:
                exit=input("y,Y,N,n")

        



main()

get_number()