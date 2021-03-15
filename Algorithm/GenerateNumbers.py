import random
from random import randint


def createRandomNumbers():
    winnerNumberList = []
    for _ in range(5):
        winnerNumberList.append(randint(1, 35))

    return random.sample(winnerNumberList, 5)
