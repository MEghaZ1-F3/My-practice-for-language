class Number:
    def __init__(self, n):
        self.t = n

    def __add__(self,num):
        return self.t + num.t


n = Number(4)
m= Number(6)

print(n+m)