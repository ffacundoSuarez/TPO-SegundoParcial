import random

# Llena la matriz de pilotos
def llenar():
    """
    Carga y retorna la matriz inicial de pilotos con datos predefinidos.
    Cada fila representa un piloto con el siguiente formato:
    [nombre, numero_monoplaza, escuderia, puntos, tiempo_promedio, salario, abandonos]
    """
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

# Mostrador del menu
def mostrarMenu():
    """
    Muestra por pantalla el menu principal del sistema con las opciones disponibles.
    No recibe parametros ni retorna valores.
    """
    print("\n=========================================")
    print("SISTEMA DE GESTIÓN: VELOCITY RACING TEAM")
    print("=========================================")
    print("1. Registrar piloto (Alta)")
    print("2. Eliminar piloto (Baja)")
    print("3. Modificar puntos o tiempo promedio (Modificación)")
    print("4. Informe General - Visualización de los datos")
    print("5. Salir")
    print("=========================================")

# Ejercicio 1 -- Alta del piloto
# Hecho por Tomas Prieto
def registrarPilotos(pilotos):
    """
    Permite registrar uno o varios pilotos en la lista.
    El usuario elige entre carga manual (ingreso por teclado)
    o carga automatica (generacion con valores aleatorios via random).
    Valida cada campo ingresado antes de agregarlo a la lista.
    Parametros:
        pilotos (list): lista principal donde se agregan los nuevos pilotos.
    """
    print("\n--- Se eligió la opción 1 para registrar pilotos ---")
    
    # 1. Validación de la opción de carga
    opcion = input("Ingrese 1 para carga manual o 2 para carga automática: ")
    while opcion != "1" and opcion != "2":
        opcion = input("Ingreso inválido. Intente nuevamente (1 para manual, 2 para automática): ")
    
    # 2. Validación de cuántos pilotos ingresar
    cant_pilotos = input("¿Cuántos pilotos desea ingresar (entre 1 y 10)?: ")
    while not cant_pilotos.isdigit() or int(cant_pilotos) <= 0 or int(cant_pilotos) > 10:
        cant_pilotos = input("Número inválido. Ingrese una cantidad entre 1 y 10: ")
    n = int(cant_pilotos)

    # ================= CARGA MANUAL =================
    if opcion == "1":
        for i in range(n):
            print(f"\n--- Cargando datos del piloto {i+1} de {n} ---")
            
            # Nombre (Debe tener exactamente dos palabras)
            nombre = input("Ingrese el nombre del piloto (debe tener dos palabras, nombre y apellido): ")
            while len(nombre.split()) != 2:
                nombre = input("Nombre inválido (debe tener dos palabras). Intente nuevamente: ")
            
            # Número de monoplaza
            numero = input("Ingrese el número identificatorio de monoplaza (debe ser un número positivo): ")
            while not numero.isdigit() or int(numero) <= 0:
                numero = input("Número inválido. Intente nuevamente: ")
            numero = int(numero)
            
            # Escudería
            escuderia = input("Ingrese la escudería del piloto: ")
            while escuderia == "":
                escuderia = input("El campo no puede quedar vacío. Ingrese la escudería: ")
            
            # Puntos acumulados
            puntos = input("Ingrese los puntos acumulados en el campeonato: ")
            while not puntos.isdigit() or int(puntos) < 0:
                puntos = input("Cantidad de puntos inválida. Intente nuevamente: ")
            puntos = int(puntos)
            
            # Tiempo promedio
            #tiempo = ingresarDecimal("Ingrese el tiempo promedio por vuelta (en segundos): ")
            tiempo=input("Ingrese el tiempo promedio por vuelta (en segundos): ")
            while not tiempo.replace('.', '', 1).isdigit():
                tiempo = input("Tiempo inválido. Intente nuevamente: ")
            tiempo = float(tiempo)
            
            # Presupuesto
            presupuesto = input("Ingrese el presupuesto designado al piloto (USD): ")
            while not presupuesto.replace('.', '', 1).isdigit():
                presupuesto = input("Presupuesto inválido. Intente nuevamente: ")
            presupuesto = float(presupuesto)
            
            # Abandonos
            abandonos = input("Ingrese la cantidad de abandonos del piloto en la temporada: ")
            while not abandonos.isdigit() or int(abandonos) < 0:
                abandonos = input("Cantidad de abandonos inválida. Intente nuevamente: ")
            abandonos = int(abandonos)
            
            # Guardamos el nuevo piloto en la matriz
            nuevo_piloto = [nombre, numero, escuderia, puntos, tiempo, presupuesto, abandonos]
            pilotos.append(nuevo_piloto)
            print(f"¡Piloto {nombre} registrado con éxito en la matriz!")

    # ================= CARGA AUTOMÁTICA =================
    elif opcion == "2":
        # Renombrados de mock a aleatorio.
        nombres_aleatorio = ["Lewis Hamilton", "George Russell", "Carlos Sainz", "Oscar Piastri", "Fernando Alonso", "Pierre Gasly"]
        escuderias_aleatorio = ["Mercedes", "Ferrari", "McLaren", "Aston Martin", "Alpine"]
        
        for i in range(n):
            nombre = random.choice(nombres_aleatorio)
            numero = random.randint(1, 99)
            escuderia = random.choice(escuderias_aleatorio)
            puntos = random.randint(0, 300)
            tiempo = round(random.uniform(85.0, 95.0), 2)
            presupuesto = round(random.uniform(1000000.0, 4000000.0), 2)
            abandonos = random.randint(0, 5)
            
            nuevo_piloto = [nombre, numero, escuderia, puntos, tiempo, presupuesto, abandonos]
            pilotos.append(nuevo_piloto)
            print(f"¡Piloto {nombre} (#{numero}) generado automáticamente con éxito!")

    print("\n--- Matriz actual de pilotos ---")
    print(pilotos)

