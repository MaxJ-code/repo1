
from rotator import rotate
import random as rd
def randomizer(parts):
    list = ["x", "y", "z"]
    for i in range(rd.randrange(0, 10)):
        axis = list[rd.randrange(0, 2)]
        slot = rd.randrange(-1, 1)