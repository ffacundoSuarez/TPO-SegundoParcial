def llenar():
    """Retorna matriz 10x7 con datos de pilotos F1."""
    return [
        ["Max Verstappen", 1, "RedBull", 350, 87.45, 2500000.00, 1],
        ["Charles Leclerc", 16, "Ferrari", 280, 88.15, 2200000.00, 1],
        ["Lando Norris", 4, "McLaren", 245, 88.30, 2100000.00, 2],
        ["Franco Colapinto", 81, "Velocity Racing", 45, 89.20, 1500000.00, 2],
        ["Lewis Hamilton", 44, "Mercedes", 310, 87.90, 2800000.00, 0],
        ["Sergio Pérez", 11, "RedBull", 198, 88.60, 2000000.00, 3],
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

                





