import monsters, events
from random import randint, choice
from time import sleep as s
from math import ceil

# for i in range(5):
#     Rooms.append([])
#     for ii in range(5):
#         Rooms[i].append([])

Rooms = [
    [[],[],[],[],[]],
    [[],[],[],[],[]],
    [[],[],[],[],[]],
    [[],[],[],[],[]],
    [[],[],[],[],[]]
]

def Print2(text):
    for char in text:
        print(char,end="",flush = True)
        s(0.01)
    print()



Keys = 0
#if keys = 5:
# bossroom is unlocked

Inventory = ["Health Potion"]
# health regeneration
# can be found randomly
# one time strength potion

# new weapon / equipment - bonus atk/defense
# equipped when you get them


PlayerStats = [100,10,10] # HP, Def, Atk
MonsterStats = [40,5,15]

# combat - attack / defend / prepare
# monster - attack, defend, do nothing

# if you attack and monster attacks - just deal damage = atk
# if you attack and monster defends - your atk - monster defense
# if you attack and monster does nothing -atk goes through
# if you defend and monster attacks - monster atk - your defense
# if you prepare - double dmg next turn

# prompt what the monster is doing next time - item locked?
# hardcode crit chance

Nothing = ["The monster is loafing around", "The monster gets lost in your eyes", "The monster starts tying its shoelaces"]
Attacking = ["The monster prepares to attack", "The monster readies itself to strike"]
Defending = ["The monster takes a defensive stance", "The monster steadies itself"]

def Combat(Stats,MobStats):
    PHealth = Stats[0]
    PDef = Stats[1]
    PAtk = Stats[2]
    EHealth = MobStats[0]
    EDef=MobStats[1]
    EAtk=MobStats[2]

    defscaling = 2

    preparing = False

    while PHealth != 0 or EHealth !=0:

        MonDoNothingChance = 0.95
        MonChoice = randint(1,100)

        critical=randint(0,100)
        if critical > 95:
            Crit = True

        if MonChoice/100 >= MonDoNothingChance: # do nothing
            Print2(choice(Nothing))
            MonChoice = "nothing"


        elif MonChoice%8 == 0: # defends
            Print2(choice(Defending))
            MonChoice = "defending"


        else: # attack
            Print2(choice(Attacking))
            MonChoice = "attacking"



        valid = False

        while not valid and not preparing:
            Print2("""
Choose your move
1. Attack
2. Defend
3. Charge a strong attack""")
            try:
                Choice = int(input(">"))
                if Choice not in [1, 2, 3]:
                    Print2("Please pick a proper action with 1, 2 or 3")
                    continue

                else:
                    valid = True

            except KeyboardInterrupt:
                quit()

            except:
                Print2("Please pick a proper action with 1, 2 or 3")
                pass

        MonDamage = 0
        Crit = False

        critical = randint(1,100)
        if critical > 95:
            Crit = True
        if Choice == 1:
            Print2("You charge forwards with sword in hand, slashing at the monster")



            if MonChoice != "defending":
                Damage = PAtk

            else:
                Damage = ceil(PAtk-EDef/defscaling)


            if Crit:
                Damage*=2
                Print2("You strike the monster at its weak point, dealing more damage than usual!")

            EHealth -= Damage

            if EHealth <=0:
                Result = "Win"
                break

            if MonChoice == "attacking":
                MonDamage = EAtk
            Print2(f"You deal {Damage} damage. The enemy has {EHealth}HP left.")


        if Choice == 2:
            Print2("You raise your shield, bracing yourself")
            if MonChoice in ["defending", "nothing"]:
                Print2("You and the monster stare at eachother for a second before resuming your fight")

            else:
                MonDamage = round(EAtk - PDef/defscaling)

            if Crit:
                MonDamage/=2
                print("You block the enemies attack perfectly, deflecting most of the damage")

        if Choice == 3:

            if not preparing:
                preparing = True
                print("You ready your sword, waiting for an opportune moment to strike")


            elif preparing:
                print("You find your moment to strike")
                Damage = PAtk*2.5

                if Crit:
                    Damage*=2
                    print("You strike the monster at its weakest point, dealing more damage than usual!")

                EHealth -= Damage

                if EHealth <=0:
                    Result = "Win"
                    break

                if MonChoice == "attacking":
                    MonDamage = EAtk*1.5

                print(f"You deal {Damage} damage. The enemy has {EHealth}HP left.")

                preparing = False



        PHealth-=MonDamage
        if PHealth <=0:
            Result = "Lose"
            break

        Print2(f"The monster deals {MonDamage} damage to you. You have {PHealth}HP left.")


    if Result == "Win":
        Print2("The monster falls to the ground defeated")

    else:
        Print2("The monster strikes you in the head.\n\nYour vision fades to black...")



    return Result


