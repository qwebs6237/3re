import random 


class Randomizer:
    def __init__(self, x, y):
        self.b1 = x
        self.b2 = y
        self.v = self._get_random_v()

    def _get_random_v(self):
        return random.randint(self.b1 , self.b2)

    def get_v(self):
        return self.v

a = int(input('Введите число '))
b = int(input('Введите число '))
res = Randomizer(a, b)
re = res.get_v()
print('случайное число:', re)
