import pandas as pd


class PP():
    def __init__(self, name, c, x, y, z):
        self.name = name
        self.c = c
        self.x = x
        self.y = y
        self.z = z

df = pd.read_excel('Data/Book1.xlsx', sheet_name='None')

potions = df.values.tolist()

print(potions)