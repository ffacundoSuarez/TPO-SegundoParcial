
from funciones import *

# ====================================================================
# TPO - GRUPO 3
# ====================================================================

# Archivo principal - main.py
def main():
    """
    Funcion principal del sistema Velocity Racing Team.
    Inicializa la lista de pilotos y controla el flujo del menu principal,
    derivando cada opcion a la funcion correspondiente.
    """
    opcion = 0
    pilotos=[]
    pilotos=llenar()
    while opcion != 5:
        mostrarMenu()
        opcion = input("Seleccione una opcion (1-5): ")
        while not opcion.isdigit() or int(opcion) < 0:
                opcion = input("Numero invalido intente nuevamente: ")
        opcion = int(opcion)
        if opcion == 1:
            print("\n [Acceso] Registrar Piloto (Alta)")
            registrarPilotos(pilotos)
        elif opcion == 2:
            print("\n [Acceso] Eliminar Piloto (Baja)")
            n=input("Dime el numero del monoplaza que quieres eliminar: ")
            while not n.isdigit() or int(n) < 0:
                n = input("Numero de monoplaza invalido. Intente nuevamente: ")
            n = int(n)
            pos=buscar_piloto_por_numero(pilotos, n)
            if pos==-1:
                print("Piloto no fue encontrado")
            else:
                decision=input("Estas seguro de que quieres borrarlo, si es asi pon 1, sino pon 0: ")
                if decision==1:
                    eliminar_piloto(pilotos,pos)
                    print("El piloto ha sido eliminado con exito")
                else:
                    print("Piloto no fue eliminado")
        elif opcion == 3:
            print("\n [Acceso] Modificar Puntos o tiempo promedio")
            ModificarPuntos_TiempoPromedio(pilotos)
        elif opcion == 4:
            print("\n [Acceso] Informe General")
            informeGeneral(pilotos)
        elif opcion == 5:
            print("\n Saliendo del sistema de Velocity Racing Team ===")
        else:
            print("\n Opcion invalida. Debe elegir un numero entre 1 y 5")
    
            
if __name__ == "__main__":
    main()
