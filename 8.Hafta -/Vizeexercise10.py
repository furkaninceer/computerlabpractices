def hanoi(n,from_,to,temp):
    if n>0:
        hanoi(n-1,from_,temp,to)
        print(f"put this disk from {from_} to {to}")
        hanoi(n-1,temp,to,from_)
hanoi(2,"a","b","c")