# Ejercicio 2 -- Baja del piloto
# Hecho por Juan Ignacio Teruya
def eliminar_piloto(pilotos,n):
    """
    Elimina un piloto de la lista a través de la posición del monoplaza.
    Parametros:
        pilotos (list): lista principal de pilotos.
        n (int): posicion del piloto en la lista
    """
    pilotos.pop(n)


# Ejercicio 3 -- Modificacion Puntos o Tiempos de un piloto
# Hecho por Facundo Suarez
def ModificarPuntos_TiempoPromedio(pilotos):
    """
    Permite modificar los puntos acumulados y/o el tiempo promedio por vuelta de un piloto.
    El usuario elige si buscar al piloto por nombre o por numero de monoplaza.
    Una vez encontrado, puede modificar uno o ambos valores en un submenu,
    y volver al menu principal cuando lo desee.
    Parametros:
        pilotos (list): lista principal de pilotos.
    """
    print("\n--- Modificar Puntos o Tiempo Promedio ---")
    print("1. Buscar por nombre")
    print("2. Buscar por numero de monoplaza")

    criterio = int(input("Como desea buscar al piloto? (1-2): "))
    while criterio != 1 and criterio != 2:
        criterio = int(input("Opcion invalida, intente nuevamente (1-2): "))

    id_piloto = -1
    i = 0

    if criterio == 1:
        busqueda = input("Ingrese el nombre del piloto: ")
        while i < len(pilotos) and id_piloto == -1:
            if pilotos[i][0].lower() == busqueda.lower():
                id_piloto = i
            i += 1
    else:
        numero = int(input("Ingrese el numero de monoplaza: "))
        while numero <= 0:
            numero = int(input("Debe ser un numero positivo: "))
        while i < len(pilotos) and id_piloto == -1:
            if pilotos[i][1] == numero:
                id_piloto = i
            i += 1

    if id_piloto == -1:
        print("No se encontro ningun piloto con los datos ingresados.")
        return

    opcion = 0
    while opcion != 3:
        piloto = pilotos[id_piloto]
        print(f"\n=========================================")
        print(f"Piloto: {piloto[0]} | Monoplaza: #{piloto[1]}")
        print(f"Puntos actuales: {piloto[3]} | Tiempo actual: {piloto[4]} segs")
        print(f"=========================================")
        print("1. Modificar Puntos Acumulados")
        print("2. Modificar Tiempo Promedio por Vuelta")
        print("3. Volver al menu principal")
        print("=========================================")

        opcion = int(input("Seleccione una opcion (1-3): "))

        if opcion == 1:
            nuevos_puntos = int(input("Ingrese los nuevos puntos acumulados (entero >= 0): "))
            while nuevos_puntos < 0:
                nuevos_puntos = int(input("Los puntos no pueden ser negativos: "))
            pilotos[id_piloto][3] = nuevos_puntos
            print(f"Puntos actualizados a {pilotos[id_piloto][3]}.")

        elif opcion == 2:
            nuevo_tiempo = float(input("Ingrese el nuevo tiempo promedio en segundos (>= 0): "))
            while nuevo_tiempo < 0:
                nuevo_tiempo = float(input("El tiempo no puede ser negativo: "))
            pilotos[id_piloto][4] = nuevo_tiempo
            print(f"Tiempo actualizado a {pilotos[id_piloto][4]} segs.")

        elif opcion != 3:
            print("Opcion invalida. Elija entre 1 y 3.")



        

