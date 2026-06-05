# ====================================================================
# TPO - GRUPO 3
# ====================================================================

# Archivo principal - main.py

# Menu de opciones del programa: 
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

def main():
    opcion = 0

    while opcion != 5:
        mostrarMenu()

        opcion = int(input("Seleccione una opcion (1-5): "))

        if opcion == 1:
            print("\n [Acceso] Registrar Piloto (Alta)")
            print("Status: Funcionalidad Pendiente")
        elif opcion == 2:
            print("\n [Acceso] Eliminar Piloto (Baja)")
            print("Status: Funcionalidad Pendiente")
        elif opcion == 3:
            print("\n [Acceso] Modificar Puntos o tiempo promedio")
            print("Status: Funcionalidad Pendiente")
        elif opcion == 4:
            print("\n [Acceso] Informe General")
            print("Status: Funcionalidad Pendiente")
        elif opcion == 5:
            print("\n Saliendo del sistema de Velocity Racing Team ===")
        else:
            print("\n Opcion invalida. Debe elegir un numero entre 1 y 5")
    
            

if __name__ == "__main__":
    main()