def pageRank(matriz):
    from numpy.linalg import matrix_power
    import numpy as np
    from functools import reduce
    pesos_iniciales = []
    for pagina in range(len(matriz)):
        pesos_iniciales.append(1/len(matriz))

    def sistema_dinamico(mat, pesos):


        array = np.array(mat)
        mat = matrix_power(mat, 2)
        mat = mat.tolist()
        
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

    print("inicio",pesos_iniciales)
    pesos_iniciales = sistema_dinamico(matriz, pesos_iniciales)
    print("final",pesos_iniciales)

    return pesos_iniciales