def pageRank(matriz):
    from numpy.linalg import matrix_power
    import numpy as np
    from functools import reduce

    pesos = [1/(len(matriz)) for pagina in range(len(matriz))]

    def sistema_dinamico(mat, pesos, exponente=2):
        array = np.array(mat)
        mat = matrix_power(mat, exponente).tolist()
        
        matriz_resultado = []
        for i in range(len(mat)):
            fila = []
            for j in range(len(mat)):
                fila.append(pesos[i] * mat[i][j])
            matriz_resultado.append(fila)
        pesos_nuevos = []
        for i in range(len(matriz)):
            pesos_nuevos.append(reduce(lambda x, y: x + y, matriz_resultado[i]))
        return pesos_nuevos

    pesos = sistema_dinamico(matriz, pesos, 8)

    return pesos