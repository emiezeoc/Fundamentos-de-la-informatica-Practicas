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
        nombre_equipo = input("Ingrese el nombre del equipo(coloque ZZZ para terminar el programa): ").upper()
    return lista_equipos

def imprimir_goles_primero_ultimo(lista):
    Goles_primer_equipo = lista[0][2]
    goles_ultimo_equipo = lista[-1][2]
    return print("Los goles del primer equipo son: " + str(Goles_primer_equipo) + ", los goles del ultimo equipo son: " + str(goles_ultimo_equipo))

def imprimir_equipo_campeon(equipos):
    equipo_campeon = equipos[0]

    for equipo in equipos:
        if equipo[1] > equipo_campeon[1]:
            equipo_campeon = equipo 
    return equipo_campeon


#Codigo principal

lista_equipos = armar_equipo()
imprimir_goles_primero_ultimo(lista_equipos)
print(imprimir_equipo_campeon(lista_equipos))