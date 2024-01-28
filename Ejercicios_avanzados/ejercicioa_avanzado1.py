#Zona de definicion de funciones
def contar_vocales(a):
    contador_vocales = 0
    vocales = ["a","e","i","o","u"]
    for caracter in a:
        if caracter in vocales:
            contador_vocales += 1
    return contador_vocales

def ingresar_palabras():
    lista_palabras = []
    palabra = input("Ingrese una palabra: ").lower()
    
    while palabra != "fin":
            cantidad_vocales = contar_vocales(palabra)
            lista_palabras.append([palabra, cantidad_vocales])
            palabra = input("ingrese una palabra: ").lower()
    
    return lista_palabras

#codigo principal


print(ingresar_palabras())