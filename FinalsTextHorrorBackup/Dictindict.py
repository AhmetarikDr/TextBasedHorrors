rooms = {
    "siloA": {
        "Lines": [
            "It's the middle storage room",
            "Filled with boxes of food and water",
            "You don't feel hungry. And you know, it's probably not the best time for a tea party",
            "So you start to look around",
            "There are two doors on the east and west walls of the room. Going to the other storage units",
            "And a bigger door on the north wall. It's the way to the corridor"
            ],
        "east": "siloB",
        "west": "siloC",
        "north": "corridorA",
        "item": [],
    },
    "siloB": {
        "Lines": [
            "This is the B section of the storage unit",
            "It's as dark as the section A",
            "But you can see the lever on the ground"
        ],
        "west": "siloA",
        "item": ["lever"]
    },
    "siloC": {
        "Lines": [
            "This is the C section of the storage unit",
            "There is a poster on the wall",
            "It's an advertisement of a corporation that sells sea shells on mars",
            "The line 'She sells sea shells on a sea shore' feels important for some reason"
        ],
        "east": "siloA",
        "item": []
    },
    "corridorA": {
        "Lines": [
            "There is no item to take",
            "There is the corridor B on west, the space port on east and control room on north",
            "Also you can go back to silo A from south"
        ],
        "south": "siloA",
        "north": "control-panel",
        "west": "corridorB",
        "east": "port",
        "locked": True,
        "item": []
    },
    "corridorB": {
        "Lines": [
            "It's huge. and has a lot of exits",
            "'south-east' goes to corridorA",
            "'north-east' goes to corridorC",
            "'south-west' goes to bedroomA",
            "'north-west' goes to bedroomB",
            "and east goes to the control panel",
            "there is no item to take"
        ],
        "south-east": "corridorA",
        "east": "control-panel",
        "north-east": "corridorC",
        "south-west": "bedroomA",
        "north-west": "bedroomB",
        "item": []
    },
    "corridorC": {
        "Lines": [
            "It's just a corridor like the others",
            "no item to take, but a lot of paths to follow",
            "your east is the archive, west is corridor B.",
            "south is control room, and north is the core"
        ],
        "south": "control-panel",
        "north": "core",
        "east": "archive",
        "west": "corridorB",
        "item": [],
        "locked": True
    },
    "port": {
        "Lines": [
            "This is the place for smaller space ships, the captain's ship is on the south wall. Ready to go",
        ],
        "west": "corridorA",
        "north": "archive",
        "south": "escape-rocket",
        "item": [],
    },
    "control-panel": {
        "Lines": [
            "This is the place captain uses to control everything",
            "You can use the control 'panel' to open archive's and corridorC's doors"
        ],
        "south": "corridorA",
        "north": "corridorC",
        "west": "corridorB",
        "item": ["panel"]
    },
    "bedroomA": {
        "Lines": [
            "It's where crew used to sleep",
            "There is something under the bed...?"
        ],
        "east": "corridorB",
        "item": ["bed"]
    },
    "bedroomB": {
        "Lines": [
            "It's where the captain used to sleep",
            "There is his wardrobe"
        ],
        "east": "corridorB",
        "item": ["wardrobe"]
    },
    "archive": {
        "Lines": [
            "This is where most of the crew works all day",
            "You can see some of them laying on the ground",
            "You can also see the key of the core!!! (or 'core-key' if you will)"
        ],
        "south": "port",
        "west": "corridorC",
        "item": ["core-key"],
        "locked": True
    },
    "escape-rocket": {
        "Lines": ["You used your now ex-captains ship to run away and save your life!!!"],
        "locked": True,
    },
    "core": {
        "Lines": "You reached the core BOOOOOOOOOOOOOM",
        "locked": True
    }
}

