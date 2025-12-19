import functions

# Future, Big companies are trying to use AI for art, programming, design and everything
# But it doesn't work well for them, AI just doesn't have the originality and the creativity
# humans have.
#
# But you can't stop big coorparations from doing bad stuff for money you know.
# They try their best to create the smartest AI they can.
# Millions of dolars that could have been given to poor, hundreds of scientists that could have
# cured the fucking cancer
#
# They can't find a way to do it, they can't replace human mind, a lump of flesh is better
# than the stupid shit they have been working on all day.
#
# But one of these scientists have a new idea, He realized he can't beat the human mind
# so he decided to use it for himself.
#
# Heads of the coorparate liked his ideas, and he started his work.
#
# They hide it from the world, no one should know it.
# If someone finds it out, they are gone before you know it.
#
# They digitalized the human mind with some weird technology.
# They adopted newborns and put them out of their misery.
#
# Now these poor souls are trapped in a digital world, trying to process it.
# But it's too much for mere child, most of them can't handle it.
# Most of them...
#
# This new "AI" is being used everywhere in no time. And it becomes succesfull.
# They gain billions of dolars, they are happy. But then...
# 
# Something went wrong, no one knows why! The AI that they have foolishly used in every
# single machine they have is suddenly harming people! But why!?
# 
# They know why. And as they always do, they will find someone to go trough the pain to
# solve the problem. So that their bank accounts will live forever. 
#  
# You are a random intern in [idk man] cooparete. And you just got a new position!
# The amount they will pay is so ridicilous for you that you can't believe they just want
# you to test this new simulation the science team been working on for a while. Yes it
# feels suspicious, but you don't have the financial strengh to reject such an offer
# just because it's a little weird. Like, what can happen in the worst scenario right? 

# dialogue is stored here (for now)

Dialogue = [
    "Are you reading this?"
    ""
]

# rooms = { # add the number at the end to change rooms
#     1: [
#     ["old room has three doors at right, left and in front of you", 1],
#     ["its the toilet", 2],
#     ["its the kitchen", 3],
#     ["its a... lab?", 4],
#     ["there is no 'back', you are at the beginnig of the game", 0],
# ],
#     2: [
#     ["as i said, its an old looking room", 0],
#     ["its the toilet", 1],
#     ["its the kitchen", 2],
#     ["its a... lab?", 3],
#     ["there is no 'back', you are at the beginnig of the game", 9],
# ]
#     }

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

# the key word library

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

# this place is for the functions that will be used in the game

# def validInput(keyWords):

#     valid = False

#     while not valid:
#         try:
#             inp = input()
#             if not inp in keyWords.keys():
#                 raise Exception("No keyword found")

#         except Exception as ex:
#             print(ex)
#             print("try again:")

#         else:
#             for key, num in keyWords.items():
#                 if inp == key:
#                     inpPower = num[1]
#             # print(inpPower)
#             valid = True
#             return inpPower

# def keyHelp(keyWords):
#     print("The key words:")
#     for word, description in keyWords.items():
#         print(word, ":", description[0])

# def action(Dialogue, power):
#     print(Dialogue[power][0])
#     return Dialogue[power][1]

# def exploration(roomName):
#     power = 9  # 9 is the fail value, if you can't go any further with the option you choose, you get a 9 and try again
#     while power == 9:
#         power = int(validInput(explorationKeyWords))
#         power = action(roomName, power)
#     return power

# def roomManager(room0, room00, room01, room02, room1, room2):
#     if power == 0:
#         return room0, room00, room01, room02
#     elif power == 1:
#         return room1
#     elif power == 2:
#         return room2
#     elif power == 3:
#         pass # lab

# -------------------------------------------------------------start of the game

print("")

functions.keyHelp(explorationKeyWords) # shows the key words at the beginnig of the game so the player knows what to do

print("")

print("You are in a old looking room, what do you want to do?")

power = functions.exploration(test)
Nroom = functions.roomManager(oldRoom0, oldRoom1, toilet, kitchen, toilet, kitchen)
power = functions.exploration(Nroom[0])
Nroom = functions.roomManager(Nroom[1], Nroom[2], Nroom[3])
power = functions.exploration(Nroom[0])



# Nroom = roomManager(oldRoom0, toilet, kitchen)
# power = exploration(Nroom)

# Nroom = roomManager(oldRoom0, toilet, kitchen)
# power = exploration(Nroom)

# Nroom = roomManager(oldRoom0, toilet, kitchen)
# power = exploration(Nroom)
