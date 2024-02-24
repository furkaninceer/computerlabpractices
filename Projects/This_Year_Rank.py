#This Proect is a simultaneous soccer leauge proect.
from collections import OrderedDict
team_dict={"Manchester_City":1260.00,"Arsenal":1100.00,"Chelsea":999.00,"FC_Liverpool":877.30,"Manchester_United":877.30,
   "Tottenham_Hotspur":747.60,"Newcastle_United":650.50,"Aston_Villa":630.70,"West_Ham_United":470.85,
    "Brighton_Hove_Albion":468.30,"Nottingham_Forest":395.58,"FC_Brentford":379.10,"Crystal_Palace":369.45,
        "Everton":350.70,"AFC_Bournemouth":343.50,"Wolverhampton_Wanderers":320.48,"Fulham":304.00,
            "Burnley":256.75,"Sheffield_United":154.95,"Luton_Town":87.20}


team_rank_dict={}

Team_count=20
while Team_count>0:
    name=input("Name:")

    last_year_rank=int(input("Last Year Rank"))
    worth=team_dict[name]
    coach=int(input("1-10"))
    fans=int(input("Good Or Not Bad Or Bad(3,2,1)"))
    managment=int(input("Good Or Not Bad Or Bad(3,2,1)"))
    probably_this_year_rank=(1/last_year_rank)+(worth*4)+(coach*3)+(fans*2)+(managment*1)#5ten emin değilim
    team_rank_dict[name]=probably_this_year_rank
    
    Team_count-=1

for key,value in team_rank_dict.items():
    print(key,value)
   




    


