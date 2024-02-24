from collections import OrderedDict
import random
team_dict={"Manchester_City":1260.00,"Arsenal":1100.00,"Chelsea":999.00,"FC_Liverpool":877.30,"Manchester_United":877.30,
   "Tottenham_Hotspur":747.60,"Newcastle_United":650.50,"Aston_Villa":630.70,"West_Ham_United":470.85,
    "Brighton_Hove_Albion":468.30,"Nottingham_Forest":395.58,"FC_Brentford":379.10,"Crystal_Palace":369.45,
        "Everton":350.70,"AFC_Bournemouth":343.50,"Wolverhampton_Wanderers":320.48,"Fulham":304.00,
            "Burnley":256.75,"Sheffield_United":154.95,"Luton_Town":87.20}

def this_year_rank(last,worth,coach,fans,managment):
    return last*5+worth*4+coach*3+fans*2+managment*1

Manchester_City=["Manchester_City",1,team_dict["Manchester_City"],10,8,10,this_year_rank(1,team_dict["Manchester_City"],10,8,10),0,0,0,0,0,0,0]
Arsenal=["Arsenal",2,team_dict["Arsenal"],9,9,9,this_year_rank(2,team_dict["Arsenal"],9,9,9),0,0,0,0,0,0,0]
Chelsea=["Chelsea",12,team_dict["Chelsea"],9,8,7,this_year_rank(12,team_dict["Chelsea"],9,8,7),0,0,0,0,0,0,0]
FC_Liverpool=["FC_Liverpool",5,team_dict["FC_Liverpool"],10,10,9,this_year_rank(5,team_dict["FC_Liverpool"],10,10,9),0,0,0,0,0,0,0]
Manchester_United=["Manchester_United",3,team_dict["Manchester_United"],8,10,6,this_year_rank(3,team_dict["FC_Liverpool"],8,10,6),0,0,0,0,0,0,0]
Tottenham_Hotspur=["Tottenham_Hotspur",8,team_dict["Tottenham_Hotspur"],8,9,10,this_year_rank(8,team_dict["Tottenham_Hotspur"],8,9,10),0,0,0,0,0,0,0]
Newcastle_United=["Newcastle_United",4,team_dict["Newcastle_United"],8,8,10,this_year_rank(4,team_dict["Newcastle_United"],8,8,10),0,0,0,0,0,0,0]
Aston_Villa=["Aston_Villa",7,team_dict["Aston_Villa"],8,8,9,this_year_rank(7,team_dict["Aston_Villa"],8,8,9),0,0,0,0,0,0,0]
West_Ham_United=["West_Ham_United",14,team_dict["West_Ham_United"],7,8,8,this_year_rank(14,team_dict["West_Ham_United"],7,8,8),0,0,0,0,0,0,0]
Brighton_Hove_Albion=["Brighton_Hove_Albion",6,team_dict["Brighton_Hove_Albion"],9,5,10,this_year_rank(6,team_dict["Brighton_Hove_Albion"],9,5,10),0,0,0,0,0,0,0]
FC_Brentford=["FC_Brentford",9,team_dict["FC_Brentford"],5,5,7,this_year_rank(9,team_dict["FC_Brentford"],5,5,7),0,0,0,0,0,0,0]
Crystal_Palace=["Crystal_Palace",11,team_dict["Crystal_Palace"],6,7,7,this_year_rank(11,team_dict["Crystal_Palace"],6,7,7),0,0,0,0,0,0,0]
Everton=["Everton",17,team_dict["Everton"],6,8,5,this_year_rank(17,team_dict["Everton"],6,8,5),0,0,0,0,0,0,0]
AFC_Bournemouth=["AFC_Bournemouth",15,team_dict["AFC_Bournemouth"],5,6,5,this_year_rank(15,team_dict["AFC_Bournemouth"],5,6,5),0,0,0,0,0,0,0]
Wolverhampton_Wanderers=["Wolverhampton_Wanderers",13,team_dict["Wolverhampton_Wanderers"],6,6,7,this_year_rank(13,team_dict["Wolverhampton_Wanderers"],6,6,7),0,0,0,0,0,0,0]
Fulham=["Fulham",10,team_dict["Fulham"],5,5,6,this_year_rank(10,team_dict["Fulham"],5,5,6),0,0,0,0,0,0,0]

