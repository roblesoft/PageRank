
def pageRank(matriz):
    from numpy.linalg import matrix_power
    import numpy as np
    from functools import reduce
    from math import fabs
    from ThreadReturn import ThreadReturn
    import time
    import queue
    from threading import Thread
    tiempo_inicio = time.time()
    pesos_iniciales = [1/(len(matriz)) for pagina in range(len(matriz))]
    def arreglo(resultado, pesos, mat, inicio, fin):
        for i in range(inicio, fin):
            fila = []
            for j in range(len(mat)):
                fila.append(pesos[i] * mat[i][j])
            resultado.append(fila)

    def sistema_dinamico(mat, pesos, exponente=1):
        array = np.array(mat)
        mat = matrix_power(mat, exponente).tolist()
        matriz_resultado = []
        #for i in range(len(mat)):
        #    fila = []
        #    for j in range(len(mat)):
        #        fila.append(pesos[i] * mat[i][j])
        #    matriz_resultado.append(fila)
        primer_hilo = Thread(target=arreglo, args=(matriz_resultado, pesos, mat, 0, int(len(mat) / 2)))
        segundo_hilo = Thread(target=arreglo, args=(matriz_resultado, pesos, mat, int(len(mat)/ 2), len(mat)))
        primer_hilo.start()
        segundo_hilo.start()
        primer_hilo.join()
        segundo_hilo.join()
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

        #hilo_de_pesos_ini = ThreadReturn(target=sistema_dinamico, args=(matriz, pesos_iniciales, exp), name='pesos_ini')
        #hilo_de_pesos_ini.start()
        pesos_ini = sistema_dinamico(matriz, pesos_iniciales, exp)

        if success != len(pesos_finales):
            exp += 1
        #    hilos_de_pesos_finales = ThreadReturn(target=sistema_dinamico, args=(matriz, pesos_iniciales, exp), name='pesos_fin')
        #    hilos_de_pesos_finales.start()
        #    pesos_finales = hilos_de_pesos_finales.join()
        #    pesos_ini = hilo_de_pesos_ini.join()
            pesos_finales = sistema_dinamico(matriz, pesos_iniciales, exp)
            return checkUmbral(pesos_ini, pesos_finales, exp)
        else:  
        #    pesos_ini = hilo_de_pesos_ini.join()
            return pesos_ini


    pesos_finales = sistema_dinamico(matriz, pesos_iniciales)
    pesos = checkUmbral(pesos_iniciales, pesos_finales, 1)
    tiempo_final = time.time()
    print(tiempo_final - tiempo_inicio)
    return pesos