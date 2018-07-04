import csv
from Board import *
from Cell import *
from ShuttleArmor import *


class Game:

    def __init__(self, path, shuttlesCount, strategy):
        self.initializeBoard(path)
        self.shuttleArmor = ShuttleArmor(shuttlesCount, strategy)

    def initializeBoard(self, path):
        file = open(path, 'r')
        reader = csv.reader(file, delimiter=' ')
        rows = sum(1 for row in file)
        file.seek(0)
        columns = len(next(reader)) - 1
        file.seek(0)

        self.board = Board(rows)
        actualRow = 0
        for line in reader:
            for i in range(1, columns + 1, 1):
                self.board.addCell(Cell(actualRow, i - 1, int(line[i])))
            self.board.addShip(int(line[0]), actualRow)
            actualRow += 1

    def finished(self):
        return not self.board.shipAlive()

    def playTurn(self):
        print("\nINICIO DE TURNO: ")
        self.board.draw()
        self.shuttleArmor.attack(self.board)
        print("\nTABLERO POST ATAQUE: ")
        self.board.draw()
        self.board.removeDeadShips()
        self.board.moveShips()
        return self.board.shipsAliveCount()


game = Game("board.csv", 3, "DINAMICO")
points = 0
turn = 1
while not game.finished():
    print ("TURNO NUMERO: " + str(turn))
    points += game.playTurn()
    print ("PUNTOS : " + str(points))
    print ("TURNOS TOTALES: " + str(turn))
    turn += 1