team_list=[Manchester_City,Arsenal,Chelsea,FC_Liverpool,Manchester_United,
   Tottenham_Hotspur,Newcastle_United,Aston_Villa,West_Ham_United,
    Brighton_Hove_Albion,FC_Brentford,Crystal_Palace,
        Everton,AFC_Bournemouth,Wolverhampton_Wanderers,Fulham]

class FACupSimult:
    def __init__(self,team1,team2,team3,team4,team5,team6,team7,team8,team9,team10,
                 team11,team12,team13,team14,team15,team16):
        self.team1=team1
        self.team2=team2
        self.team3=team3
        self.team4=team4
        self.team5=team5
        self.team6=team6
        self.team7=team7
        self.team8=team8
        self.team9=team9
        self.team10=team10
        self.team11=team11
        self.team12=team12
        self.team13=team13
        self.team14=team14
        self.team15=team15
        self.team16=team16
        

    def Match_of_two_teams(teamone,teamtwo):
        if teamone[4]>=9 and teamone[4]<=10:
            teamone_coach=random.uniform(1.5,2)*teamone[3]
        elif teamone[4]>=8 and teamone[4]<9:
            teamone_coach=random.uniform(1,1.5)*teamone[3]
        elif teamone[4]>=7 and teamone[4]<8:
            teamone_coach=random.uniform(0.5,1)*teamone[3]
        elif teamone[4]<7:
            teamone_coach=random.uniform(0,0.5)*teamone[3]
        if teamtwo[4]>=9 and teamtwo[4]<=10:
            teamtwo_coach=random.uniform(1.5,2)*teamtwo[3]
        elif teamtwo[4]>=8 and teamtwo[4]<9:
            teamtwo_coach=random.uniform(1,1.5)*teamtwo[3]
        elif teamtwo[4]>=7 and teamtwo[4]<8:
            teamtwo_coach=random.uniform(0.5,1)*teamtwo[3]
        elif teamtwo[4]<7:
            teamtwo_coach=random.uniform(0,0.5)*teamtwo[3]

        if teamone_coach<=20 and teamone_coach>=15:
            teamone_worth=random.uniform(1.5,2)*teamone[2]
        elif teamone_coach<=15 and teamone_coach>=10:
            teamone_worth=random.uniform(1,1.5)*teamone[2]
        elif teamone_coach<=10 and teamone_coach>=5:
            teamone_worth=random.uniform(0.5,1)*teamone[2]
        elif teamone_coach<=5 and teamone_coach>=0:
            teamone_worth=random.uniform(0,0.5)*teamone[2]
        if teamtwo_coach<=20 and teamtwo_coach>=15:
            teamtwo_worth=random.uniform(1.5,2)*teamtwo[2]
        elif teamtwo_coach<=15 and teamtwo_coach>=10:
            teamtwo_worth=random.uniform(1,1.5)*teamtwo[2]
        elif teamtwo_coach<=10 and teamtwo_coach>=5:
            teamtwo_worth=random.uniform(0.5,1)*teamtwo[2]
        elif teamtwo_coach<=5 and teamtwo_coach>=0:
            teamtwo_worth=random.uniform(0,0.5)*teamtwo[2]
        
        if teamone[1]<=23 and teamone[1]>=15:
            teamone_power=random.uniform(0,0.5)*teamone_worth
        elif teamone[1]<15 and teamone[1]>=10:
            teamone_power=random.uniform(0.5,1)*teamone_worth
        elif teamone[1]<10 and teamone[1]>=5:
            teamone_power=random.uniform(1,1.5)*teamone_worth
        elif teamone[1]<5 and teamone[1]>=0:
            teamone_power=random.uniform(1.5,2)*teamone_worth
        if teamtwo[1]<=23 and teamtwo[1]>=15:
            teamtwo_power=random.uniform(0,0.5)*teamtwo_worth
        elif teamtwo[1]<15 and teamtwo[1]>=10:
            teamtwo_power=random.uniform(0.5,1)*teamtwo_worth
        elif teamtwo[1]<10 and teamtwo[1]>=5:
            teamtwo_power=random.uniform(1,1.5)*teamtwo_worth
        elif teamtwo[1]<5 and teamtwo[1]>=0:
            teamtwo_power=random.uniform(1.5,2)*teamtwo_worth
        
        if teamone_power>teamtwo_power:
            if len(teamone)==14 and len(teamtwo)==14:
                teamone.append(True)
                teamtwo.append(False)
            else:
                teamone[14]=True
                teamtwo[14]=False
            teamone[8]+=int(teamone_power//teamtwo_power/100)
            teamtwo[8]+=int(teamone[8]*0.6/100)
            teamone[9]+=int(teamone[8]*0.6/100)
            teamtwo[9]+=int(teamone_power//teamtwo_power/100)
            
        elif teamone_power<teamtwo_power:
            if len(teamone)==14 and len(teamtwo)==14:
                teamtwo.append(True)
                teamone.append(False)
            else:
                teamtwo[14]=True
                teamone[14]=False
            teamtwo[8]+=int(teamtwo_power//teamone_power/100)
            teamone[8]+=int(teamtwo[8]*0.6/100)
            teamone[9]+=int(teamtwo_power//teamone_power/100)
            teamtwo[9]+=int(teamtwo[8]*0.6/100)
           
        elif teamone_power==teamtwo_power:
            FACupSimult.Match_of_two_teams(teamone,teamtwo)
        
        teamone[10]=teamone[8]-teamone[9]
        teamtwo[10]=teamtwo[8]-teamtwo[9]
        
        


Football=FACupSimult(Manchester_City,Arsenal,Chelsea,FC_Liverpool,Manchester_United,
   Tottenham_Hotspur,Newcastle_United,Aston_Villa,West_Ham_United,
    Brighton_Hove_Albion,FC_Brentford,Crystal_Palace,
        Everton,AFC_Bournemouth,Wolverhampton_Wanderers,Fulham)

for i in range(1,9):
    team_index=random.randint(0,17-2*i)
    team1=team_list[team_index]
    team_list.pop(team_index)
    team_index2=random.randint(0,16-2*i)
    team2=team_list[team_index2]
    team_list.pop(team_index2)
    FACupSimult.Match_of_two_teams(team1,team2)
team_list=[Manchester_City,Arsenal,Chelsea,FC_Liverpool,Manchester_United,
   Tottenham_Hotspur,Newcastle_United,Aston_Villa,West_Ham_United,
    Brighton_Hove_Albion,FC_Brentford,Crystal_Palace,
        Everton,AFC_Bournemouth,Wolverhampton_Wanderers,Fulham]
team_list2=[]
for i in team_list:
    if i[14]:
        team_list2.append(i)
for i in range(1,5):
    team_index=random.randint(0,9-2*i)
    team1=team_list2[team_index]
    team_list2.pop(team_index)
    team_index2=random.randint(0,8-2*i)
    team2=team_list2[team_index2]
    team_list2.pop(team_index2)
    FACupSimult.Match_of_two_teams(team1,team2)
team_list=[Manchester_City,Arsenal,Chelsea,FC_Liverpool,Manchester_United,
   Tottenham_Hotspur,Newcastle_United,Aston_Villa,West_Ham_United,
    Brighton_Hove_Albion,FC_Brentford,Crystal_Palace,
        Everton,AFC_Bournemouth,Wolverhampton_Wanderers,Fulham]
team_list3=[]
for i in team_list:
    if i[14]:
        team_list3.append(i)
for i in range(1,3):
    team_index=random.randint(0,5-2*i)
    team1=team_list3[team_index]
    team_list3.pop(team_index)
    team_index2=random.randint(0,4-2*i)
    team2=team_list3[team_index2]
    team_list3.pop(team_index2)
    FACupSimult.Match_of_two_teams(team1,team2)
team_list=[Manchester_City,Arsenal,Chelsea,FC_Liverpool,Manchester_United,
   Tottenham_Hotspur,Newcastle_United,Aston_Villa,West_Ham_United,
    Brighton_Hove_Albion,FC_Brentford,Crystal_Palace,
        Everton,AFC_Bournemouth,Wolverhampton_Wanderers,Fulham]
team_list4=[]
for i in team_list:
    if i[14]:
        team_list4.append(i)
print(team_list4,"CHAMPİON")
