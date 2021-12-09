class empty:
    def str(self):
       self.a= ["my","name ",""," is ","mick","",26]
       self.c = list(filter(None,self. a))
       print(self.a)
       print(self.c)
obj =empty()
obj.str()