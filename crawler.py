import re
import os
from indexer import indexer

pagina = open('./world wide web/google.html', 'r')
path = './world wide web/'

def main():
    word_wide_web = indexer('./world wide web')
    print(word_wide_web)

 
    for key, value in word_wide_web.items():
        pagina = open(path + value + '.html', 'r')
        print("pagina {}".format(value))
        for linea in pagina:
            if re.findall('www.([a-zA-Z]+).com', linea):
                rango = re.finditer('www.([a-zA-Z]+).com', linea)
                for encontrado in rango:
                    sub_cadena = list(encontrado.span())
                    direccion = (linea[sub_cadena[0]:sub_cadena[1]])[4: -4]
                    print(direccion)


if __name__ == "__main__":
    main()