def SpawnMonsters():
    global Monster1, Monster2, Monster3, Monster4, Monster5
    Occupied = True

    Monster1 = []

    while Occupied:
        x = randint(0,4)
        y = randint(0,4)
        if Rooms[x][y] == [] and [x,y] != [2,2]:
            Monster1 = [x,y]
            Rooms[x][y] = "Monster 1"
            break


    Monster2 = []

    while Occupied:
        x = randint(0,4)
        y = randint(0,4)
        if Rooms[x][y] == [] and [x,y] != [2,2]:
            Monster1 = [x,y]
            Rooms[x][y] = "Monster 2"
            break


    Monster3 = []

    while Occupied:
        x = randint(0,4)
        y = randint(0,4)
        if Rooms[x][y] == [] and [x,y] != [2,2]:
            Monster1 = [x,y]
            Rooms[x][y] = "Monster 3"
            break


    Monster4 = []

    while Occupied:
        x = randint(0,4)
        y = randint(0,4)
        if Rooms[x][y] == [] and [x,y] != [2,2]:
            Monster1 = [x,y]
            Rooms[x][y] = "Monster 4"
            break


    Monster5 = []

    while Occupied:
        x = randint(0,4)
        y = randint(0,4)
        if Rooms[x][y] == [] and [x,y] != [2,2]:
            Monster1 = [x,y]
            Rooms[x][y] = "Monster 5"
            break


    #Boss = []

DropChance = 0.5
HealthChance = 0.8 # otherwise strength

def DropItem(): 
    rng = randint(1, 100)
    if rng > DropChance * 100:
        rng2 = randint(1,100)
        if rng2 > HealthChance * 100:
            Print2("The enemy drops a health potion!")
            return "Health Potion"
        else:
            Print2("The enemy dropped a strength potion!")
            return "Strength Potion"
    Print2("The enemy drops an empty bottle.")
    return None

#spawn boss once all enemies are defeated

def SpawnEvents():
    global Event1, Event2, Event3
    Occupied = True

    Event1 = []

    while Occupied:
        x = randint(0,4)
        y = randint(0,4)
        if Rooms[x][y] == [] and [x,y] != [2,2]:
            Monster1 = [x,y]
            Rooms[x][y] = "Event 1"
            break


    Event2 = []

    while Occupied:
        x = randint(0,4)
        y = randint(0,4)
        if Rooms[x][y] == [] and [x,y] != [2,2]:
            Monster1 = [x,y]
            Rooms[x][y] = "Event 2"
            break


    Event3 = []

    while Occupied:
        x = randint(0,4)
        y = randint(0,4)
        if Rooms[x][y] == [] and [x,y] != [2,2]:
            Monster1 = [x,y]
            Rooms[x][y] = "Event 3"
            break




#Print2(Rooms[0][4])

def SpawnItems(): # 5 items - potions
    Occupied = True
    for i in range(randint(3,7)):

        RNG = randint(1,100)

        if RNG/100 <= HealthChance:
            while Occupied:
                x = randint(0,4)
                y = randint(0,4)
                if Rooms[x][y] == [] and [x,y] != [2,2]:
                    Monster1 = [x,y]
                    Rooms[x][y] = "Health Potion"
                    break
        else:
            while Occupied:
                x = randint(0,4)
                y = randint(0,4)
                if Rooms[x][y] == [] and [x,y] != [2,2]:
                    Monster1 = [x,y]
                    Rooms[x][y] = "Strength Potion"
                    break


def SpawnBoss():
    global Boss
    Boss = []


EmptyRoomDescriptions = ["There is nothing in this room", "You look closely at the corners, but only find cobwebs", "..."]
# random descriptions

