import random
import copy


#declaro los laberintos precargados cmo lista d listas
MAZES = {
    "maze1": [
        list("###############"),
        list("#E  # # #     #"),
        list("### ###       #"),
        list("##  # # ###   #"),
        list("# #           #"),
        list("# # #         #"),
        list("# # ## # #    #"),
        list("## #          #"),
        list("# ##         S#"),
        list("###############")
    ],
    "maze2": [
        list("####################"),
        list("#E    #  ##   # # ##"),
        list("## #  # # #    # ###"),
        list("#    #     #   #####"),
        list("#      # ##     #  #"),
        list("### #    ###  # #  #"),
        list("#   #  ### #       #"),
        list("#     ##        #  #"),
        list("#  #  #    ###     #"),
        list("# #    # # # ##    #"),
        list("#   #     ##    #  #"),
        list("#   #    #         #"),
        list("#  ##  #   ## #   ##"),
        list("#   ## #  # # #   ##"),
        list("# #   # #          #"),
        list("# #  #      #  #   #"),
        list("#    #       # #   #"),
        list("##  ##  ## ## #   ##"),
        list("## ##     #        #"),
        list("#  ###   # #      ##"),
        list("#    #  #   ##   # #"),
        list("####      # #      #"),
        list("#  # #  #  ## ## ###"),
        list("####   # #  #    #S#"),
        list("####################")
    ],
    "maze3": [
        list("##########"),
        list("#E    # ##"),
        list("# #  #  ##"),
        list("# #   ## #"),
        list("#     ## #"),
        list("#   ##   #"),
        list("#  #    ##"),
        list("#    #   #"),
        list("###  ###S#"),
        list("##########")
    ]
}

