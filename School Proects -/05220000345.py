def display(field_size,field):
    for i in range(field_size):
        if i==0:
            print("      ",f"{Alph[i]:4}",end="")
        else:
            print(f"{Alph[i]:4}",end="")
    print()
    print("     "+"-"*(4*field_size+1))
    for i,row in enumerate(field):

        print(f"   {i+1} |",end="")
        for j in row:
            print(f" {j}",end=" |")
        print(f" {i+1}",end="")
        print()
        print("     "+"-"*(4*field_size+1))

    for i in range(field_size):
        if i==0:
            print("      ",f"{Alph[i]:4}",end="")
        else:
            print(f"{Alph[i]:4}",end="")
    print()

    

    
    
   
    
def move_check(field_size,field,direction,player):
    directions={"N":(-1,0),"NE":(-1,1),"NW":(-1,-1),"S":(1,0),"SE":(1,1),"SW":(1,-1),"W":(0,-1),"E":(0,1)}
    for i in range(field_size):
        for j in range(field_size):
            if field[i][j]==player:
                row_move,column_move=directions[direction]
                row,column=i+row_move,j+column_move
                if field_size>row>=0 and field_size>column>=0 and field[row][column]==" ":
                    field[row][column]=player
                    field[i][j]=" "
                    return True
    return False

def small_stones(field,field_size,location):
    row,col=int(location[0])-1,Alph.index(location[1])-Alph.index("A")
    if 0<=row<field_size and 0<=col<field_size and field[row][col]==" ":
        field[row][col]="O"
        return True
    else:
        return False
def winning_check(field_size,field,players,directions,curr):
    for i in range(field_size):
        for j in range(field_size):
            
            if field[i][j]==players[curr]:
                directions={"N":(-1,0),"NE":(-1,1),"NW":(-1,-1),"S":(1,0),"SE":(1,1),"SW":(-1,-1),"W":(0,-1),"E":(0,1)}
                for a,b in directions.values():
                    row,col=i+a,j+b
                    if 0<=row<field_size and 0<=col<field_size:
                        if field[row][col]!=" ":
                            Flag=True
                        else:
                            Flag=False
                            break
                        
            
            
    if Flag==True:
        return True
    else:
        return False
                            

                        
                    
                        
    
    
                        
                


def main():
    
    players = [input("Enter a capital letter to represent player 1 (except O): "),input("Enter a capital letter to represent player 2 (except O): ")]
    players[0],players[1]=players[0].upper(),players[1].upper()
    while players[0] not in Alph or players[1] not in Alph:
        players = [input("Try Again Enter a capital letter to represent player 1 (except O): "),input("Try Again Enter a capital letter to represent player 2 (except O): ")]
        players[0],players[1]=players[0].upper(),players[1].upper()
    curr=0
    

    field=[]
    try:
        field_size=int(input("Enter the row/column number of the playing field (3,5,7):"))
        while field_size not in [3,5,7]:
            field_size=int(input("Try Again Enter the row/column number of the playing field (3,5,7):"))
    except ValueError:
        field_size=int(input("ValueError Enter the row/column number of the playing field (3,5,7):"))
        while field_size not in [3,5,7]:
            field_size=int(input("Try Again Enter the row/column number of the playing field (3,5,7):"))
    for i in range(field_size):
        field.append([" "]*field_size) 
    field[0][int(field_size/2)]=players[0]
    field[field_size-1][int(field_size/2)]=players[1]
    curr=0

    while True:
            
        player=players[curr]
        display(field_size,field)
        direction=input(f"Player {player}, please enter the direction you want to move your own big stone(N,S,E,W,NE,NW,SE,SW)")
        while direction not in ["N","S","E","W","NE","NW","SE","SW"]:
            direction=input(f"Player {player}, please enter the direction you want to move your own big stone(N,S,E,W,NE,NW,SE,SW)")
        

        if move_check(field_size,field,direction,player):
            display(field_size,field)
            
            location=input(f"Player {player} please enter the location where you want to place a small stone (like 1A)")
            
            if small_stones(field,field_size,location):
                display(field_size,field)
                directions={"N":(-1,0),"NE":(-1,1),"NW":(-1,-1),"S":(1,0),"SE":(1,1),"SW":(-1,-1),"W":(0,-1),"E":(0,1)}
                if winning_check(field_size,field,players,directions,1-curr):
                    print()
                    
                    player=players[curr]
                    print(f"       {player} won")
                    return False


                else:
                    curr=1-curr
            
            else:
                print("This place is full")
                while small_stones(field,field_size,location)==False:
                    location=input(f"Player {player} please enter the location where you want to place a small stone (like 1A)")
                    
                    curr=1-curr
        else:
            print("This place is full")
            while move_check(field_size,field,direction,player)==False:  
                direction=input(f"Player {player}, please enter the direction you want to move your own big stone(N,S,E,W,NE,NW,SE,SW)")
                while direction not in ["N","S","E","W","NE","NW","SE","SW"]:
                    direction=input(f"Player {player}, please enter the direction you want to move your own big stone(N,S,E,W,NE,NW,SE,SW)")
        
            display(field_size,field)
            location=input(f"Player {player} please enter the location where you want to place a small stone (like 1A)")
           
            if small_stones(field,field_size,location):
                display(field_size,field)
                directions={"N":(-1,0),"NE":(-1,1),"NW":(-1,-1),"S":(1,0),"SE":(1,1),"SW":(-1,-1),"W":(0,-1),"E":(0,1)}
                if winning_check(field_size,field,players,directions,1-curr):
                    print()
                    
                    player=players[curr]
                    print(f"       {player} won")
                    return False


                else:
                    curr=1-curr    
            else:
                print("This place is full")
                while small_stones(field,field_size,location)==False:
                    location=input(f"Player {player} please enter the location where you want to place a small stone (like 1A)")
                   
                curr=1-curr
if __name__ == "__main__":
        pass
            
cont="Y"   
while cont=="Y" :
    Alph="ABCDEFGHIJKLMNOPQRSTUVWXYZ"



       
    main()
    cont=input("would you like to play again?(Y/N)")
    cont=cont.upper()
    while cont not in ["Y","N"]:
        cont=input("would you like to play again?(Y/N)")
        cont=cont.upper()

        

 
