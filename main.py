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
