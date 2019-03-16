def pageRank(matriz):
    from numpy.linalg import matrix_power
    import numpy as np
    from functools import reduce
    from math import fabs

    pesos_iniciales = [1/(len(matriz)) for pagina in range(len(matriz))]

    def sistema_dinamico(mat, pesos, exponente=1):
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

    def checkUmbral(pesos_inicio, pesos_finales, exp=1):
        success = 0
        for valor in range(len(pesos_iniciales)):
            umbral = fabs(pesos_finales[valor] - pesos_inicio[valor])
            if  umbral >= 0.0 and umbral <= 0.01:
                success += 1

        pesos_ini = sistema_dinamico(matriz, pesos_iniciales, exp)
        if success != len(pesos_finales):
            exp += 1
            pesos_finales = sistema_dinamico(matriz, pesos_iniciales, exp)
            return checkUmbral(pesos_ini, pesos_finales, exp)
        return pesos_ini

    pesos_finales = sistema_dinamico(matriz, pesos_iniciales)
    pesos = checkUmbral(pesos_iniciales, pesos_finales, 1)
    return pesos