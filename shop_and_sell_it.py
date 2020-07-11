#shops to buy from
shop_list=["shaufiq store","saraz store","karim store","sakil store"]
#list to take input on which store NAME player chooses
shop_decider_list=["shaufiq","saraz","karim","sakil"]
#variable for initial budget
budget= 500
#global variable to store the bought items and quantities
shoping_list={}
#selling item prices
sell_list={"ram":22,"i3":13,"i5":17,"graphics card":25,"cpu cooler":20,"monitors":21,"mouse":8,"keyboard":9}
return_points=0

f1=open('gamedata','a')
f2=open('gamedata','r')
#class for shoping in the shaufiq store
class shaufiq:
    def __init__(self):
        self.shaufiq_store={"ram":[10,20],"i3":[14,13],"i5":[16,16]}
        
    #method to take input on shop for shaufiq class
    def take_input_for_shooping(self):

        print(self.shaufiq_store)
        def goto_outer_layer():
            #budget variable to modify it
            global budget
            global shoping_list
            #get the item names in a list
            item_names=sorted(self.shaufiq_store.keys())
            
            validity_check=True
            #while loop to keep checking the name if it isn't valid
            while validity_check:
                #take input to for player to buy items
                input_taker=input("enter the item_name to purchase it ")


                
                #checking if item name is valid
                if input_taker in item_names:

                    if input_taker in shoping_list.keys():
                        print("you cant have two same products dumbasss")
                        continue
                    #checking if input is valid and checking the stock         
                    stock_checking=True
                    while stock_checking:

                        #taking input on the amount of the product
                        take_amount =input("how many of this item do you need")

                        #checking if input is valid
                        if take_amount.isdigit():
                            #turning take_amount to an int
                            take_amount=int(take_amount)

                            # checking if take amount is smaller or equal to the stock of the item 
                            if take_amount <= self.shaufiq_store[input_taker][0]:
                                #subtracting the amount from the store
                                self.shaufiq_store[input_taker][0]=self.shaufiq_store[input_taker][0]-take_amount
                                #subtracting the money
                                budget=budget-self.shaufiq_store[input_taker][1]*take_amount
                                print("your budget is now",str(budget))
                                #shoping list is bought items and quantity
                                shoping_list[input_taker]=take_amount
                                print(shoping_list)
                                #breaking out of the 
                                if len(shoping_list)==2:
                                    print("you have reached the limit")
                                    
                                else:
                                    goto_outer_layer()
                                
                                break
                               
                                
                                                                    
                            #else telling the player
                            else:
                                print("insufficient amount")
                                stock_checking=True
                                continue
                            
                        
                        # if amount input is then continuing the the stock_checking loop      
                        else:
                            print("invalid type of input")
                            continue
                    #beaking out of the validity check loop
                    validity_check=False
                        

                #else achknoweledging the player
                else:
                    print("invalid name")
                    continue
                break
        
        goto_outer_layer()

    
       




        
#class for saraz store
class saraz(shaufiq):
    #products of saraz store 
    def __init__(self):
        shaufiq.__init__(self)
        self.saraz_store={"mouse":[27,5],"keyboard":[13,7],"monitors":[20,13]}
        self.shaufiq_store=self.saraz_store
        
        
# class for karim store  
class karim(shaufiq):
    def __init__(self):
        shaufiq.__init__(self)
        self.karim_store ={"graphics card":[8,16],"ram":[15,23],"monitors":[17,15]}
        self.shaufiq_store=self.karim_store       


  
#class for sakil store
class sakil(shaufiq):
    def __init__(self) :
        shaufiq.__init__(self)
        self.sakil_store={"graphics card":[9,17],"headphones":[10,11],"cpu cooler":[15,17]}
        self.shaufiq_store=self.sakil_store        

