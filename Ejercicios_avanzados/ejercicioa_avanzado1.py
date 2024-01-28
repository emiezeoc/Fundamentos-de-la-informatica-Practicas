texto = input("Ingrese una cadena de texto: ")
texto = texto.lower()

def contar_vocales(a):
    contador_vocales = 0
    vocales = ["a","e","i","o","u"]
    for caracter in a:
        if caracter in vocales:
            contador_vocales += 1
    return contador_vocales

cantidad_vocales = contar_vocales(texto)

print("La cantidad de vocales en el texto es: " + str(cantidad_vocales))


