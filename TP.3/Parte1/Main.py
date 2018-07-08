import sys
from Game import *

if __name__ == '__main__':
    boardPath = sys.argv[1]
    shuttlesCount = sys.argv[2]
    strategy = sys.argv[3]

    game = Game(boardPath, int(shuttlesCount), strategy)
    points = 0
    turn = 1
    print("\n\x1b[5;30;41mJUGANDO CON ESTRATEGIA: " + strategy + "\x1b[0m\n")
    while not game.finished():
        print ("\nTURNO NUMERO: " + str(turn))
        points += game.playTurn()
        print ("PUNTOS : " + str(points))
        print ("TURNOS TOTALES: " + str(turn))
        turn += 1


    f = open('output.txt', 'a')
    f.write("Tablero: " + str(boardPath[12:len(boardPath)]) + " - Lanzaderas: " + str(shuttlesCount) + " - Modo: " + str(strategy) +    " - Puntos: " + str(points) + "\n")
    f.close()

