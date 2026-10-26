class ghar:
    def __init__(self,):
        self.nameg = "sukhdev"
        self.location = "Digma"
        # self.nameg = nameg
        # self.location = location

    def gharn(self):
        print(f"ghar ka naam: {self.nameg} and location is: {self.location}")

class family(ghar):
    def __init__(self):
        ghar.__init__(self)
        self.namef = "Raj"

    def familyn(self):
        print(f"family name is:{self.namef}")

u = family()
u.gharn()
u.familyn()
