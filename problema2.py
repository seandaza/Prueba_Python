
def kadane(arreglo, inicio, fin, sumCols):

    n = len(arreglo)
    positivos = 0
    maxPositivos = 0
    inicioLocal = 0
    finLocal = 0

    for i in range(n):

        if(i == 0):
            if(arreglo[i] == sumCols):
                positivos += 1
        else:
            if(arreglo[i - 1] == sumCols):
                if(arreglo[i] == sumCols):
                    finLocal = i
                    positivos += 1
                else:
                    positivos = 0
            else:
                if(arreglo[i] == sumCols):
                    inicioLocal = i
                    finLocal = i
                    positivos += 1
                else:
                    positivos = 0

        if positivos > maxPositivos:
            maxPositivos = positivos
            inicio[0] = inicioLocal
            fin[0] = finLocal

    return maxPositivos * sumCols

def maximo_cuadrado(M):

    FILAS = len(M)
    COLUMNAS = len(M[0])
    sumaMaxima, finalIzq = -999999999999, None
    finalDer, finalArriba, finalAbajo = None, None, None
    izq, der, i = None, None, None

    temp = [None] * FILAS
    suma = 0
    inicio = [0]
    fin = [0]

    for izq in range(COLUMNAS):
        temp = [0] * FILAS

        for der in range(izq, COLUMNAS):

            for i in range(FILAS):
                temp[i] += M[i][der]

            sumCols = der - izq + 1
            suma = kadane(temp, inicio, fin, sumCols)

            if suma > sumaMaxima:

                tempFinalIzq = izq
                tempFinalDer = der
                tempFinalArriba = inicio[0]
                tempFinalAbajo = fin[0]

                tempColumnas = tempFinalDer - tempFinalIzq + 1
                tempFilas = tempFinalAbajo - tempFinalArriba + 1

                tempSubM = subMatriz(M, tempFinalArriba, tempFinalAbajo, tempFinalIzq, tempFinalDer)
                unosSubM = [[1 for i in range(tempColumnas)] for j in range(tempFilas)]

                if(tempSubM == unosSubM):
                    sumaMaxima = suma
                    finalIzq = izq
                    finalDer = der
                    finalArriba = inicio[0]
                    finalAbajo = fin[0]

    ancho = finalDer - finalIzq + 1
    alto = finalAbajo - finalArriba + 1
    lado = min(ancho, alto)

    return (finalArriba, finalIzq, lado)

def subMatriz(M, filaIni, filaFin, colIni, colFin):
    filas = filaFin - filaIni + 1
    cols = colFin - colIni + 1
    sub =  [[0 for i in range(cols)] for j in range(filas)]
    indFila = 0
    for i in range(filaIni, filaFin + 1):
        indCol = 0
        for j in range(colIni, colFin + 1):
            sub[indFila][indCol] = M[i][j]
            indCol += 1
        indFila += 1
    return sub

print("\n***** Bienvenido *****")
print("A continuación ingrese las dimensiones de la matriz.\n")

filas = int(input("filas: "))
columnas = int(input("columnas: "))

print("\nAhora ingrese los valores de cada fila separados por espacio.")

M = [None] * filas

for i in range(filas):
    M[i] = [None] * columnas

for i in range(filas):
    print("\nFila", i)
    vectorFila = input().split(" ")
    for j in range(columnas):
        M[i][j] = 0 if vectorFila[j] == "1" else 1

tupla = maximo_cuadrado(M)
print("")
print(tupla)
