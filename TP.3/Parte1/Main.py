import sys
from Game import *


if __name__ == '__main__':
    boardPath = sys.argv[1]
    shuttlesCount = sys.argv[2]
    game = Game(boardPath, int(shuttlesCount))
    playerA = 0
    playerB = 0
    turn = 1
    while not game.finished():
        print ("TURNO NUMERO: " + str(turn))
        (pointsA, pointsB) = game.playTurn()
        playerA += pointsA
        playerB += pointsB
        print ("PUNTOS JUGADOR A: " + str(playerA))
        print ("PUNTOS JUGADOR B: " + str(playerB))
        print ("TURNOS TOTALES: " + str(turn))
        turn += 1




