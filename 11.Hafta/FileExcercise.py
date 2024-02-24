file=open("web.txt","r")

c=input("Team Name:(a,b,c)")
c_var=0

for line in file:
    line=file.readlines()
    if line[0]==c:
       c_var+=1  

print(c_var)
    