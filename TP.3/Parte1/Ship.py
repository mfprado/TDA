class Ship:

    def __init__(self, life):
        self.life = life

    def alive(self):
        return self.life > 0

    def receiveAttack(self, damage):
        self.life -= damage

