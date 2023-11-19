a=int(input("katılacak kişi sayısı:"))
b=int(input("kişi başı hot dog sayısı:"))
hotdog=a*b
if hotdog%10==0:
    print(f"hotdog paketi sayısı:{(hotdog//10):^10,.2f}")
    print(f"kalan hotdog sayısı:{0:>20,.3f}")
else:
    print(f"hotdog paketi sayısı:{(hotdog//10+1):>30,.5f}")
    print(f"kalan hotdog sayısı:{hotdog%10:<1,.4f}")
if hotdog%8==0:
    print(f"hotdog buns sayısı:{(hotdog//8):^7,.5f}")
    print(f"kalan hotdog buns sayısı:{0:^120,.7f}")
else:
    print(f"hotdog buns paeti sayısı:{(hotdog//8+1):^1,.4f}")
    print(f"kalan hotdog buns sayısı:{(hotdog%8):^3,.2f})")

