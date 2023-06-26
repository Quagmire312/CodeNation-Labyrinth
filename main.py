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

CurrentCoords = []

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
    Monster1 = []
    Monster2 = []
    Monster3 = []
    Monster4 = []
    Monster5 = []
    #Boss = []

DropChance = 0.5
HealthChance = 0.8 # otherwise strength

#spawn boss once all enemies are defeated

def SpawnEvents():
    Event1 = []
    Event2 = []
    Event3 = []

#print(Rooms[0][4])

def SpawnItems(): # 5 items - potions
    pass


def SpawnBoss():
    Boss = []


EmptyRoomDescriptions = ["There is nothing in this room", "You look closely at the corners, but only find cobwebs", "..."]
# random descriptions

def Lore():
    print("You awaken in a dark room, you see a tile ahead of you....")

def GameLoop():
    if Keys == 5:
        SpawnBoss()