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


#Program:
def display_menu():
    print("1. Find...")
    print("2. Replace all...")
    print("3. Replace one by one...")
    print("0. Quit...")
    print("Enter your choice [0-3]:", end="")

def get_number(lower_limit,upper_limit):
    # Alternative-1:
    # incorrect_entry = True
    # while incorrect_entry==True:
    #     try:
    #         number = int(input())
    #         if number>=lower_limit and number<=upper_limit:
    #             incorrect_entry = False
    #         else:
    #             print("incorrect data entry, please enter again:",end="")
    #     except ValueError:
    #         print("incorrect data entry, please enter again:",end="")
    # return number
    #
    # Alternative-2:
    number=input()
    while not (number.isdigit() and int(number)>=lower_limit and int(number)<=upper_limit):
        number = input("incorrect data entry, please enter again:")
    return int(number)

def get_yes_no():
    answer = input()
    while answer not in "yYnN":
        answer = input("incorrect data entry, please enter again:")
    return answer

def find(text,search_text):
    occurrence_count=0
    search_text_length=len(search_text)
    print("No Location")
    print("-- --------")
    location_index=text.find(search_text)
    while location_index!=-1:
        occurrence_count+=1
        print(f"{occurrence_count:2} {location_index+1:4}")
        location_index = text.find(search_text,location_index+search_text_length)

def replace_all(text,search_text,new_text):
    return text.replace(search_text,new_text)

def replace_one_by_one(text,search_text,new_text):
    search_text_length=len(search_text)
    search_start_index=0
    resulting_text=""
    location_index=text.find(search_text,search_start_index)
    while location_index!=-1:
        print(f"Do you want to replace the text in location {location_index+1} (y/Y/n/N)?:",end="")
        replace=get_yes_no()
        resulting_text = resulting_text + text[search_start_index:location_index]
        if replace.upper()=="Y":
            resulting_text = resulting_text+new_text
        else:
            resulting_text = resulting_text+search_text
        search_start_index=location_index+search_text_length
        location_index = text.find(search_text,search_start_index)
    resulting_text=resulting_text+text[search_start_index:]
    return resulting_text

def main():
    text=input("Enter a piece of text:")
    out='N'
    while out.upper()=='N':
        display_menu()
        menu_choice=get_number(0,3)
        if menu_choice==1:
            search_text=input("Enter the text you want to search:")
            find(text,search_text)
        elif menu_choice==2:
            search_text = input("Enter the text you want to search:")
            new_text = input("Enter the text you want to replace:")
            text=replace_all(text,search_text,new_text)
            print(text)
        elif menu_choice==3:
            search_text = input("Enter the text you want to search:")
            new_text = input("Enter the text you want to replace:")
            text=replace_one_by_one(text,search_text,new_text)
            print(text)
        else:
            print("Are you sure you want to quit(y/Y/n/N)?:",end="")
            out=get_yes_no()

main()
