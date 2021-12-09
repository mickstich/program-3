class dic:

    def lis(self):
       self.a = [1, 2, 3]
       self.b = ["one", "two", "three"]
       self.c = dict(zip(self.a,self.b))
       print(self.c)
obj = dic()

obj.lis()
