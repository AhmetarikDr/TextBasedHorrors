import functions
import dialogue
import classes

#----------------------------------------------------------------

test = [
    ["old room has three doors at right, left and in front of you", 0],
    ["its the toilet", 1],
    ["its the kitchen", 2],
    ["its a... lab?", 3],
    ["there is no 'back', you are at the beginnig of the game", 9],
]

oldRoom0 = [
    ["as i said, its an old looking room", 0],
    ["its the toilet", 1],
    ["its the kitchen", 2],
    ["its a... lab?", 3],
    ["there is no 'back', you are at the beginnig of the game", 9],
]

oldRoom1 = [
    ["AS I SAID, its an old looking room", 0],
    ["its the toilet", 1],
    ["its the kitchen", 2],
    ["its a... lab?", 3],
    ["there is no 'back', you are at the beginnig of the game", 9],
]

oldRoom2 = [
    ["are you fucking serious?", 9],
    ["its the toilet", 0],
    ["its the kitchen", 1],
    ["its a... lab?", 2],
    ["there is no 'back', you are at the beginnig of the game", 9],
]

toilet = [
    ["its disgusting and doesn't connect to any other room, but there is a scissor", 0],
    ["toilet is not connected to any other room", 9],
    ["toilet is not connected to any other room", 9],
    ["toilet is not connected to any other room", 9],
    ["you are at the old looking room again", 1]
]

kitchen = [
    ["its a little dusty, there is a door on the left wall, and a kitchen knife on a table!", 0],
    ["there is no path", 9],
    ["you are in a small room filled with old junk", 1],
    ["there is no path", 9],
    ["you are at the old looking room again", 2],
]

laborototro = []

# -------------------------------------------------------------start of the game

print("")

for i in range(0,8):
    print(dialogue.Monologue0[i])
    input()

print(dialogue.Entrance[0])
power = functions.validInput(functions.questionKeyWords)

if power == 1:
    print(dialogue.Entrance[1])
elif power == 0:
    print(dialogue.Entrance[2])

power = functions.validInput(functions.questionKeyWords)

if power == 0:
    print(dialogue.Entrance[3])
    input()
    for i in range(12,15):
        print(dialogue.Entrance[i])
        input()
elif power == 1:
    for i in range(4,15):
        print(dialogue.Entrance[i])
        input()

currentRoom = classes.test
power = 0

newNum = functions.roomManager(currentRoom, power)

classes.rooms(object)

print(newNum)


input()