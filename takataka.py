import string, ysisi

def takataka():
    dictionary = string.ascii_lowercase
    result = ""

    for item in dictionary:
        siono = ysisi(requestador(item, comprobador))
        if siono:
            result += item
        # ysisi

    print(result)


        #requestador(letra,buscador,posicion)