def Lore():
    Print2("You awaken in a dark room, you see a tile ahead of you....")

def Move(direction, x,y):
    NewX = x
    NewY = y
    Stuck = False
    if direction == "North":
        NewY-=1
    elif direction == "South":
        NewY+=1
    elif direction == "West":
        NewX-=1
    else:
        NewX+=1

    if NewX < 0 or NewX > 4 or NewY > 4 or NewY < 0:
        #Print2("You can't go that way")
        NewX = x
        NewY = y
        Stuck = True

    return x,y,NewX,NewY,Stuck


x=2
y=2

CurrentCoords = [x,y]
PastCoords = [x,y]
def Start():
    SpawnMonsters()
    SpawnEvents()
    SpawnItems()
    Lore()
    Rooms[x][y] = "Player"

    Print2Grid()

def Print2Grid():
    for i in range(len(Rooms)):
        Print2(Rooms[i])


# def GameLoop():
#     if Keys == 5:
#         SpawnBoss()


Start()

Directions = ["West", "East", "South", "North"]

CurrentDescription = "You stand in the room where you awoke"
array = (2,2,2,2,False)


GameLoop = True
while GameLoop:
    if Rooms[x][y] != []:
        if "Monster" in Rooms[x][y]:
            # check which monster is in the room
            if Rooms[x][y][-1] == "1":
                MonsterInfo = monsters.Monster1()
            elif Rooms[x][y][-1] == "2":
                MonsterInfo = monsters.Monster2()
            elif Rooms[x][y][-1] == "3":
                MonsterInfo = monsters.Monster3()
            elif Rooms[x][y][-1] == "4":
                MonsterInfo = monsters.Monster4()
            elif Rooms[x][y][-1] == "5":
                MonsterInfo = monsters.Monster5()
            # #retrieve monster information
            MonsterDesc = MonsterInfo[1]
            print(MonsterDesc)

            MonsterStats = MonsterInfo[0]
            if Combat(PlayerStats, MonsterStats) == "Lose":
                quit()
            else:
                Keys+=1
                Rooms[x][y] == "Dead monster"
                Inventory.append(DropItem())
                # itemdrop function needed()

        if "Event" in Rooms[x][y]:
            event = ""
            if Rooms[x][y][-1] == "1":
                event = events.Event1()
            elif Rooms[x][y][-1] == "2":
                event = events.Event2()
            elif Rooms[x][y][-1] == "3":
                event = events.Event3()
            
            if event == "an Orichalcum Sword":
                Print2(f"You found a {event}. You proudly replace your old iron sword with it.")
                PlayerStats[2] += 20
            elif event == "a Titanium Armor":
                Print2(f"You found {event}. You proudly replace your old leather armor with it.")
                PlayerStats[1] += 20
            elif event == "trap":
                Print2("You walked towards the chest looking for new loot. However, the floor open beneath you into a giant pit. You sprained both of your ankles.")
                PlayerStats[0] -= 15

            Rooms[x][y] = []


        # Time to explore
    Print2(Rooms[x][y])
    Print2(Rooms[PastCoords[0]][PastCoords[1]])
    Print2Grid()


    if array[4]:
        Print2("You can't go that way")

    #Print2(f"Health: {PlayerStats[0]} || Attack: {PlayerStats[2]} || Defense: {PlayerStats[1]}")

    Print2(f"""
{CurrentDescription}

Health: {PlayerStats[0]} || Attack: {PlayerStats[2]} || Defense: {PlayerStats[1]}

Which direction do you go?
1. North
2. South
3. East
4. West""")
    # checking inventory / using items
    #Print2 (x,y)
    NotMoved = True
    while NotMoved:
        try:
            array = Move(Directions[int(input(">"))-1],x,y)
            NotMoved = False
        except KeyboardInterrupt:
            quit()
        except:
            Print2("Please input a proper direction using the numbers 1, 2, 3 or 4")
    x = array[2]
    y = array[3]

    if not array[4]:
        PastX = array[0]
        PastY = array[1]

    if Rooms[x][y] == []:
        CurrentDescription = choice(EmptyRoomDescriptions)
    else:
        CurrentDescription = Rooms[x][y]

    PastCoords = [PastX,PastY]