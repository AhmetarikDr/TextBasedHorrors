
#------------------------------

questionKeyWords = {
    "yes": 0,
    "y": 0,
    "no": 1,
    "n": 1
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
                    inpPower = num
            valid = True
            return inpPower

# def keyHelp(keyWords):
#     print("The key words:")
#     for word, description in keyWords.items():
#         print(word, ":", description[0])

def keyHelp(keyWords):
    print("The key words:")


def action(Dialogue, power):
    print(Dialogue[power][0])
    return Dialogue[power][1]

def roomManager(currentRoom, power):
    newNum = currentRoom.no + power
    return newNum
    # i need to change the current room based on the new no



