class  owner:
    def __init__(self):
        self.name_owner = "pravin"
    def owner(self):
        print(f"The owner name is: {self.name_owner}")


class members:
    def __init__(self):
        self.name_member = "Ayush"
    def membrnam(self):
        print(f"The member name is: {self.name_member}")

class property(owner,members):
    def __init__(self):
        owner.__init__(self)
        members.__init__(self)
        self.name_buyer = "Amjad"
    def buyer(self):
        print(f"The property buyer name is {self.name_buyer} ")

t = property()
t.owner()
t.membrnam()
t.buyer()
