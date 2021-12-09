class merge:

    def lis(self):
        self.a = {1: "one", 2: "two", 3: "three"}
        self.b = {4: "four", 5: "five", 6: "six"}
        self.a.update(self.b)
        print(self.a)
obj = merge()

obj.lis()
