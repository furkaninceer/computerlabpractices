def display_menu():
    print("1.Find")
    print("2.replace all")
    print("3.replace one by one")
    print("0.Quit")
    
    
def get_number(minu,maxu):
    num=input("num")
    while not num.isdigit() and (num>maxu or num<minu):
        num=input()
    return int(num)
def get_yes_no():
    answer=input("answer")
    while answer not in ["y","n","N","Y"]:
        answer=input()
    return answer

def find(text,researched_text):
    occurrence_count=0
    search_text_len=len(researched_text)
    location_index=text.find(researched_text)
    while location_index!=-1:
        occurrence_count+=1
        location_index=text.find(researched_text,location_index+search_text_len)
      
def replace_one_by_one(text,researched_text,new_text):
    search_text_len=len(researched_text)
    search_start_index=0
    resulting_text=""
    location_index=text.find(researched_text,search_start_index)
    while location_index!=-1:
        print()
        replace=get_yes_no()
        resulting_text=resulting_text+text[search_start_index]

def replace_all(text,researched_text,new_text):
    return text.replace(researched_text,new_text)

def main():
    text=input("text")
    out="N"
    while out.upper=="N":
        display_menu()
        menu_choice=get_number(0,3)
        if menu_choice=="0":
            out
        elif menu_choice=="1":
            researched_text=input("researched_text")
            print(find(text,researched_text))

        elif menu_choice=="2":           
            researched_text=input("researched_text")
            new_text=input("new_text")
            print(replace_all(text,researched_text,new_text))
        elif menu_choice=="3":
            researched_text=input("researched_text")
            new_text=input("new_text")
            print(replace_one_by_one(text,researched_text,new_text))
    out=get_yes_no()

main()




