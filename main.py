import random
import io


output = io.StringIO()


def crear_laberinto_resoluble(filas=11, columnas=15):
    if filas % 2 == 0:
        filas += 1
    if columnas % 2 == 0:
        columnas += 1

    laberinto = [['#' for _ in range(columnas)] for _ in range(filas)]

    laberinto[1][0] = '#E'
    laberinto[filas - 2][columnas - 2] = 'S'

    def generar_camino(x, y):
        direcciones = [(0, 2), (2, 0), (0, -2), (-2, 0)]
        random.shuffle(direcciones)
        for dx, dy in direcciones:
            nx, ny = x + dx, y + dy
            if 1 <= nx < filas - 1 and 1 <= ny < columnas - 1 and laberinto[nx][ny] == '#':
                laberinto[x + dx // 2][y + dy // 2] = ' '
                laberinto[nx][ny] = ' '
                generar_camino(nx, ny)

    laberinto[1][1] = ' '
    generar_camino(1, 1)


    if laberinto[filas - 3][columnas - 2] == '#':
        laberinto[filas - 3][columnas - 2] = ' '
    if laberinto[filas - 2][columnas - 3] == '#':
        laberinto[filas - 2][columnas - 3] = ' '

    return laberinto


def imprimir_laberinto(laberinto):
    for fila in laberinto:
        print("".join(fila))
    print()


def agente_reactivo(laberinto):

    for i in range(len(laberinto)):
        for j in range(len(laberinto[i])):
            if laberinto[i][j] == '#E':
                agente_fila, agente_columna = i, j
                break


    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]


    while laberinto[agente_fila][agente_columna] != 'S':
        # Marcar la casilla actual como visitada
        if laberinto[agente_fila][agente_columna] != '#E':
            laberinto[agente_fila][agente_columna] = '·'


        movido = False
        for direccion in direcciones:
            nueva_fila = agente_fila + direccion[0]
            nueva_columna = agente_columna + direccion[1]


            if 0 <= nueva_fila < len(laberinto) and 0 <= nueva_columna < len(laberinto[0]):
                if laberinto[nueva_fila][nueva_columna] == ' ' or laberinto[nueva_fila][nueva_columna] == 'S':
                    agente_fila, agente_columna = nueva_fila, nueva_columna
                    movido = True
                    break


        if not movido:
            print("El agente no puede encontrar la salida.")
            break


        imprimir_laberinto(laberinto)

    if laberinto[agente_fila][agente_columna] == 'S':
        print("¡El agente ha encontrado la salida!")


if __name__ == "__main__":
    lab = crear_laberinto_resoluble()

    def guardar_laberinto(laberinto, archivo = None):
        for fila in laberinto
            linea  = " ".join(fila)
            print(linea)
            if archivo:
                print(linea, file=archivo)

    print("Laberinto inicial:")
    imprimir_laberinto(lab)

    print("Recorrido del agente:")
    agente_reactivo(lab)