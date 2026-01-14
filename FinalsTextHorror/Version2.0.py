import dialogue as d
import Dictindict as dict
from functions import *
import random

print("")

name = ""
CurrentDialogue = "Entrance"
CurrentLocation = "siloA"
inventory = []
textspeed = 0.02

answers = ["write", "don't"]
cevaplar = ["open", "nope"]
boom = ["destroy", "NOO"]
danger = ["attack", "run"]
TrueCode = "She sells sea shells on a sea shore"
takeable = ["core-key", "lever"]

MonsterLocation = "control-panel"
MonsterRooms = ["corridorA", "corridorB", "corridorC", "port", "control-panel", "bedroomA", "bedroomB", "archive"]

# THE start of THE game

slow_print("You are an astronaut named...?", textspeed)
name = input(">")
print("Yes, your name is ", name, ", you are in a spaceship going to mars for research")

TalkFunc(d.d1, CurrentDialogue)

while True:
    print("You are in the", CurrentLocation)

    MonsterLocation = random.choice(MonsterRooms) # monster moves trough went or something idk
    # print(MonsterLocation)

    if CurrentLocation == MonsterLocation:
        encountered = True
        slow_print("You encountered the monster!")
        slow_print("Think fast [attack, run]")
        instinct = validInput(danger)
        if instinct == "attack":
            if "shotgun" in inventory:
                slow_print("You shot the monster, it stopped moving")
                slow_print("You WONNNNNNN!!!!!!!")
                break
            elif "shotgun" and "lever" in inventory:
                slow_print("You shot the monster, it stopped moving")
                slow_print("You WONNNNNNN!!!!!!!")
                break
            elif "lever" in inventory and "shotgun" not in inventory:
                slow_print("You throw your lever to the monster, it got scared and run away")
                slow_print("You lost your lever in the process")

                placeHolder = MonsterLocation
                MonsterRooms.remove(MonsterLocation)
                MonsterLocation = random.choice(MonsterRooms)
                MonsterRooms.append(placeHolder)
            else:
                slow_print("You attacked THE MONSTER with your fists")
                slow_print("You were a brave soul. But also a little dumb")
                slow_print("You died")
                break
        else:
            slow_print("Which direction???")
            where = input(">")
            if where in Dictindict.rooms[CurrentLocation] and where != "item" and where != "Options":
                yönüm = Dictindict.rooms[CurrentLocation][where]
                nextRoom = Dictindict.rooms.get(yönüm)

                isLocked = nextRoom.get("locked", False)

                if isLocked:
                    slow_print("The door was locked, you wasted your chance")
                    slow_print("You died")
                    break
                else:
                    CurrentLocation = Dictindict.rooms[CurrentLocation][where]
                    skipped = True
            else:
                slow_print("You ran into a wall, and the monster caught you")
                slow_print("You died")
                break
    else:
        slow_print("You hear loud noises from another room")

    if skipped == True:
        pass
    else:
        TalkFunc(dict.rooms, CurrentLocation) # i will write something for them all # i did
        slow_print("What do you want to do?", textspeed)
        action = input(">")
        actionList = action.split(" ", 1) # splits every word of the user

    if actionList[0] == "go":
        direction = actionList[1]
        if direction in Dictindict.rooms[CurrentLocation] and direction != "item" and direction != "Options": # make sure i don't go to "items"
            yönüm = Dictindict.rooms[CurrentLocation][direction]
            nextRoom = Dictindict.rooms.get(yönüm)

            isLocked = nextRoom.get("locked", False)

            if isLocked:
                if yönüm == "corridorA":
                    TalkFunc(d.d2, CurrentDialogue)
                    answer = validInput(answers)
                    if answer == "write":
                        slow_print("Okay... go for it", textspeed)
                        code = input(">")
                        if code == TrueCode:
                            slow_print("You opened the door!", textspeed)
                            Dictindict.rooms["corridorA"]["locked"] = False
                            CurrentLocation = "corridorA"
                        else:
                            slow_print("Noooo, wrong code. Maybe next time", textspeed)
                    else:
                        pass
                elif yönüm == "core":
                    if "core-key" in inventory:
                        slow_print("If you enter the core, you can explode this whole ship and kill the monster")
                        slow_print("Are you willing to do it?")
                        bom = validInput(boom)
                        if bom == "destroy":
                            slow_print("You killed everyone")
                            break
                        else:
                            pass
                    else:
                        slow_print("This door requires a key to open", textspeed)
                else:
                    slow_print("This door is locked", textspeed)
            else:
                CurrentLocation = Dictindict.rooms[CurrentLocation][direction]
                print("You move to", CurrentLocation)
        else:
            print("There are no doors in that direction.")

    if actionList[0] == "int":
        targetItem = actionList[1]
        if "item" in dict.rooms[CurrentLocation]:
            if targetItem in dict.rooms[CurrentLocation]["item"]:
                if targetItem in takeable:
                    print("Picked up", targetItem)
                    inventory.append(targetItem)
                    dict.rooms[CurrentLocation]["item"].remove(targetItem)
                    youGonnaGo = dict.rooms[CurrentLocation]["Lines"][2]
                    dict.rooms[CurrentLocation]["Lines"].remove(youGonnaGo)
                    print(inventory)
                elif targetItem == "panel":
                    slow_print("Do you wanna open the doors of archive and corridorA?", textspeed)
                    slow_print("[open, nope]", textspeed)
                    cevap = validInput(cevaplar)
                    if cevap == "open":
                        slow_print("You opened the doors!", textspeed)
                        Dictindict.rooms["archive"]["locked"] = False
                        Dictindict.rooms["corridorC"]["locked"] = False
                        youGonnaGo = dict.rooms[CurrentLocation]["Lines"][1]
                        dict.rooms[CurrentLocation]["Lines"].remove(youGonnaGo)
                    else:
                        slow_print("okay", textspeed)
                elif targetItem == "bed":
                    slow_print("You carefully checked under the bed...", textspeed)
                    slow_print("It's the captain! he is injured!", textspeed)
                    slow_print(f"-{name}, is that you? Eheheh, At least you are still alive", textspeed)
                    choice = TalkFunc(d.d3, CurrentDialogue)
                    if choice == "I want to kill that monster!":
                        inventory.append("wardrobe-key")
                    else:
                        inventory.append("ship-key")
                        Dictindict.rooms["escape-rocket"]["locked"] = False
                    print(inventory)
                elif targetItem == "wardrobe":
                    if "wardrobe-key" in inventory:
                        slow_print("You opened the wardrobe and took the shotgun")
                    else:
                        slow_print("You can't open the wardrobe")
            else:
                print("There is no", targetItem)
        else:
            print("There are no items in this room.")

    if CurrentLocation == "escape-rocket":
        break
    elif CurrentLocation == "core":
        break