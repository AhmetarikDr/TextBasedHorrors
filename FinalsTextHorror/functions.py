power = 0

#------------------------------

explorationKeyWords = {    # that is a long name
    "check": ["checks the sorrounding area for items", 0],
    "right": ["goes right if a path exists", 1],
    "left": ["goes left if a path exists", 2],
    "forward": ["goes forward if a path exists", 3],
    "back": ["goes back to the last room", 4],
}

questionKeyWords = {
    "yes": ["do the action",0],
    "y": ["short for yes",0],
    "no": ["don't do anything or do something else",1],
    "n": ["short for no",1]
}

#-------------------------------

def validInput(keyWords):

    valid = False

    while not valid:
        try:
            inp = input()
            if not inp in keyWords.keys():
                raise Exception("No keyword found")

        except Exception as ex:
            print(ex)
            print("try again:")

        else:
            for key, num in keyWords.items():
                if inp == key:
                    inpPower = num[1]
            # print(inpPower)
            valid = True
            return inpPower

def keyHelp(keyWords):
    print("The key words:")
    for word, description in keyWords.items():
        print(word, ":", description[0])

def action(Dialogue, power):
    print(Dialogue[power][0])
    return Dialogue[power][1]

def exploration(roomName):
    power = 9  # 9 is the fail value, if you can't go any further with the option you choose, you get a 9 and try again
    while power == 9:
        power = int(validInput(explorationKeyWords))
        power = action(roomName, power)
    return power

def roomManager(room0, room00, room01, room02, room1, room2):
    if power == 0:
        return room0, room00, room01, room02
    elif power == 1:
        return room1
    elif power == 2:
        return room2
    elif power == 3:
        pass # lab

