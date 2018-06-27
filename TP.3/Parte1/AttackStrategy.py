from abc import ABCMeta, abstractmethod

class AttackStrategy():
    __metaclass__ = ABCMeta

    def __init__(self, shuttlesCount):
        self.shuttlesCount = shuttlesCount

    @abstractmethod
    def attack(self, board): pass
