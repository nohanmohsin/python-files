#os module for clearing the screen after input
import os

#====GLOBAL VARIABLES====

#cordinates variable of player1 
coordinates1=[]
#cordinates variable of player2
coordinates2=[]
#mine fields variable for player1
mine_location_for_player1=[]
#mine fields variable for player2
mine_location_for_player2=[]
#attacking coordinates of player 1
attacking_coordinates1=[]
# attacking coordinates of player 2
attacking_coordinates2=[]
#points variable of player1
points_of_player1=0
#points variable of player2
points_of_player2=0

#points variable for game for player1
game_wins1=0
#points variable for game for player2
game_wins2=0

#====END OF GLOBAL VARIABLES====

#start of functions

#function combining all the functions a then inintializig it
def play_game():

    start_menu()
    enter_coordinates()
    mine_fields()
    take_attack_input_and_count_points()
    check_wins()
     
        
#start of the game

def start_menu():
    #acknowledging the player that the game has started 
    print("HELLO PLAYERS")
    #RULES OF THE GAME
    print("""
    THE RULES OF THE GAME
  YOU CAN ENTER COORDINATES FROM 0 - 10
  YOU CAN ENTER COORDINATES FOR 5 SHIPS
  THEN YOU HAVE TO ENTER ATTACKING COORDINATES 
  IF YOUR ATTACKING COORDINATES MATCH THE OPPONENT'S SHIP COORDINATES YOU GET A POINT
  MAX POINT IS 5
  AFTER YOU ENTER THE COORDINATES FOR THE FIVE SHIPS THE OTHER FIVE NUMBERS WILL BE THE COORDINATES FOR THE MINES
  IF YOUR  ATTACKING COORDINATES MATCH TO YOUR OPPONENT'S MINE FIELD COORDINATES THAN 1 POINT WILL BE DEDUCTED FROM YOU 
    """)
    
    

#coordinates of the ships

def enter_coordinates():
    #global variables needed in this function are written below
    global coordinates1
    global coordinates2
  
    #checking for more than 2 same elements in the to coordinates
    def duplicate_checking(list_parm):
      for elem in list_parm:
         if list_parm.count(elem) > 2:
             return True
      return False 

    #player1's coordinates
    print("PLEASE ENTER THE COORDINATES FOR YOUR FIVE SHIPS PLAYER1")
    #taking input of the coordinates of player 1
    valid1=True
    
    while  valid1 :
    #taking the input in a variable and adding to coordinates1
     coor=int(input())
     coordinates1.append(coor)
     #checking for duplicates
     result_checking1=duplicate_checking(coordinates1)
     
     if result_checking1==True :
         valid1=True
         coordinates1.pop(-1)
         
         print("you cant enter three same coordinates")
     elif coor not in range (0,11):
         valid1=True
         coordinates1.pop(-1)

         print("invalid input.TRY AGAIN!!!")
   

     #exiting the while loop and clearing the screen
     if len(coordinates1)==5:
          print ("you have entered all of your coordinates")
          
          os.system('cls')
          break
    #player2's coordinates
    
    print("NOW ENTER YOUR COORDINATES OF THE SHIPS PLAYER2")
    #taking input of the coordinates of player 2
    valid2=True

    while  valid2 :
       #taking the input in a variable and adding to coordinates2
     coor2=int(input())
     coordinates2.append(coor2)
     #checking for duplicates
     result_checking2=duplicate_checking(coordinates2)
     
     if result_checking2==True :
         valid2=True
         coordinates2.pop(-1)
         
         print("you cant enter three same coordinates")
     elif coor2<0:
         valid2=True
         coordinates2.pop(-1)

         print("you cant enter negative coordinates ")
     #checking if input is bigger than 5
     elif coor2>10:
         valid2=True

         coordinates2.pop(-1)

         print("you cant enter a coordinate bigger than 10")

         #exiting the while loop and clearing the screen
     if len(coordinates2)==5:
          print ("you have entered all of your coordinates")
          #clearing the creen after input
          os.system('cls') 
          break
