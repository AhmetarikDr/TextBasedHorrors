import dialogue
import time
import Dictindict

#------------------------------

CurrentDialogue = "Entrance"
CurrentLocation = "siloA"

#-------------------------------

def validInput(keyWords):

    valid = False

    while not valid:
        try:
            inp = input(">")
            if not inp in keyWords:
                raise Exception("No keyword found")

        except Exception as ex:
            print(ex)
            print("try again:")

        else:
            valid = True
            return inp

def slow_print(message, delay=0.02):
    for char in message:
        print(char, end = "", flush=True)
        time.sleep(delay)
    print()

def TalkFunc(dno, CurrentDialogue):
    talking = True
    while talking:
        room = dno.get(CurrentDialogue)
        lines = room.get("Lines")
        for l in lines:
            slow_print(l, 0.02)
        options = room.get("Options")
        if options == []:
            talking = False # finish
        elif options == None:
            talking = False
        else:
            print(options)
            inp = validInput(options)
            CurrentDialogue = inp
    return CurrentDialogue
