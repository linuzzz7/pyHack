from icecream import ic


def add(x, y):
    return x + y


dict1 = {'Alex': ['passwbook', 'water', 'red'], 'Lena': [1, 2, 3]}
print(dict1)

ic(dict1)

x = ic(add(10, 20))
print(x + 2)
