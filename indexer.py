def indexer(path):
    """busca todos los archivos html en el word wide web"""
    import os
    directorio = os.listdir(path)
    paginas = [pagina[4:-9] for pagina in directorio]
    word_wide_web = {}
    for index in range(len(paginas)):
        word_wide_web[index] = paginas[index]
    return word_wide_web