import random

import balanza
import bola

# Pablo rubio ariketa

bolas = [bola.Bola(1) for _ in range(8)]
posicion_aleatoria = random.randint(0, 8)
bolas.insert(posicion_aleatoria, bola.Bola(1.1))  # Bola más pesada

balanza = balanza.Balanza()

pisatuta = balanza.pesar(bolas[:3], bolas[3:6])
# Compara las primeras 4 bolas con las últimas 4
if pisatuta == 1:
    pisatuta_1 = balanza.pesar(bolas[:1], bolas[1:2])
    if pisatuta_1 == 1:
        print(balanza.emaitza(bolas[0]))
    elif pisatuta_1 == -1:
        print(balanza.emaitza(bolas[1]))
    else:
        print(balanza.emaitza(bolas[2]))

elif pisatuta == -1:
    pisatuta_2 = balanza.pesar(bolas[3:4], bolas[4:5])
    if pisatuta_2 == 1:
        print(balanza.emaitza(bolas[3]))
    elif pisatuta_2 == -1:
        print(balanza.emaitza(bolas[4]))
    else:
        print(balanza.emaitza(bolas[5]))

else:
    pisatuta_3 = balanza.pesar(bolas[5:6], bolas[6:7])
    if pisatuta_3 == 1:
        print(balanza.emaitza(bolas[6]))
    elif pisatuta_3 == -1:
        print(balanza.emaitza(bolas[7]))
    else:
        print(balanza.emaitza(bolas[8]))


# Muestra el resultado de la comparación
