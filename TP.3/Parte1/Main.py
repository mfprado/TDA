import sys
from Game import *

if __name__ == '__main__':
    # boardPath = sys.argv[1]
    # shuttlesCount = sys.argv[2]
    # strategy = sys.argv[3]
    #
    boardPath = "victorTests/bNaval_random5x4_0_100.txt"
    shuttlesCount = 3
    strategy = "DINAMICO"
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
    f.write("Tablero: " + str(boardPath) + " - Con Lanzaderas: " + str(shuttlesCount) + "\nModo: " + str(strategy) +    " - Puntos: " + str(points) + "\n")
    f.close()

