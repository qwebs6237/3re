import random 
def wer(a, b):
    j = random.randint(a, b)
    return j

a = int(input('Введите число '))
b = int(input('Введите число '))
res = wer(a, b)
print('случайное число:', res)
