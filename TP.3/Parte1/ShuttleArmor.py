from GreedyAttack import *
from DinamicAttack import *

class ShuttleArmor:
    def __init__(self, shuttlesCount, strategy):
        if strategy == "DINAMICO":
            self.attackStrategy = DinamicAttack(shuttlesCount)
        else:
            self.attackStrategy = GreedyAttack(shuttlesCount)

    def attack(self, board):
        self.attackStrategy.attack(board)
