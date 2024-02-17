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
    for estudiante in lista:
        print(str("Legajo: ") + str(estudiante[0]))
        print(str("Nombre: ") + str(estudiante[1]))
        print(str("Apellido: ") + str(estudiante[2]))
        print(str("Contraseña: ") + str(estudiante[3]))

def buscar_menor_legajo(lista):
    menor_legajo = 9999
    for estudiante in lista:
        if estudiante[0] < menor_legajo:
            menor_legajo = estudiante[0]
    if menor_legajo != 9999:
        return menor_legajo
    else:
        return None

def buscar_nombre_mas_largo(lista):
    nombre_mas_largo = ""
    for estudiante in lista:
        if len(estudiante[1]) > len(nombre_mas_largo):
            nombre_mas_largo = estudiante[1]
    if len(nombre_mas_largo) > 0:
        return nombre_mas_largo
    else:
        return None

def controlar_clave(lista):
    for estudiante in lista:
        if len(estudiante[3]) >= 6 and estudiante[3].isdigit():
            print("La contraseña de " + str(estudiante[0]) + " es correcta.")
        else:
            print("La contraseña de " + str(estudiante[0]) + " es incorrecta.")



#Codigo principal

lista_estudiantes = carga_estudiante()


print("1-Imprimir los datos de todos los alumnos")
print("2-Imprimir los datos del alumno que tiene el legajo más chico.")
print("3- Imprimir los datos del alumno que tiene el nombre más largo.")
print("4- Imprimir si las contraseñas de cada alumno cumplen con un tamaño mayor a 6 caracteres y terminan con un número.")
print("0- Finalizar el programa")
opciones_menu = int(input("Ingrese un numero para comenzar: "))

while opciones_menu != 0:
    print("1-Imprimir los datos de todos los alumnos")
    print("2-Imprimir los datos del alumno que tiene el legajo más chico.")
    print("3- Imprimir los datos del alumno que tiene el nombre más largo.")
    print("4- Imprimir si las contraseñas de cada alumno cumplen con un tamaño mayor a 6 caracteres y terminan con un número.")
    print("0- Finalizar el programa")
    opciones_menu = int(input("Ingrese un numero para continuar: "))
    
    
    if opciones_menu == 1:
        imprimir_estudiantes(lista_estudiantes)       
    if opciones_menu == 2:
        print(buscar_menor_legajo(lista_estudiantes))
    if opciones_menu == 3:
        buscar_nombre_mas_largo(lista_estudiantes)
    if opciones_menu == 4:
        controlar_clave(lista_estudiantes)
    else:
        print("Numero no valido, por favor ingrese nuevamente un numero")
        print("1-Imprimir los datos de todos los alumnos")
        print("2-Imprimir los datos del alumno que tiene el legajo más chico.")
        print("3- Imprimir los datos del alumno que tiene el nombre más largo.")
        print("4- Imprimir si las contraseñas de cada alumno cumplen con un tamaño mayor a 6 caracteres y terminan con un número.")
        print("0- Finalizar el programa")
opciones_menu = int(input("Ingrese un numero para continuar: "))
    

