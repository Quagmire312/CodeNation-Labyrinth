"""
Minotaur

4 more monsters
boss
"""

def Monster1():
    #description, stats, fight, item drops? - keys for boss room
    # spider
    description = "You enter a room and see a giant enemy spider. It is a menacing arachnid with eight legs, venomous bites, and a talent for spinning intricate webs."
    stats = [50,10,10]
    return stats, description


def Monster2():
    # orc
    description = "You enter a room and see an orc. Orcs are formidable humanoid creatures with greenish-gray skin, sharp teeth, and a penchant for crude weapons like axes and clubs."
    stats = [60,20,10]
    return stats, description

def Monster3():
    # skeleton
    description = "You enter a room and see a skeleton, the animated remains of the deceased, roam dungeons with their skeletal frames clad in tattered armor, relentlessly attacking intruders."
    stats = [40,20,20]
    return stats, description

def Monster4():
    # minotaur
    description = "You enter a room and see a minotaur, with the head of a bull atop a muscular humanoid body, it possesses immense strength and guards ancient treasures in labyrinthine dungeons." 
    stats = [50,25,25]
    return stats, description

def Monster5():
    # troll
    description = "You enter a room and see a giant trolls, hulking creatures with tough skin and regenerative abilities. It poses a significant threat with their lumbering gait and powerful blows."
    stats = [70,25,20]
    return stats, description

def Boss():
    description = """
You enter the room and find yourself stand before the fearsome dragon, its massive wings spread wide and its fiery breath lighting up the room.
This ancient creature radiates power and danger, its scales shimmering in shades of black and crimson.
Prepare yourself for the ultimate battle against the legendary dragon!
    """
    stats = [100,30,30]
    return stats, description