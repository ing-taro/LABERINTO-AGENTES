import random


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


if __name__ == "__main__":
    lab = crear_laberinto_resoluble()
    imprimir_laberinto(lab)
