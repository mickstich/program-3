class access:

    def __init__(self,year,name,history,geography):
        self.year=year
        self.name=name
        self.history=history
        self.geography=geography
    def ke(self):
        print("history mark is ", self.history)
y=int(input("year "))
l=input("name ")
p=input("history ")
o=input("geography ")
obj=access(y,l,p,o)
obj.ke()




