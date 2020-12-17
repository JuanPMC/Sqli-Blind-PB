def ysisi(webpage, comprobador):

    res = webpage.find(comprobador)

    if res != -1:
        return True
    return False

print(ysisi('holaguanillo bananero', 'Hola'))