#function for mine fields location
def mine_fields():
    #global variables needed in this function
    global mine_location_for_player1
    global mine_location_for_player2
 #iterating through the coordinates list to find the missing numbers and adding it to the mine_location
    for j in range(10):
        if j not in coordinates1:
            mine_location_for_player1.append(j) 
        if j not in coordinates2:
            mine_location_for_player2.append(j)

#function for taking the attaking coordinates

def take_attack_input_and_count_points():
    #global variables needed in this function
    global attacking_coordinates1
    global attacking_coordinates2
    global points_of_player1
    global points_of_player2
    global mine_location_for_player1
    global mine_location_for_player2

    print("enter the coordinate of your attack player1 ")
 
    avalid1=True
    while avalid1:
     #variable to take input 
     attack_coor1=int(input())
     
     if attack_coor1<=10:
         #checking if input is valid and adding it to the list
         attacking_coordinates1.append(attack_coor1)
     
        


         #adding the points of player1
     
         if attack_coor1 in coordinates2:
             #adding the points if met condition
             points_of_player1+=1
             #achknowledging the player
             print("you got one")
             #checking if player hit mine 
         elif attack_coor1 in mine_location_for_player1:
             #subtracting a point if condition is met
             points_of_player1-=1
             #achknowledging the player
             print("you hit a mine")
         #checking if player gave negative coordinates
         elif attack_coor1<0:
             avalid1=True
             print("you cant enter negative coordinates")
         #checking if player gave coordinates bigger than 10
         elif attack_coor1>10:
             avalid1=True
             print("you cant enter coordinates bigger than 10 ")
            
        


     #breaking out of the loop
     if len(attacking_coordinates1)==5:
         print("you have entered all your attacks")
         
         avalid1=False


    print("enter your attack coordinations player2")
    if avalid1==False:
        avalid2=True
        while avalid2:
            #variable to take input 
            attack_coor2=int(input())
            #checking if input is valid and adding it to the list
            if attack_coor2<=10:
                attacking_coordinates2.append(attack_coor2)
            #adding the points of player2
            if attack_coor2 in coordinates1:
                #adding the points if met condition
                points_of_player2+=1
                #achknowledging the player
                print("you got one")
            elif attack_coor1 in mine_location_for_player1:
             #subtracting a point if condition is met
             points_of_player1-=1
             #achknowledging the player
             print("you hit a mine")       
            elif attack_coor2<0:
             avalid2=True
             print("you cant enter negative coordinates")
         #checking if player gave coordinates bigger than 10
            elif attack_coor2>10:
             avalid2=True
             print("you cant enter coordinates bigger than 10 ")
            
     
            if len(attacking_coordinates2)==5:
                print("you have entered all your attacks")
         
                print("PLAYER 1 GOT"+ str(points_of_player1))
                print("PLAYER 2 GOT"+str(points_of_player2))
                avalid2=False

    

def check_wins():
    #global variables needed in this function
    global game_wins1
    global game_wins2
    if points_of_player1>points_of_player2:
        print("PLAYER 1 WON THE GAME ")
        game_wins1+=1
    elif points_of_player2>points_of_player1:
        print("PLAYER 2 WON THE GAME")
        game_wins2+=1
    
    

    

#varible for ending the game
determiner_for_end=True
while  determiner_for_end:
 #vaiable to take input to start the game 
 game_starter=input ("do you want to start the game then enter yes")
 if game_starter=="yes":
     play_game()
     #take input if user wants to end the game
     end_game_input=input("if you want to end the game then press y and then enter key")
     if end_game_input=='y':
         if game_wins1==game_wins2:
             print("IT WAS A TIE!!")
         elif game_wins1>game_wins2:
             print('the game was won by player1' )
         elif game_wins2>game_wins1:
             print("the game was won by player2")
         print()
         break 