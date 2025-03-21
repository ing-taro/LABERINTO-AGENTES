import random

# LABERINTO
def generar_laberinto(filas=10, columnas=10):
    laberinto = [['#' for _ in range(columnas)] for _ in range(filas)]

    # coloco E y S
    entrada = (1, 1)
    salida = (filas-2, columnas-2)

    # Aseguro que E se conecta con un camino
    for j in range(entrada[1], columnas//2 + 1):
        laberinto[entrada[0]][j] = ' '

    #  Aseguro que S se conecta con un camino
    for j in range(columnas//2, salida[1] + 1):
        laberinto[salida[0]][j] = ' '

    # Creo caminos
    for j in range(1, columnas-1):
        laberinto[filas//2][j] = ' '
    for i in range(1, filas-1):
        laberinto[i][columnas//2] = ' '

    # Coloco E y S
    laberinto[entrada[0]][entrada[1]] = 'E'
    laberinto[salida[0]][salida[1]] = 'S'

    # Coloco más caminos aleatorios para asegurar solucion
    for _ in range(filas * columnas // 4):
        i = random.randint(1, filas-2)
        j = random.randint(1, columnas-2)
        if (i, j) == entrada or (i, j) == salida:
            continue
        laberinto[i][j] = ' '

    return laberinto


def mostrar_laberinto(laberinto):
    """Muestra el laberinto en consola."""
    for fila in laberinto:
        print(''.join(fila))


def encontrar_posicion(laberinto, simbolo):
    """Encuentra la posición de E o S."""
    for i, fila in enumerate(laberinto):
        for j, celda in enumerate(fila):
            if celda == simbolo:
                return (i, j)
    return None


#menu para elegir
def menu_principal():
    print("\n--- Menú Laberintos ---")
    print("1. Generar laberinto automático")
    print("2. Cargar laberinto desde archivo")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")
    return opcion


<<<<<<< HEAD
#AGENTE REACTIVO
=======
# --------------------- Lógica de agentes ---------------------
>>>>>>> f5b184780a8befe22123ff040b15e4cc08cb972d
def agente_reactivo(laberinto):
    entrada = encontrar_posicion(laberinto, 'E')
    salida = encontrar_posicion(laberinto, 'S')
    pos_actual = entrada
    movimientos = 0
    max_iter = 1000

<<<<<<< HEAD
    puede_continuar = True

    while movimientos < max_iter and pos_actual != salida and puede_continuar:
=======
    while movimientos < max_iter and pos_actual != salida:
        # Lógica de movimiento aleatorio
>>>>>>> f5b184780a8befe22123ff040b15e4cc08cb972d
        i, j = pos_actual
        direcciones = []

        if i > 0 and laberinto[i - 1][j] != '#': direcciones.append((-1, 0))
        if i < len(laberinto) - 1 and laberinto[i + 1][j] != '#': direcciones.append((1, 0))
        if j > 0 and laberinto[i][j - 1] != '#': direcciones.append((0, -1))
        if j < len(laberinto[0]) - 1 and laberinto[i][j + 1] != '#': direcciones.append((0, 1))


        if not direcciones:
            puede_continuar = False
        else:

            di, dj = random.choice(direcciones)
            pos_actual = (i + di, j + dj)
            laberinto[i][j] = '.'
            movimientos += 1

    return pos_actual == salida, movimientos

#AGENTE INFORMADO
def agente_deliberativo(laberinto):
    entrada = encontrar_posicion(laberinto, 'E')
    salida = encontrar_posicion(laberinto, 'S')
    pos_actual = entrada
    movimientos = 0
    max_iter = 1000

    cont_mov = []





#main
if __name__ == "__main__":
    salir = False
    while not salir:
        opcion = menu_principal()

        if opcion == '1':
            lab = generar_laberinto()
            print("\nLaberinto generado:")
            mostrar_laberinto(lab)


            entrada_pos = encontrar_posicion(lab, 'E')
            salida_pos = encontrar_posicion(lab, 'S')

            if not entrada_pos or not salida_pos:
                print("Error: El laberinto no tiene E/S válidas.")
                continue

            lab_resolver = [fila.copy() for fila in lab]
            exito, movs = agente_reactivo(lab_resolver)

            print("\nResultado:")
            mostrar_laberinto(lab_resolver)
            print(f"\n{'Éxito' if exito else 'Fallo'} en {movs} movimientos")

        elif opcion == '2':
<<<<<<< HEAD
            #cargo el archivo
            archivo = input("Nombre del archivo (opciones: maze1.txt, maze2.txt, maze3.txt): ")
=======
            # Cargar desde archivo 
            archivo = input("Nombre del archivo (ej: maze1.txt): ")
>>>>>>> f5b184780a8befe22123ff040b15e4cc08cb972d
            try:
                with open(archivo, 'r') as f:
                    lab = [list(linea.strip()) for linea in f]
                print("\nLaberinto cargado:")
                mostrar_laberinto(lab)

<<<<<<< HEAD

            except FileNotFoundError: #chatgpt
=======
            except FileNotFoundError:
>>>>>>> f5b184780a8befe22123ff040b15e4cc08cb972d
                print("¡Archivo no encontrado!")

        elif opcion == '3':
            salir = True
            print("Saliendo del programa...")

        else:
            print("Opción no válida")
