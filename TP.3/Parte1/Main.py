import sys
from Game import *


if __name__ == '__main__':
    boardPath = sys.argv[1]
    shuttlesCount = sys.argv[2]
    game = Game(boardPath, int(shuttlesCount))
    points = 0
    turn = 1
    while not game.finished():
        print ("TURNO NUMERO: " + str(turn))
        points += game.playTurn()
        print ("PUNTOS : " + str(points))
        print ("TURNOS TOTALES: " + str(turn))
        turn += 1
