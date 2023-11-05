import random
coins=600
inventory=[]
exp=0
hp=10000

sailed=False
strolled=False


def fightScene():
    global hp,exp
    hp=hp-1500
    exp=exp+1000
    print("You prepare to face wrath from this unrecognizable creature standing on the beach.")
    print("...")
    print("After a tiring fight, you manage to defeat the filthy animal. You have gained 1000 fighting exp. You have lost 1500 health points.")
    print("You go back to the beach from where you started.")
    sea_region()

def Stroll():
    global strolled
    strolled=True
    print("You are walking on the beach and you see a huge figure in the distance. You prepare yourself for a potential fight.")
    print("Options: fight/sneak past/go back : ")
    options=["fight","sneak past","go back"]
    userInput=input()
    while userInput not in options:
        print("Options: fight/sneak past/go back : ")
        userInput=input()
    if userInput == "fight":
        fightScene()
    elif userInput == "sneak past":
        print("You sneak past it skillfully and continue with your stroll.")
        print("There is nothing to explore beyond this region so you go back the way you came from.")
        print("On your way back you see that the creepy figure is missing but you find it's leftover cooked fish. Fish has been added to your inventory.")
        inventory=["fish"]
        introScene()
    elif userInput == "go back":
        introScene()
    else:
        print("Please enter a valid option to progress.")


def sea_region():
    options=["sail","stroll","go back"]
    print("You decide to stay at the beach and explore. You have two options :")
    print("Sailing across the sea to the nearby treasure island, or taking a stroll on the beach to explore.")
    print("Pick between sail/stroll/go back: ")
    userInput=input()
    
    while userInput not in options:
        print("Options: sail/stroll/go back \n")
        userInput=input()
    if userInput == "sail":
        if sailed==False:
            Sail()
        else:
            print("You have already been through this route.")
            sea_region()
    elif userInput == "stroll":
        if strolled==False:
            Stroll()
        else:
            print("You have already been through this route.")
            sea_region()
    elif userInput == "go back":
        introScene()
    else:
        print("Please enter a valid option to progress.")

def Sail():
    global sailed, coins
    coins+=10000
    sailed=True
    print("You decided to travel across the sea and reach the nearest treasure island. You have gained 10000 coins.")
    print("You get back to the beach.")
    introScene()

def forest_region():
    global hp, inventory
    print("You venture further into the forest, and on your path you find some delicious looking fresh apples.")
    print("Do you want to eat them or store them?")
    print("Options eat/store: ")
    userInput=input()
    options=["eat","store"]
    while userInput not in options: 
        print("Options: eat/store")
        userInput = input()
    if userInput == "eat":
        hp=hp-2000
        print("Ahh! Unfortunately the apples were poisonous. You have lost 2000 hp.")
        print("Making your way through the forest, you reach the town.")
        town_region()
    elif userInput == "store":
        inventory.append("apples")
        print("Apples have been added to inventory!")
        print("Making your way through the forest, you reach the town.")
        town_region()
    else:
        print("Please enter a valid option to progress.")


