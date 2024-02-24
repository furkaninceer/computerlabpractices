a=[1,2,3]
midpoint=len(a)//2
if a[2]>a[midpoint]:
    for i in range(midpoint+1):
        a.pop(i)
else:
    for i in range(midpoint,len(a)):
        a.pop(i)