# Ejercicio 4 - Informe general: Parte de ordenar los pilotos
# Hecho por Juan Ignacio Teruya
def ordenarPilotos(pilotos):
    """
    Ordena la lista de pilotos usando el algoritmo de burbujeo.
    Criterio principal: puntos acumulados de mayor a menor.
    Criterio de desempate: tiempo promedio por vuelta de menor a mayor.
    Parametros:
        pilotos (list): lista principal de pilotos. Se modifica en lugar (in-place).
    """
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

# Ejercicio 4 - Informe general: Parte de mostrar los pilotos
# Hecho por Juan Ignacio Teruya
def mostrarPilotos(pilotos):
    print("="*len(f"{'Piloto':<20} {'Nº':<4} {'Equipo':<18} {'Puntos':<8} {'Tiempo Prom':<12} {'Salario':<15} {'Podios':<6}"))
    print(f"{'Piloto':<20} {'Nº':<4} {'Equipo':<18} {'Puntos':<8} {'Tiempo Prom':<12} {'Salario':<15} {'Podios':<6}")
    print("-"*len(f"{'Piloto':<20} {'Nº':<4} {'Equipo':<18} {'Puntos':<8} {'Tiempo Prom':<12} {'Salario':<15} {'Podios':<6}"))
    for p in pilotos:
        print(f"{p[0]:<20} {p[1]:<4} {p[2]:<18} {p[3]:<8} {p[4]:<12} ${p[5]:<14} {p[6]:<6}")
    print("="*len(f"{'Piloto':<20} {'Nº':<4} {'Equipo':<18} {'Puntos':<8} {'Tiempo Prom':<12} {'Salario':<15} {'Podios':<6}"))

# Ejercicio 4 -- Informe, que llama a las dos funciones superiores
# Hecho por Juan Ignacio Teruya
def informeGeneral(pilotos):
    """
    Genera el informe general del campeonato.
    Ordena los pilotos por puntos (y tiempo como desempate)
    y luego muestra la tabla completa por pantalla.
    Parametros:
        pilotos (list): lista principal de pilotos.
    """
    ordenarPilotos(pilotos)
    mostrarPilotos(pilotos)

# Busca el monoplaza por número
# Hecho por Juan Ignacio Teruya
def buscar_piloto_por_numero(pilotos, numero):
    """
    Busca un piloto por su número de monoplaza usando un ciclo while.
    
    Parametros:
        pilotos (list): lista principal de pilotos
        numero (int): número a buscar
    
    Retorna:
        int: índice del piloto encontrado, o -1 si no existe
    """
    i = 0
    while i < len(pilotos) and pilotos[i][1] != numero:
        i += 1
    
    if i == len(pilotos):
        return -1
    else:
        return i