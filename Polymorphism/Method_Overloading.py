class Addition:
    def add(self, a, b=0, c=0):
        print("Sum =", a + b + c)

obj = Addition()
obj.add(10, 20)
obj.add(10, 20, 30)