
from funciones import *

# ====================================================================
# TPO - GRUPO 3
# ====================================================================

# Archivo principal - main.py
def main():
    opcion = 0
    pilotos=[]
    pilotos=llenar()
    while opcion != 5:
        mostrarMenu()

        opcion = int(input("Seleccione una opcion (1-5): "))

        if opcion == 1:
            print("\n [Acceso] Registrar Piloto (Alta)")
            print("Status: Funcionalidad Pendiente")
        elif opcion == 2:
            print("\n [Acceso] Eliminar Piloto (Baja)")
            eliminar_piloto(pilotos)
        elif opcion == 3:
            print("\n [Acceso] Modificar Puntos o tiempo promedio")
            print("Status: Funcionalidad Pendiente")
        elif opcion == 4:
            print("\n [Acceso] Informe General")
            informeGeneral(pilotos)
        elif opcion == 5:
            print("\n Saliendo del sistema de Velocity Racing Team ===")
        else:
            print("\n Opcion invalida. Debe elegir un numero entre 1 y 5")
    
            

if __name__ == "__main__":
    main()

import random

pilotos = []

#funcion para registrar pilotos
def registrarPilotos(pilotos):
    print("Se eligio la opcion 1 para registrar pilotos")
    opcion = int(input("ingrese 1 para carga manual o 2 para carga automatica: "))
    while opcion != 1 and opcion != 2:
        opcion = int(input("ingreso invalido, intente nuevamente"))
    if opcion == 1:
        n = int(input("cuantos pilotos desea ingresar (entre 1 y 10)?: "))
        while n<=0 or n>=10:
            n = int(input("numero invalido, intente nuevamente: "))
        for i in range(n):
            nombre = input("ingrese el nombre del piloto (debe tener dos palabras, nombre y apellido): ")
            while len(nombre.strip().split()) != 2:
                nombre = input("nombre invalido, intente nuevamente: ")

            numero = int(input("ingrese el numero identificatorio de monoplaza (debe ser un numero positivo): "))
            while numero <= 0:
               numero = int(input("numero invalido, intente nuevamente: ")) 
            
            escuderia = input("ingrese la escuderia del piloto (el campo no puede quedar vacio: )")
            while len(escuderia) <= 0: 
                escuderia = int(input("escuderia invalida, intente nuevamente: "))
            
            puntos = int(input("ingrese los puntos del piloto (debe ser un numero entero positivo o cero): "))
            while puntos < 0:
                puntos = int(input("valor invalido, ingrese un valor nuevamente: "))
            
            tiempo = float(input("ingrese el tiempo promedio por vuelta (no puede ser negativo): "))
            while tiempo < 0:
                tiempo = float(input("tiempo invalido, intente nuevamente: "))

            presupuesto = float(input("ingrese el presupuesto designado al piloto (debe ser positivo): "))
            while presupuesto < 0:
                presupuesto = float(input("presupuesto invalido, intente nuevamente: "))
            
            abandonos = int(input("ingrese la cantidad de abandonos del piloto en la temporada (debe ser positivo): "))
            while abandonos < 0:
                abandonos = int(input("cantidad de abandonos invalida, intente nuevamente: "))
            
            nuevo_piloto = [nombre, numero, escuderia, puntos, tiempo, presupuesto, abandonos]
            pilotos.append(nuevo_piloto)
            print(f"¡Piloto {nombre} registrado con éxito en la matriz!")
            print(pilotos)

    elif opcion == 2:
        
        nombres_mock = ["Lewis Hamilton", "George Russell", "Carlos Sainz", "Oscar Piastri", "Fernando Alonso", "Pierre Gasly"]
        escuderias_mock = ["Mercedes", "Ferrari", "McLaren", "Aston Martin", "Alpine"]

        n = int(input("¿Cuántos pilotos desea generar automáticamente (entre 1 y 10)?: "))
        while n <= 0 or n > 10:
            n = int(input("Número inválido, intente nuevamente: "))

        for i in range(n):
            
            nombre = random.choice(nombres_mock)
            numero = random.randint(1, 99)                    
            escuderia = random.choice(escuderias_mock)        
            puntos = random.randint(0, 300)                   
            tiempo = round(random.uniform(85.0, 95.0), 2)     
            presupuesto = round(random.uniform(1000000.0, 4000000.0), 2)
            abandonos = random.randint(0, 5)                  

            
            nuevo_piloto = [nombre, numero, escuderia, puntos, tiempo, presupuesto, abandonos]
            pilotos.append(nuevo_piloto)
            
            print(f"¡Piloto {nombre} (#{numero}) generado automáticamente con éxito!")
        
        print("\nMatriz actual de pilotos:")
        print(pilotos)

registrarPilotos(pilotos)
