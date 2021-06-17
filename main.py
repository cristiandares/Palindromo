def palindromo(palabra):
    palabra = palabra.replace(" ","")
    palabra = palabra.lower()

    #Invertimos la pablabra
    palabra_invertida = palabra[::-1]

    #Validamos si la palabra es igual de forma invertida
    if palabra == palabra_invertida:
        return True
    else:
        return False

def run():
    palabra = input("Escribe una palabra: ")
    es_palindromo = palindromo(palabra)
    
    if es_palindromo:
        print("Es palíndromo")
    else:
        print("No es palíndromo")    


if __name__ == "__main__":
    run()