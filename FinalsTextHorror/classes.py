
class rooms:
    no = 0
    description = ""
    options = {}
    items = {}

    def __init__(self, no = 0, description = "", options = {}, items = {}):
        self.no = no
        self.description = description
        self.options = options
        self.items = items

test = rooms(no=1)
test.description = "old room has three doors at right, left and in front of you"
test.options = {
    "check": ["checks the sorrounding area for items and information", "room1"],
}

roomiki = rooms(no=2)





