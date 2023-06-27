from random import randint, choice
from math import ceil

stats = [100,10,20]
mobstats = [50,10,20]


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

    defscaling = 1.5

    preparing = False

    while PHealth != 0 or EHealth !=0:

        MonDoNothingChance = 0.95
        MonChoice = randint(1,100)

        critical=randint(0,100)
        if critical > 95:
            Crit = True

        if MonChoice/100 >= MonDoNothingChance: # do nothing
            print(choice(Nothing))
            MonChoice = "nothing"


        elif MonChoice%2: # attack
            print(choice(Attacking))
            MonChoice = "attacking"


        else: # defend
            print(choice(Defending))
            MonChoice = "defending"



        valid = False

        while not valid and not preparing:
            print("""
Choose your move
1. Attack
2. Defend
3. Charge a strong attack""")
            try:
                Choice = int(input(">"))
                if Choice not in [1, 2, 3]:
                    print("Please pick a proper action with 1, 2 or 3")
                    continue

                else:
                    valid = True

            except KeyboardInterrupt:
                quit()

            except:
                print("Please pick a proper action with 1, 2 or 3")
                pass

        MonDamage = 0
        Crit = False
        if Choice == 1:
            print("You charge forwards with sword in hand, slashing at the monster")
            critical=randint(1,100)
            if critical > 95:
                Crit = True
                print("You strike the monster at its weak point, dealing more damage than usual!")

            if MonChoice != "defending":
                Damage = PAtk

            else:
                Damage = ceil(PAtk-EDef/defscaling)


            if Crit:
                Damage*=2

            EHealth -= Damage

            if EHealth <=0:
                Result = "Win"
                break

            if MonChoice == "attacking":
                MonDamage = EAtk
            print(f"You deal {Damage} damage. The enemy has {EHealth}HP left.")


        if Choice == 2:
            print("You raise your shield, bracing yourself")
            if MonChoice in ["defending", "nothing"]:
                print("You and the monster stare at eachother for a second before resuming your fight")

            else:
                MonDamage = round(EAtk - PDef/defscaling)

        if Choice == 3:


            if not preparing:
                preparing = True
                print("You ready your sword, waiting for an opportune moment to strike")
                continue

            elif preparing:
                print("You find your moment to strike")
                Damage = PAtk*2

                crit = randint(1,100)
                if crit > 95:
                    Damage*=2
                    print("You strike the monster at its weakest point, dealing more damage than usual!")

                EHealth -= Damage

                if EHealth <=0:
                    Result = "Win"
                    break

                if MonChoice == "attacking":
                    MonDamage = EAtk
                print(f"You deal {Damage} damage. The enemy has {EHealth}HP left.")

                preparing = False
                continue

        PHealth-=MonDamage
        if PHealth <=0:
            Result = "Lose"
            break

        print(f"The monster deals {MonDamage} damage to you. You have {PHealth}HP left.")


    if Result == "Win":
        print("The monster falls to the ground defeated")

    else:
        print("The monster strikes you in the head.\n\nYour vision fades to black...")



    return Result


Combat(stats,mobstats)