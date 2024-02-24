#This Proect is a simultaneous soccer leauge proect.
#dictionary,class,file,str,tryexcept,mapreducefilterzipenumerate,html,sqlite,bazı tür maçlarda güçsüz güçlüyü yensin,kura usulü turnuva
#en çok gol atan,gol yiyen,korner,penaltı,xg takım ; gol,asist kralı,  

team_dict={"Manchester_City":1260.00,"Arsenal":1100.00,"Chelsea":999.00,"FC_Liverpool":877.30,"Manchester_United":877.30,
           "Tottenham_Hotspur":747.60,"Newcastle_United":650.50,"Aston_Villa":630.70,"West_Ham_United":470.85,
           "Brighton_Hove_Albion":468.30,"Nottingham_Forest":395.58,"FC_Brentford":379.10,"Crystal_Palace":369.45,
           "Everton":350.70,"AFC_Bournemouth":343.50,"Wolverhampton_Wanderers":320.48,"Fulham":304.00,"Burnley":256.75,
           "Sheffield_United":154.95,"Luton_Town":87.20}



        
team_rank=list()


Team_count=20
while Team_count>0:
    name=input()
    last_year_rank=int(input())
    worth=team_dict["name"]
    coach=int(input("1-10"))
    fans=int(input("good or not bad or bad(3,2,1)"))
    managment=int(input("good or not bad or bad(3,2,1)"))
    probably_this_year_rank=(last_year_rank*5)+(worth*4)+(coach*3)+(fans*2)+(managment*1)#5ten emin değilim
    team_rank.append(probably_this_year_rank)
    Team_count-=1

team_rank.sort()
for i in team_rank:
    print(i)

def match(team1,team2): #taçtan emin değilim
    team1_goal_count=0
    team2_goal_count=0
    Taç_count=0
    team1_corner_count=0
    team2_corner_count=0
    team1_penalty_count=0
    team2_penalty_count=0
    team1_xg=0
    team2_xg=0
    team1_faul_count=0
    team2_faul_count=0

    print("10 action will happen")
    print(""" Choose
          start 1
          taç 2
          corner 3
          penalty 4
          goal 5
          action 6

          end 8
""")
    while act>0:
        action=int(input("1,2,3,4,5,6"))
        if action==1:
            print("The game started")
        elif action==2:
            print("Taç")
            Taç_count+=1
        elif action==3:
            print("Corner")
            corner=input("Who has the corner? team1 or team2")
            if corner=="team1":
                team1_corner_count+=1
            elif corner=="team2":
                team2_corner_count+=1
        elif action==4:
            print("Penalty")
            corner=input("Who has the corner? team1 or team2")
            if corner=="team1":
                team1_xg+=0.8
            elif corner=="team2":
                team2_xg+=0.8

        elif action==5:
            print("Goal")
            goal=input("Who scored team1 or team2")
            if goal==team1:
                team1_goal_count+=1
            elif goal==team2:
                team2_goal_count+=1
        elif action==6:
            xg=int(input("xg:"))
            xg_team=input("who had position team1 or team2")
            if xg==team1:
                team1_xg+=xg
            elif xg==team2:
                team2_xg+=xg
        elif action==77:
            print("Faul")
            faul=input("Who had faul team1 or team2")
            if faul==team1:
                team1_faul_count+=1
            elif faul==team2:
                team2_faul_count+=1
        elif action==8:
            print("End")
            break
        act-=1
    if team1_goal_count>team2_goal_count:
        print("team1 Won")
        print(f"Score:{team1_goal_count},{team2_goal_count}")
    elif team2_goal_count>team1_goal_count:
        print("team2 Won")
        print(f"Score:{team1_goal_count},{team2_goal_count}")
    print("Statistics:")
    print(f"corners:{team1_corner_count},{team2_corner_count}")
    print(f"goals:{team1_goal_count},{team2_goal_count}")
    print(f"xgs:{team1_xg},{team2_xg}")



    

    