# LABERINTO
def generar_laberinto(filas=10, columnas=10):

    #lleno todo de paredes
    laberinto = [['#' for _ in range(columnas)] for _ in range(filas)]

    # definicion de E y S
    entrada = (1, 1)
    salida = (filas-2, columnas-2)

    # Aseguro que E se conecta con un camino
    for j in range(entrada[1], columnas//2 + 1):
        laberinto[entrada[0]][j] = ' '

    #  Aseguro que S se conecta con un camino
    for j in range(columnas//2, salida[1] + 1):
        laberinto[salida[0]][j] = ' '

    # Creo caminos a izquierda y derecha
    for j in range(1, columnas-1):
        laberinto[filas//2][j] = ' '
    for i in range(1, filas-1):
        laberinto[i][columnas//2] = ' '

    # Coloco E y S
    laberinto[entrada[0]][entrada[1]] = 'E'
    laberinto[salida[0]][salida[1]] = 'S'

    # Coloco caminos aleatorios por si acaso
    for _ in range(filas * columnas // 4):
        i = random.randint(1, filas-2)
        j = random.randint(1, columnas-2)
        if (i, j) == entrada or (i, j) == salida:
            continue
        laberinto[i][j] = ' '

    return laberinto


#muestra el laberinto cmo corresponde(formaetado)
def mostrar_laberinto(laberinto):
    for fila in laberinto:
        print(''.join(fila))


#devuelve la entrada y la salida
def encontrar_posicion(laberinto, simbolo):
    for i, fila in enumerate(laberinto):
        for j, celda in enumerate(fila):
            if celda == simbolo:
                return (i, j)
    return (-1, -1)


#menu para elegir
def menu_principal():
    print("\n--- Menú Laberintos ---")
    print("1. Generar laberinto automático")
    print("2. Cargar laberinto desde archivo")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")
    return opcion

#AGENTE REACTIVO

def agente_reactivo(laberinto):
    entrada = encontrar_posicion(laberinto, 'E')
    salida = encontrar_posicion(laberinto, 'S')
    pos_actual = entrada
    movimientos = 0
    max_iter = 1000
    puede_continuar = True

    while movimientos < max_iter and pos_actual != salida:
        i, j = pos_actual
        direcciones = []

        # Reglas genericas para moverse
        if i > 0 and laberinto[i - 1][j] != '#': direcciones.append((-1, 0))
        if i < len(laberinto) - 1 and laberinto[i + 1][j] != '#': direcciones.append((1, 0))
        if j > 0 and laberinto[i][j - 1] != '#': direcciones.append((0, -1))
        if j < len(laberinto[0]) - 1 and laberinto[i][j + 1] != '#': direcciones.append((0, 1))

        if not direcciones:
            puede_continuar = False
        else:
            # si hay mas de un camino posible, elige de forma aleatoria
            cambio_i, cambio_j = random.choice(direcciones)
            pos_actual = (i + cambio_i, j + cambio_j)
            laberinto[i][j] = '.'
            movimientos += 1 #incrementa

    return pos_actual == salida, movimientos


# AGENTE INFORMADO
def agente_informado(laberinto):
    entrada = encontrar_posicion(laberinto, 'E')
    salida = encontrar_posicion(laberinto, 'S')
    pos_actual = entrada
    movimientos = 0
    max_iter = 1000
    puede_continuar = True
    visitados = set()  #array dinamico para la memoria

    while movimientos < max_iter and pos_actual != salida and puede_continuar:
        i, j = pos_actual
        direcciones = []

        # reglas genericas para moverse
        if i > 0 and laberinto[i - 1][j] != '#': direcciones.append((-1, 0))
        if i < len(laberinto) - 1 and laberinto[i + 1][j] != '#': direcciones.append((1, 0))
        if j > 0 and laberinto[i][j - 1] != '#': direcciones.append((0, -1))
        if j < len(laberinto[0]) - 1 and laberinto[i][j + 1] != '#': direcciones.append((0, 1))

        if not direcciones:
            puede_continuar = False
        else:
            no_visitadas = []
            ya_visitadas = []

            #bucle para clasificar direcciones
            for cambio_i, cambio_j in direcciones:
                nueva_pos = (i + cambio_i, j + cambio_j)
                if laberinto[nueva_pos[0]][nueva_pos[1]] == 'S':
                    pos_actual = nueva_pos
                    movimientos += 1
                    return True, movimientos
                elif laberinto[nueva_pos[0]][nueva_pos[1]] != '.' and nueva_pos not in visitados:
                    no_visitadas.append((cambio_i, cambio_j))
                else:
                    ya_visitadas.append((cambio_i, cambio_j))

            #actualiza el estado del informado
            if no_visitadas:
                cambio_i, cambio_j = random.choice(no_visitadas)
            elif ya_visitadas:
                cambio_i, cambio_j = random.choice(ya_visitadas)
            else:
                puede_continuar = False
                continue

            visitados.add(pos_actual)
            pos_actual = (i + cambio_i, j + cambio_j)
            laberinto[i][j] = '.'
            movimientos += 1 #incrementa

    return pos_actual == salida, movimientos


#elegir agente por comodidad
def seleccionar_agente():
    print("\nSelecciona un agente:")
    print("1. Agente Reactivo")
    print("2. Agente Informado")
    return input("Opcion: ")


#main
if __name__ == "__main__":
    salir = False
    while not salir:
        opcion = menu_principal()

        if opcion == '1':
                lab = generar_laberinto()
                print("\nLaberinto generado:")

        if opcion == '2':
            seleccion = input("Elige laberinto (maze1/maze2/maze3): ").strip().lower()
            if seleccion not in MAZES:
                print("Laberinto inválido")
                continue
            lab = [fila.copy() for fila in MAZES[seleccion]]  # copio manualmente
            print("\nLaberinto cargado:")

            mostrar_laberinto(lab)
            entrada_pos = encontrar_posicion(lab, 'E')
            salida_pos = encontrar_posicion(lab, 'S')


            agente = seleccionar_agente()
            lab_resolver = [fila.copy() for fila in lab]

            if agente == '1':
                exito, movs = agente_reactivo(lab_resolver)
            elif agente == '2':
                exito, movs = agente_informado(lab_resolver)

            print("\nResultado:")
            mostrar_laberinto(lab_resolver)
            print(f"\n{'Éxito' if exito else 'Fallo'} en {movs} movimientos")

        elif opcion == '3':
            salir = True
            print("Saliendo del programa...")

        else:
            print("Opción no válida")