class shaufiq_sell(shaufiq):
    def __init__(self):
        print("you have bought")
        print(shoping_list)
        shaufiq.__init__(self)



        
    #method to take input for selling the items to the store
    def take_input_for_selling(self):
        for items in self.shaufiq_store.keys():
            #checking if duplicate is found in shoping list
            if items in shoping_list.keys():
                shoping_list.pop(items)

                #checking if duplicate is found
                if len(shoping_list)==1:
                    #if the for loop is true 
                    # then searching for duplicate item in th other shoped item
                    for items2 in self.shaufiq_store.keys():
                        if items2 in shoping_list.keys():
                            shoping_list.pop(items2)
                            break


                    #if duplicate not found in second then pass the if else statement       
                    else:
                        pass
                    #break out of the for loop
                    break 
        def goto_outer_loop():
            #global variable budget to modify it
            global budget
            #global variable sell_list to check item price
            global sell_list
            global return_points
            if len(shoping_list)>=1:
                validity_check=True
                while validity_check:

                    take_input_for_sellings=input("enter the item to sell")
                    #checking if input item is in the shoping list
                    if take_input_for_sellings in shoping_list.keys():
                        #if true then asking for the amount

                        stock_checking=True
                        while stock_checking:
                            sell_amount=input("now enter the amount of how much you want to sell")
                            #checking the type of the sell_amount
                            if sell_amount.isdigit():
                                sell_amount=int(sell_amount)
                                #check if amount is in range or not
                                if sell_amount<=shoping_list[take_input_for_sellings]:
                                    #then subtracting the quantity from the shoping_list item
                                    shoping_list[take_input_for_sellings]=shoping_list[take_input_for_sellings]-sell_amount
                                    #checking if stock of the item is out
                                    if shoping_list[take_input_for_sellings]==0:
                                        #if true then poping the item out
                                        shoping_list.pop(take_input_for_sellings)
                                    else:
                                        pass
                                    #adding the money 
                                    budget+=sell_list[take_input_for_sellings]*sell_amount
                                    print("your budget is now ",str(budget))
                                    if return_points>2 :
                                        break
                                    if len(shoping_list)!=0:
                                        exit_decider=input("do you want to sell another item than enter y else enter anything but y ")
                                        
                                    else:
                                        break
                                    if exit_decider=="y" and return_points<2:
                                        return_points+=3
                                        
                                        #asking the player again
                                        goto_outer_loop()
                                        return_points=0
                                        break
                                    else:
                                        break
                                #if out of range than staring the loop again 
                                else:
                                    print("amount is out of range")
                                    stock_checking=True
                            #if not integer printing invalid input and starting the loop again
                            else:
                                print("invalid type of input")
                                stock_checking=True
                        validity_check=False                           
                    

                    #if item not in shoping_list then starting the loop again and telling the player
                    else:
                        print("you do not have this item in your shoping list")
                        validity_check=True
                    
            
            else:
                print("you have lost all your items")
                
        goto_outer_loop()



class saraz_sell(saraz,shaufiq_sell):
    def __init__(self):
        saraz.__init__(self)
        shaufiq_sell.__init__(self)
        self.shaufiq_store=self.saraz_store


class karim_sell(karim,shaufiq_sell):
    def __init__(self):
        karim.__init__(self)
        shaufiq_sell.__init__(self)
        self.shaufiq_store=self.karim_store
 

class sakil_sell(sakil,shaufiq_sell):
    def __init__(self):
        sakil.__init__(self)
        shaufiq_sell.__init__(self)
        self.shaufiq_store=self.sakil_store
      
        

def play_game():
    #the game has started
    print("hello player")
    print("BELOW YOU HAVE THE SHOPS")
    print(shop_list)
    #variable to keep checking name 
    validity_check=True
    #while loop to keep checking the name if it isn't valid
    while validity_check:
        #variable to take input to check which store to buy from
        shop_decider=input("ENTER THE SHOP NAME YOU WANT TO BUY FROM") 
        print("on the left side of the list is the available shop")
        print("on the right hand side you shall find the rice of the item")
        #checking which class the shop object should have
        if shop_decider  in shop_decider_list:
            if shop_decider=="shaufiq":
                shop=shaufiq()
            elif shop_decider=="saraz":
                shop=saraz()
            elif shop_decider=="karim":
                shop=karim()
            elif shop_decider=="sakil":
                shop=sakil()
        
            shop.take_input_for_shooping()
            #braking out of the loop after its work is done
            break
        #checking if name is invalid and starting the loop again 
        else:
            print("invalid name")
            validity_check=True
    
    while True:
        #variable to take on which shop does the user want to buy from a shop
        sell_decider=input("now enter the shop you want to sell to")
        #checking if sell decider has a valid name        
        if sell_decider in shop_decider_list and sell_decider!=shop_decider:
            
            #checking which class the sell object should have 
            if sell_decider=="shaufiq":
                sell=shaufiq_sell()
            elif sell_decider=="saraz":
                sell=saraz_sell()
            elif sell_decider=="karim":
                sell=karim_sell()
            elif sell_decider=="sakil":
                sell=sakil_sell()
            sell.take_input_for_selling()
        #else asking again
        else:
            print("invalid name")
            #asking for the name again
            continue
        #ending the loop after its work is done
        break
for i in range(7):          
    play_game()
if budget>=1000:
    print("you have won the game")
    f1.write("")   
    f1.write("WIN !!!")
    

else:
    f1.write()
    f1.write("LOSE")
    print("you lost the game")
print("do you want to see the record")
record_checker=input("then enter y else enter anything")
if record_checker=='y':
    print(f2.read())

        
