def llenar():
    """Retorna matriz 10x7 con datos de pilotos F1."""
    return [
        ["Max Verstappen", 1, "RedBull", 350, 87.45, 2500000.00, 1],
        ["Charles Leclerc", 16, "Ferrari", 280, 88.15, 2200000.00, 1],
        ["Lando Norris", 4, "McLaren", 245, 88.30, 2100000.00, 2],
        ["Franco Colapinto", 81, "Velocity Racing", 45, 89.20, 1500000.00, 2],
        ["Lewis Hamilton", 44, "Mercedes", 310, 87.90, 2800000.00, 0],
        ["Sergio Pérez", 11, "RedBull", 180, 88.85, 2000000.00, 3],
        ["Carlos Sainz", 55, "Ferrari", 265, 88.25, 2150000.00, 1],
        ["Oscar Piastri", 81, "McLaren", 180, 88.75, 1800000.00, 1],
        ["George Russell", 63, "Mercedes", 220, 88.50, 1950000.00, 2],
        ["Fernando Alonso", 14, "Aston Martin", 120, 89.50, 1900000.00, 3]
    ]
    
def ModificarPuntos_TiempoPromedio(pilotos):
    """
    Permite modificar el puntaje o tiempo de los pilotos
    """

    print("\n  --- Modificar Puntos o Tiempo Promedio  ---")

    # Busqueda del piloto
    busqueda = int(input("Ingrese el nombre del piloto o el numero de monoplaza a buscar: "))

    id_piloto = -1
    cantidad_pilotos = len(pilotos)
    i = 0

    while i < cantidad_pilotos and id_piloto == -1:
        if pilotos[i][0].lower() == busqueda.lower() or pilotos[i][1] == int(busqueda):
            id_piloto = i
        i += 1

    if id_piloto == -1:
        print("No se encontro ningun piloto con los datos ingresados.")
    else:
        piloto = pilotos[id_piloto]
        opcion = 0
        while opcion != 3: 
            print(f"\n=========================================")
            print(f"Piloto: {piloto[0]} | Monoplaza: #{piloto[1]}")
            print(f"Valores actuales -> Puntos: {piloto[3]} | Tiempo: {piloto[4]} segs")
            print(f"=========================================")
            print("1. Modificar Puntos Acumulados")
            print("2. Modificar Tiempo Promedio por Vuelta")
            print("3. Volver al menú principal")
            print("=========================================")
            
            opcion = int(input("Seleccione una opcion (1-3)"))

            if opcion == 1:
                puntos_sumar = -1

                while puntos_sumar < 0:
                    entrada_puntos = float(input("\n Ingrese la nueva cantidad de puntos (enteros >= 0)"))


def eliminar_piloto(pilotos):
    n=int(input("Dime el numero del monoplaza que quieres eliminar: "))
    f=0
    while f < len(pilotos) and pilotos[f][1] != n:
        f+=1
    if f<len(pilotos):
        decision=int(input("Estas seguro de que quieres borrarlo, si es asi pon 1, sino pon 0: "))
        if decision==1:
            pilotos.pop(f)
            print("El piloto ha sido eliminado con exito")
        else:
            print("No se ha eliminado el piloto")
    else:
        print("No encontrado")
        
def mostrarMenu():
    print("\n=========================================")
    print("SISTEMA DE GESTIÓN: VELOCITY RACING TEAM")
    print("=========================================")
    print("1. Registrar piloto (Alta)")
    print("2. Eliminar piloto (Baja)")
    print("3. Modificar puntos o tiempo promedio (Modificación)")
    print("4. Informe General - Visualización de los datos")
    print("5. Salir")
    print("=========================================")
    
def ordenarPilotos(pilotos):
    '''Ordenamiento por puntos (mayor a menor), desempate por tiempo promedio (menor a mayor)'''
    for recorrido in range(1, len(pilotos)):
        for j in range(len(pilotos) - recorrido):
            if pilotos[j][3] < pilotos[j+1][3]:  
                aux=pilotos[j]
                pilotos[j]=pilotos[j+1]
                pilotos[j+1]=aux
            elif pilotos[j][3] == pilotos[j+1][3]:
                if pilotos[j][4] > pilotos[j+1][4]:
                    aux=pilotos[j]
                    pilotos[j]=pilotos[j+1]
                    pilotos[j+1]=aux

def informeGeneral(pilotos):
    '''Mostrar el informe general'''
    ordenarPilotos(pilotos)
    mostrarPilotos(pilotos)
    
def mostrarPilotos(pilotos):
    print("="*len(f"{'Piloto':<20} {'Nº':<4} {'Equipo':<18} {'Puntos':<8} {'Tiempo Prom':<12} {'Salario':<15} {'Podios':<6}"))
    print(f"{'Piloto':<20} {'Nº':<4} {'Equipo':<18} {'Puntos':<8} {'Tiempo Prom':<12} {'Salario':<15} {'Podios':<6}")
    print("-"*len(f"{'Piloto':<20} {'Nº':<4} {'Equipo':<18} {'Puntos':<8} {'Tiempo Prom':<12} {'Salario':<15} {'Podios':<6}"))
    for p in pilotos:
        print(f"{p[0]:<20} {p[1]:<4} {p[2]:<18} {p[3]:<8} {p[4]:<12} ${p[5]:<14} {p[6]:<6}")
    print("="*len(f"{'Piloto':<20} {'Nº':<4} {'Equipo':<18} {'Puntos':<8} {'Tiempo Prom':<12} {'Salario':<15} {'Podios':<6}"))

