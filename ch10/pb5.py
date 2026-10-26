from random import randint
class Train:
    def __init__(self,trainNo):
        self.trainNo = trainNo

    def Book(self,fro,to):
        print(f"The ticket is booked in train No : {self.trainNo} from {fro} to {to}")
    def getstatus(self):
        print(f"Train no : {self.trainNo} is running on the time")
    def getfare(self,fro,to):
        print(f"ticket in train no : {self.trainNo} from {fro} to {to} is {randint(222,555)}")
r = Train(5674)
r.Book("R.ganj","A.pur")
r.getstatus()
r.getfare("R.ganj","A.pur")