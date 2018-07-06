#!/usr/bin/env bash
echo "RESULTADOS DE LOS TESTS" > output.txt
python Main.py victorTests/bNaval_uniforme4x4.txt 2 GREEDO
python Main.py victorTests/bNaval_uniforme4x4_difVida.txt 2 GREEDO
python Main.py victorTests/bNaval_random5x4_0_100.txt 3 GREEDO
python Main.py victorTests/bNaval_random4x4_0_20.txt 3 GREEDO
python Main.py victorTests/bNaval_pocodenso16x4.txt 4 GREEDO
python Main.py victorTests/bNaval_gradientes_invertidos_4x5.txt 2 GREEDO
python Main.py victorTests/bNaval_mas_de_uno.txt 2 GREEDO