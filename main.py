import monsters, events
from random import randint, choice


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

"""
CurrentRoom = [x,y]
Rooms[x,y]
options = [N,S,E,W]

if x == 0:
    remove option for west
elif x == 4:
    remove option for east
if y == 0:
    remove option for north
elif y == 4:
    remove option for south


for dir in options:

"""





Keys = 0
#if keys = 5:
# bossroom is unlocked

Inventory = []
# health regeneration
# can be found randomly
# one time strength potion

# new weapon / equipment - bonus atk/defense
# equipped when you get them


PlayerStats = [100,10,10] # HP, Def, Atk
MonsterStats = [40,5,15]

# combat - attack / defend /prepare


# if you attack and monster attacks - just deal damage = atk
# if you attack and monster defends - your atk - monster defense
# if you attack and monster does nothing -atk goes through
# if you defend and monster attacks - monster atk - your defense
# if you prepare - double dmg next turn

# prompt what the monster is doing next time - item locked?
# hardcode crit chance


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




#print(Rooms[0][4])

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
    print("You awaken in a dark room, you see a tile ahead of you....")

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
        print("You can't go that way")
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

    PrintGrid()

def PrintGrid():
    for i in range(len(Rooms)):
        print(Rooms[i])


# def GameLoop():
#     if Keys == 5:
#         SpawnBoss()


Start()

Directions = ["West", "East", "South", "North"]

CurrentDescription = "You stand in the room where you awoke"
while True:
    print(Rooms[x][y])
    print(Rooms[PastCoords[0]][PastCoords[1]])
    PrintGrid()
    print(f"""
{CurrentDescription}

Which direction do you go?
1. North
2. South
3. East
4. West""")
    #print (x,y)
    array = Move(Directions[int(input(">"))-1],x,y)
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