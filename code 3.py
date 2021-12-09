class order:
    def lis(self):
        self.a = [1, 2, 3, 4]
        self.b = [600, 700, 800, 900]
        self.c = self.b[::-1]
        print(self.c)
        for i, j in zip(self.a, self.c):
            print(i, j)
obj=order()
obj.lis()
