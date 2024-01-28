#nombre
#puntaje
#goles a favor

# Zona de definicion de funciones

def armar_equipo():
    lista_equipos = []
    nombre_equipo = input("Ingrese el nombre del equipo(coloque ZZZ para terminar el programa): ").upper()
    while nombre_equipo != "ZZZ":
        puntaje_equipo = int(input("Ingrese el puntaje del equipo: "))
        goles_a_favor = int(input("Ingrese la cantidad de goles a favor: "))
        lista_equipos.append([nombre_equipo,puntaje_equipo,goles_a_favor])
        nombre_equipo = input("Ingrese el nombre del equipo(coloque fin para terminar el programa): ").upper()
    return lista_equipos

def imprimir_goles_primero_ultimo():
    return 

#Codigo principal

print(armar_equipo())
