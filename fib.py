class Fib():
    def __init__(self):
        self.x = 0
        self.y = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.x = self.y
        self.y = self.x+self.y
        return self.x


fib = Fib()
for i in fib:
    if i > 10:
        break
    print(i)
