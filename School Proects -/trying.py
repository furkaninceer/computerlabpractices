
Alph="ABCDEFG"
def display(field_size,field):
    for i in range(field_size):
        if i==0:
            print("      ",f"{Alph[i]:4}",end="")
        else:
            print(f"{Alph[i]:4}",end="")
    print()
    print("     -------------")
    for i,row in enumerate(field):

        print(f"   {i+1} |",end="")
        for j in row:
            print(f" {j}",end=" |")
        print(f" {i+1}",end="")
        print()
    print("     -------------")
    for i in range(field_size):
        if i==0:
            print("      ",f"{Alph[i]:4}",end="")
        else:
            print(f"{Alph[i]:4}",end="")

    
    

    
    
   
    
def move_check(field_size,field,direction,player):
    directions={"N":(-1,0),"NE":(-1,1),"NW":(-1,-1),"S":(1,0),"SE":(1,1),"SW":(-1,-1),"W":(0,-1),"E":(0,1)}
    for i in range(field_size):
        for j in range(field_size):
            if field[i][j]==player:
                row_move,column_move=directions[direction]
                row,column=i+row_move,j+column_move
                if field_size>=row>=0 and field_size>=column>=0:
                    field[row][column]=player
                    field[i][j]=" "
                    return True
    return False

def small_stones(field,field_size,location):
    row,col=location[0]-1,location[1].index()
    if 0<=row<=field_size and 0<=col<=field_size:
        field[row][col]="O"
        return True
    else:
        location=input("Player X please enter the location where you want to place a small stone (like 1A)")
def winning_check(field_size,field,players,directions):
    for i in range(field_size):
        for j in range(field_size):
            if field[i][j]==player:
                for a,b in directions:
                    row,col=i+a,j+b
                    if field[row][col]=="O" and 0<=row<=field_size and 0<=col<=field_size:
                        return True
                        
    return False
                


def main():
    
    players = [input("Enter a capital letter to represent player 1 (except O): "),input("Enter a capital letter to represent player 2 (except O): ")]
    curr=0
    player=players[curr]
    cont="Y"
    while cont=="Y":
        field=[]
        field_size=int(input("Enter the row/column number of the playing field (3,5,7):"))
        for i in range(field_size):
            field.append([" "]*field_size) 
        players[0]=field[0][1]
        players[1]=field[field_size-1][int(field_size/2)]
        display(field_size,field)
        
        direction=input(f"Player {player}, please enter the direction you want to move your own big stone(N,S,E,W,NE,NW,SE,SW)")
        if move_check(field_size,field,direction):
            display(field_size,field)
            location=input("Player X please enter the location where you want to place a small stone (like 1A)")
            small_stones(field,field_size,location)
            if small_stones(field,field_size,location):
                display(field_size,field)
                if winning_check:
                    print(f"{player} won")
                
            else:
                print("This place is full")
        else:
            print("This place is full")
            direction=input(f"Player {player}, please enter the direction you want to move your own big stone(N,S,E,W,NE,NW,SE,SW)")
        
        cont=input("would you like to play again?(Y/N)")
if __name__ == "__main__":
        pass
            



 