def town_region():
    global hp, inventory, coins, exp
    print("You proceed further into the town. Amidst the sounds of the bustling market you hear two people talking about a new popular betting card game happening in town.")
    print("You think about trying your luck here. The winner gets 10000 coins.")
    print("Do you want to play the minigame? Yes/No: ")
    userInput=input()
    options=["yes","no"]
    while userInput not in options:
        print("Options are yes/no: ")
        userInput=input()
    if userInput == "yes":
        print("This minigame will cost you 600 coins.")
        if coins < 600 :
            print("You currently have "+str(coins)+" coins. You do not have enough coins.")
            print("Would you like to trade something from your inventory? yes/no")
            userInput2=input()
            options2=["yes","no"]
            while userInput2 not in options2:
                print("Options are yes/no: ")
                userInput2=input()
            if userInput2=="yes":
                while len(inventory)!=0:
                    print("You currently have: "+inventory+"\nWhat do you want to trade? Enter item number starting from 0,1,2...:")
                    temp=input()
                    inventory.remove(temp)
                    minigame(coins)
                print("No items in inventory :( looks like you cannot play the minigame!")

            elif userInput2 == "no":
                exit
            else: 
                print("Please enter valid response!")
        else :
            minigame(coins)
    elif userInput == "no":
        exit
    else:
        print("Please enter valid response!")

    print("You make your way through the town and finally reach a palace. Some strange noises come from inside the palace and you recognise it to be your beloved sibling's screams.")
    print("After a short unwelcoming encounter with the palace guards, you rush into the palace grounds and look for your sister. She is being held captive in a cage.")
    print("You decide to : 1)Straightforward attack or 2)Sneak up attack? : ")
    userInput3=input()
    options3=["1","2"]
    while userInput3 not in options3:
        print("Options are 1 or 2: ")
        userInput3=input()
    if userInput3 == "1":
        hp=hp-2000
        print("You barge in to save your sibling unknowing that the cage was guarded by a monstrous fire breathing bird. You have lost 2000 HP")
        print("...")
        print("After a tiring fight, you manage to defeat the monstrous creature and save your sister.")
        print("Good job "+name+"! You have successfully made it through this journey. Congratulations on saving your sister! This is where this journey ends.")
    
    elif userInput3 == "2":
        print("You slowly sneak up to the cage, but alas you were too slow traveller! The monster guarding the cage has captured you too. Unfortunately you have no way out of here.")
        print("Better luck on your next journey!")

    exit()


def minigame(coins):
    while coins >= 600:
        coins=coins-600
        num = random.randrange(10)
        print(num)
        
        if num % 2 == 0:
            coins += 10000
            print("Congrats! You have won 10,000 coins!")
        else:
            print("Oh no! You lost.")
        
        print("You have " + str(coins) + " coins left. Would you like to try your luck again? (yes/no): ")
        userInput = input()
        
        while userInput not in ["yes", "no"]:
            print("Options: yes/no: ")
            userInput = input()

        if userInput == "no":
            break 

    print("Aw, you don't have enough coins to continue playing this game!")


def introScene():
    print("You closely examine your surroundings and conclude that there are three ways to go:")
    print("Left : The monstrous sea  Right: Lush green forest   Forward: Nearby town")
    directions = ["left", "right", "forward"]
    userInput = input()
    while userInput not in directions:
        print("Options: left/right/forward")
        userInput = input()
    if userInput == "left":
        sea_region()
    elif userInput == "right":
        forest_region()
    elif userInput == "forward":
        town_region()
    else: 
        print("Please enter a valid option to progress.")

if __name__ == "__main__":
    while True:
        print("Welcome to Teyvat Chronicles: The Elemental Odyssey!")
        print("As an enigmatic traveler who has lost all your memories, you have found yourself stranded at the beach.")
        print("You look around to find your travel partner, also your sister, who seems to be missing.")
        print("However, you remember the unique battling abilites you have and decide to make your way through this new adventure of finding your treasured sibling.")
        print("You can choose to walk in multiple directions to find a way out.")
        print("Let's start with your name: ")
        name = input()
        print("Good luck, " +name+ ".")
        introScene()


def display():
    print("To display your hp, exp, coins and inventory select the folowing resectively.")
    print("hp: h\nexp: e\ncoins: c\ninventory: i\nexit: x")
    userInput=input()
    options=["h","e","c","i","x"]
    while userInput !="x":
        print("Options: h,e,c,i")
        userInput=input()
        if userInput == "h":
            print("hp="+hp)
        elif userInput == "e":
            print("exp="+exp)
        elif userInput == "c":
            print("coins="+coins)
        elif userInput == "i":
            print("inventory="+inventory)   
        elif userInput == "x":
            break
        else:
            print("Please enter a valid option to progress.")



