class Ship:
    life = 0

    def __init__(self, life):
        self.life = life

    def alive(self):
        return self.life > 0
