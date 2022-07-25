class cal:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

    def mod(self):
        return self.a % self.b

result = cal(7, 3)
print(result.add())
print(result.sub())
print(result.mul())
print(int(result.div()))
print(result.mod())