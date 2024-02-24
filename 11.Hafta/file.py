file=open("web.txt","r")


The_line=int(input("The_line:"))
line_count=0
for line in file:
    line=file.readlines()
    line_count+=1
    if line_count==The_line:
        print(line)