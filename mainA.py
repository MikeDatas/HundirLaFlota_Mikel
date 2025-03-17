# Importamos todas las funciones del archivo funciones, el (*) significa todos

from funcionesA import *

# Creamos el tablero donde se colocan los barcos de la máquina

tablero_barcos_maquina = crear_tablero()

# Creamos el tablero donde el jugador dispara

tablero_disparos_jugador = crear_tablero()

# Creamos el tablero donde se colocan los barcos del jugador

tablero_barcos_jugador = crear_tablero()

# Creamos el tablero donde la máquina dispara

tablero_disparos_maquina = crear_tablero()

# Colocamos los barcos de la máquina de manera aleatoria

colocar_barcos(tablero_barcos_maquina, ESLORA_BARCOS)

# Colocamos los barcos del jugador de manera aleatoria

colocar_barcos(tablero_barcos_jugador, ESLORA_BARCOS)

# Visualizamos el tablero de la máquina donde se han colocado los barcos. Tenemos 10 segundos para verlo.
print("Bienvenido a HUNDIR LA FLOTA")
print("")
print("Tablero de la máquina donde coloca los barcos, tienes 10 segundos para visualizar")
visualizar(tablero_barcos_maquina)
time.sleep(10)
os.system("cls")
print()

# Comienzan los turnos. Se inicializan los contadores del jugador y la máquina a 0. Es decir, todavía no han acertado ningún tiro. 

contador_jugador = 0
contador_maquina = 0
contador_intentos = 0
# Se crea un bucle mediante while donde empieza la partida el jugador y luego la máquina. Hasta que alguno de los dos hunda todos los barcos, condición que se ha creado con if y mediante un break sale del bucle. 

while True:
    #Turno jugador
    contador_jugador = turno_jugador(tablero_disparos_jugador,tablero_barcos_maquina,contador_jugador)
    if contador_jugador == sum(ESLORA_BARCOS):
        break

    #Turno máquina
    contador_maquina = turno_maquina(tablero_barcos_jugador, tablero_disparos_maquina, contador_maquina)
    if contador_maquina == sum(ESLORA_BARCOS):
        break




