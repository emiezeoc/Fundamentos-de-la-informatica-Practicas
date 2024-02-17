#Zona de definicion de funciones

def carga_estudiante():
    estudiantes = []
    legajo = int(input("Ingrese el numero de legajo del estudiante (Ingrese 0 para finalizar): "))
    while legajo != 0:
        nombre = input("Ingrese el nombre del estudiante: ")
        apellido = input("Ingrese el apellido del estudiante: ")
        contrasenia = input("Ingrese su contraseña: ")
        estudiantes.append([legajo, nombre, apellido, contrasenia])
        legajo= int(input("Ingrese el numero de legajo del estudiante (Ingrese 0 para finalizar): "))
    return estudiantes

def imprimir_estudiantes(lista):
    for x in lista:
        print(str("Legajo: ") + str(x[0]))
        print(str("Nombre: ") + str(x[1]))
        print(str("Apellido: ") + str(x[2]))
        print(str("Contraseña: ") + str(x[3]))

def buscar_menor_legajo(lista):
    menor_legajo = 9999
    for estudiante in lista:
        if estudiante[0] < menor_legajo:
            menor_legajo = estudiante[0]
    if menor_legajo != 9999:
        return menor_legajo
    else:
        return None
    
#Codigo principal

lista_estudiantes = carga_estudiante()

imprimir_estudiantes(lista_estudiantes)
print(buscar_menor_legajo(lista_estudiantes))

