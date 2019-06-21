class Human:
    def __init__(self):
        self.blood = 7000

    def add_blood(self, volume):
        self.blood += volume
        return self.blood


a = Human()
print(a.add_blood(3000))
print(a.blood)



