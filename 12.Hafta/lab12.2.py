

def get_fan_counts(teams,cont):
    
    while cont=="y":
        team=input("team")
        cont=input("cont")
        if team in teams:
            teams[team]+=1
        else:
            teams[team]=1
        
def display(teams):
    for i,j in teams.items():
        print(i,j)
def main():
    cont="y"
    teams={}
    get_fan_counts(teams,cont)
    display(teams)
if __name__== "__main__":
    main()