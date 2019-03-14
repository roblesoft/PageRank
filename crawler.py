import re
import os
from indexer import indexer

path = './world wide web/'

def main():
    word_wide_web = indexer('./world wide web')
    print(word_wide_web)

    matriz_de_adyacencia = []
    for page in word_wide_web.keys():
        matriz_de_adyacencia.append([])

    for page in matriz_de_adyacencia:
        for i in range(len(word_wide_web)):
            page.append(0)
    print(matriz_de_adyacencia)
 
    for key, value in word_wide_web.items():
        pagina = open(path + "www." + value + '.com.html', 'r')
        pag = open(path + "www." + value + '.com.html', 'r')
        links = 0
        print("pagina {}".format(value))
        for linea in pagina:
            if re.findall('www.([a-zA-Z]+).com', linea):
                links += 1
        print("numero de links {} en {} ".format(links, value))
        for linea in pag:
            if re.findall('www.([a-zA-Z]+).com', linea):
                for encontrado in re.finditer('www.([a-zA-Z]+).com', linea):
                    sub_cadena = list(encontrado.span())
                    direccion = (linea[sub_cadena[0]:sub_cadena[1]])[4: -4]
                    print(direccion)
                    lookup = {value: key for key, value in word_wide_web.items()}
                    print(lookup[direccion])
                    print(1/links)
                    matriz_de_adyacencia[lookup[direccion]][key]= 1/links
    for row in matriz_de_adyacencia:
        print("\n")
        for col in row:
            print("| {:.2f} |\t ".format(col), end="")

    print("")
    return matriz_de_adyacencia


if __name__ == "__main__":
    main()