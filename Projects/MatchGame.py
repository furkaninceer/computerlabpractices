class FootballMatch:
    def __init__(self, team1, team2):
        self.team1=team1
        self.team2=team2
        self.team1_goal_count=0
        self.team2_goal_count=0
        self.team1_corner_count=0
        self.team2_corner_count=0
        self.team1_penalty_count=0
        self.team2_penalty_count=0
        self.team1_xg=0
        self.team2_xg=0
        self.team1_faul_count=0
        self.team2_faul_count=0
    def start(self):
        print("The Game Started")
    def corner(self,team):
        print("Corner")
        if team==self.team1:
            self.team1_corner_count+=1
        elif team==self.team2:
            self.team2_corner_count+=1
    def penalty(self,team):
        print("Penalty")
        if team=="team1":
            self.team1_xg+=0.8
        elif team=="team2":
            self.team2_xg+=0.8
        if team==self.team1:
            self.team1_penalty_count+=1
        elif team==self.team2:
            self.team2_penalty_count+=1
        

    def Goal(self,team):
        print("Goal")
        if team==self.team1:
            self.team1_goal_count+=1
        elif team==self.team2:
            self.team2_goal_count+=1
    def xg(self,team):
        xg=float(input("xg:"))
        if team==self.team1:
            self.team1_xg+=xg
        elif team==self.team2:
            self.team2_xg+=xg 

    def faul(self,team):
        print("Faul")
        if team==self.team1:
            self.team1_faul_count+=1
        elif team==self.team2:
            self.team2_faul_count+=1 
    def end(self):
        print("End")
        if self.team1_goal_count>self.team2_goal_count:
            print(f"{self.team1} Won")
            print(f"Score:{self.team1_goal_count},{self.team2_goal_count}")
        elif self.team2_goal_count>self.team1_goal_count:
            print(f"{self.team2} won")
            print(f"Score:{self.team1_goal_count},{self.team2_goal_count}")
        print("Statistics:")
        print(f"Score:{self.team1_goal_count}:{self.team2_goal_count},\
              Xgs:{self.team1_xg}:{self.team2_xg},\
              Corners:{self.team1_corner_count}:{self.team2_corner_count} , \
              Fauls:{self.team1_faul_count}:{self.team2_faul_count},\
              Penalties:{self.team1_penalty_count}:{self.team2_penalty_count}\
            ")
        
#The Game Started
#Penalties
        

Match=FootballMatch("Manchester_City","Arsenal")


def menu():
    print("""10 Action will happen. Choose
          xg 1
          corner 2
          penalty 3
          goal 4
          faul 5
          
""")
    act=10
    action=0
    while act>0:
        if action==0:
            Match.start()
        action=int(input("(1-5)"))
        if action==1:
            team=input("Team Name:")
            Match.xg(team)
        elif action==2:
            team=input("Team Name:")
            Match.corner(team)
        elif action==3:
            team=input("Team Name:")
            Match.penalty(team)
        elif action==4:
            team=input("Team Name:")
            Match.Goal(team)
        elif action==5:
            team=input("Team Name:")
            Match.faul(team)
    
        
        
        act-=1
    Match.end()

menu()