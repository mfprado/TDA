from GreedyAttack import *
from DinamicAttack import *

class ShuttleArmor:
    def __init__(self, shuttlesCount, strategy, board):
        if strategy == "DINAMICO":
            self.attackStrategy = DinamicAttack(shuttlesCount, board)
        else:
            self.attackStrategy = GreedyAttack(shuttlesCount, board)

    def attack(self, board):
        self.attackStrategy.attack(board)
