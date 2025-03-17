# En primer lugar importamos todas las funciones a utilizar y las variables creadas. 

import pprint
import os
import time
import random
from variables import *

#Función para crear tablero. En vertical se queda fija la columna y añadimos las filas
#Recordar que el nombre tablero solo se guarda dentro de la función. 

def crear_tablero():
    tablero = []
    for i in range(TAMANO):
        linea = []
        for j in range(TAMANO):
            linea.append(" ")
        tablero.append(linea)
    return tablero

# Función visualizar. Utilizamos pprint para mejorar la visualización.

def visualizar(tablero):
    pprint.pprint(tablero)


# Para el posicionamiento de barcos automático, en primer lugar creamos una función para comprobar si la posición del barco es valida.
# Definimos los argumentos tablero, fila, columna, eslora y dirección.
# La función devuelve True si la posición del barco es valida o False si la posición es incorrecta.
# Mediante un if se comprueba si el barco sale del tablero y mediante un for se recorre el rango de la eslora para ver si donde se quiere colocar el barco está vacio.

def posicion_barco_valida (tablero, fila, columna, eslora, direccion):
    if direccion == "S":
        if fila + eslora > TAMANO:  # El barco sale fuera del tablero
            return False
        for i in range(eslora):
            if tablero[fila + i][columna] != " ":  # Comprueba si la casilla está ocupada
                return False
    elif direccion == "E":
        if columna + eslora > TAMANO:  # El barco sale fuera del tablero
            return False
        for i in range(eslora):
            if tablero[fila][columna + i] != " ":  # Comprueba si la casilla está ocupada
                return False
    elif direccion == "N":
        if fila - eslora < -1:  # El barco sale fuera del tablero
            return False
        for i in range(eslora):
            if tablero[fila-i][columna] != " ":  # Comprueba si la casilla está ocupada
                return False
    elif direccion == "O":
        if columna - eslora < -1:  # El barco sale fuera del tablero
            return False
        for i in range(eslora):
            if tablero[fila][columna - i] != " ":  # Comprueba si la casilla está ocupada
                return False
    return True

# Función para colocar los barco 
# Como argumentos introducimos el tablero y la eslora. 
# Inicializamos con posición no valida, y creamos un bucle mediante while en donde obtenemos una dirección de barco, y posición mediante Random.
# Comprobamos mediante la función posicion_barco_valida si es correcta (True) o no (False).Forzamos con el bucle hasta encontrar una posición correcta.
# Entonces posicionamos el barco según su dirección, que filtramos mediante if/elif. Utilizamos for y el rango de eslora para colocar el barco.

def colocar_barco(tablero,eslora):
    posicion_valida = False
    while not posicion_valida:

        direccion = random.choice(["N", "S", "E", "O"])
        fila_barco = random.randint(0,TAMANO-1)
        columna_barco = random.randint(0, TAMANO-1)

        posicion_valida = posicion_barco_valida(tablero,fila_barco,columna_barco,eslora,direccion)

    if direccion == "S":
        for i in range(eslora):
            tablero[fila_barco + i][columna_barco] = "B"

    elif direccion == "E":
        for i in range(eslora):
            tablero[fila_barco][columna_barco + i] = "B"  # Coloca Barco en la casilla libre
                
    elif direccion == "N":
        for i in range(eslora):
            tablero[fila_barco-i][columna_barco] = "B"
            
    elif direccion == "O":
        for i in range(eslora):
            tablero[fila_barco][columna_barco - i] = "B" 

# Función para colocar los barcos
# Argumentos de entrada tablero y la variable ESLORA_BARCOS, donde hemos introducio todos los barcos y con su tamaño (eslora) en una lista. 
# Mediante un for vamos recorriendo la lista de ESLORA_BARCOS y colocando los barcos mediante la función colocar_barco.

def colocar_barcos(tablero, ESLORA_BARCOS):
    for i in ESLORA_BARCOS:
        colocar_barco(tablero,i)


# Función para el disparo 
# Introducimos como argumentos 2 tableros, en los barcos donde se dispara y en el de los disparos para llevar la cuenta de donde ha disparado. 
# Introducimos las coordenadas del disparo también como i,j
# Si aciertas el disparo devuelve True

def disparo(tablero_barcos,tablero_disparos,i,j):

    if tablero_barcos[i][j] == "B":
        print("Tocado en Fila:", i, "y Columna:", j)
        tablero_barcos[i][j] ="X"
        tablero_disparos[i][j] ="X"
        return True #si aciertas te vuelve a tocar
    elif tablero_barcos[i][j] == " ":
        print("Agua")
        tablero_barcos[i][j] ="O"
        tablero_disparos[i][j] ="O"
        return False
    else:
        print("Ya habías disparado allí!")
        return False
    
# Función para el turno del jugador
# Introducimos como argumentos tablero_disparos_jugador (para saber donde ha disparado), tablero_barcos_maquina (donde dispara), y contador_jugador (para saber si ya ha hundido todos los barcos)
# La función devuelve el contador_jugador
def turno_jugador(tablero_disparos_jugador,tablero_barcos_maquina,contador_jugador):
    #global contador_jugador
    # Creamos un bucle mediante while, ya que si el jugador acierta con el disparo vuelve a tirar. Se pide fila y columna y mediante la función disparo y si aciertas devuelve True.
    # Si no acierta el disparo, se cierra el bucle mediante un break. Si acierta, se suma en un contador. Y cuando el contador llega a la suma de esloras, ya ha ganado. 
    while True:
        print("Es TU TURNO. Indica las coordenadas del disparo:")
        visualizar(tablero_disparos_jugador)
        disparo_fila = int(input("Fila:"))
        disparo_columna = int(input("Columna:"))
        disparo_jugador = disparo(tablero_barcos_maquina, tablero_disparos_jugador, disparo_fila, disparo_columna)
    
        if disparo_jugador == False:
            break
        
        else:
            contador_jugador = contador_jugador + 1
            if contador_jugador == sum(ESLORA_BARCOS):
                print("Has ganado, todos los barcos están hundidos")
                break
            #os.system("cls")
    return contador_jugador

# Función para el turno de la máquina
# Introducimos como argumentos tablero_barcos_jugador (donde dispara), tablero_disparos_maquina (para saber donde ha disparado), y contador_maquina (para saber si ya ha hundido todos los barcos)
# La función principal devuelve el contador_maquina, que lleva la cuenta de los barcos disparados. 
# Mediante un primer bucle while si acierta con el disparo sigue y se suma el acierto al contador. Sino sale mediante un break
# Cuenta con otro while que realiza el disparo random, madiante un IF cuenta con la inteligencia de no disparar donde ya había disparado (ya fuera agua o un acierto)
def turno_maquina(tablero_barcos_jugador, tablero_disparos_maquina, contador_maquina):
    #global contador_maquina
    while True:
        print("Es el TURNO MÁQUINA")
        #visualizar (tablero_disparos_maquina)
        while True:
            disparo_maquina_fila = random.randint(0, TAMANO - 1)
            disparo_maquina_columna = random.randint(0, TAMANO - 1)
            if tablero_disparos_maquina[disparo_maquina_fila][disparo_maquina_columna] in ["O" , "X"]:
                pass
            else:
                break

        disparo_maquina = disparo(tablero_barcos_jugador, tablero_disparos_maquina, disparo_maquina_fila, disparo_maquina_columna)
        if disparo_maquina == False:
            break

        else:
            contador_maquina = contador_maquina + 1
            if contador_maquina == sum(ESLORA_BARCOS):
                print("Ha ganado la máquina!!")
                break
    visualizar(tablero_disparos_maquina)
    return contador_maquina