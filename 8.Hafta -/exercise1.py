import random
pc=False
user=False
def rock_paper_scissors():
    num=random.randint(1,3)
    if num==1:
        pc_choice="rock"
    elif num==2:
        pc_choice="paper"
    elif num==3:
        pc_choice="scissors"
    user_choice=input(f"rock or paper or scissors:")
    def rock_paper_scissor_rules(a,b):
        global user
        global pc
        if a=="rock" and b=="paper":
            user=True
        elif a=="paper" and b=="rock":
            pc=True
        elif a=="scissors" and b=="rock":
            user=True
        elif a=="rock" and b=="scissors":
            pc=True
        elif a=="paper" and b=="scissors":
            user=True
        elif a=="scissors" and b=="paper":
            pc=True
        else:
            rock_paper_scissors()
        if user==True:
            return "user won"
        elif pc==True:
            return "pc won"
    return rock_paper_scissor_rules(pc_choice,user_choice)
    
print(rock_paper_scissors())


