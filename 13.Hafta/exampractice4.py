# Problem:
# Write a program that takes a piece of text from the user and allows
#
# -	Find: prints the starting positions of a text that the user enters
# -	Replace all: replaces a text entered by the user with a new text
#                    to be entered by the user in all locations and
#                    prints the resulting text on the screen.
# -	Replace one by one: replaces a text to be entered by the user
#                           with a new text to be entered by the user
#                           at every location (if the user wishes) and
#                           prints the resulting text on the screen.
#
# operations on that text via a menu.

def menu():
    print("1.Find")
    print("2.Replace all")
    print("3.Replace one by one ")
    print("0. Quit")
    print("Select 0-3")
def find(text,text_part):
    tour_count=0
    start_index=0
    location=text.find(text_part,start_index)
    while location!=-1:
        tour_count+=1
        print(f"{tour_count} {location}")
        location=text.find(text_part,start_index+len(text_part))




def replace_all(text,text_part,replace_text):
    print(text.replace(text_part,replace_text))

def get_num():
    num=int(input("number:"))
def replace_one_by_one(text,text_part,new_text):
    length=len(text_part)
    start_index=0
    result=""
    location=text.find(text_part,start_index)
    while location!=-1:
        result=result+text[start_index:location]
        answer=input(f"Do you want to replace {text_part} with {new_text} y or no")
        if answer=="y":
            result+=new_text
        else:
            result+=text_part
        start_index=location+length
        location=text.find(text_part,start_index+length)
    result+=text[start_index:]
    return result






    result+=text[start_index:]
    return result
def main():
    text=input("text:")
    action=-1
    while action!=0:
        menu()
        action=int(input("action:"))
        if action==0:
            print("The end")
        elif action==1:
            text_part=input("text_part")
            find(text,text_part)
        elif action==2:
            text_part=(input("text_part:"))
            new_text=(input("new_text:"))
            replace_all(text,text_part,new_text)
        elif action==3:
            text_part=(input("text_part:"))
            new_text=(input("new_text:"))
            replace_one_by_one(text,text_part,new_text)
main()

