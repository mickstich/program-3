class two:

    def lis(self):
        self.a = ["a", "b", "c"]
        self.b = ["d", "e", "f"]
        for i, j in zip(self.a, self.b):
            self.c = i + j
            print(self.c)
obj = two()

obj.lis()
