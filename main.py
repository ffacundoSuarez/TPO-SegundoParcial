from funciones import *

# ====================================================================
# TPO - GRUPO 3
# ====================================================================
def ingresar_monoplaza():
    n=input("Dime el numero del monoplaza que quieres eliminar: ")
    while not n.isdigit() or int(n) < 0:
        n = input("Numero de monoplaza invalido. Intente nuevamente: ")
    n = int(n)
    return n

def ejecutar_opcion_eliminar(pilotos):
    print("\n [Acceso] Eliminar Piloto (Baja)")
    n=ingresar_monoplaza()
    pos=buscar_piloto_por_numero(pilotos, n)
    if pos==-1:
        print("Piloto no fue encontrado")
    else:
        decision=input("Estas seguro de que quieres borrarlo, si es asi pon 1, sino pon 0: ")
        if decision=="1":
            eliminar_piloto(pilotos,pos)
            print("El piloto ha sido eliminado con exito")
        else:
            print("Piloto no fue eliminado")

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
            ejecutar_opcion_eliminar(pilotos)
        elif opcion == 3:
            print("\n [Acceso] Modificar Puntos o tiempo promedio")
            print("1. Buscar por nombre")
            print("2. Buscar por numero de monoplaza")

            criterio = input("Como desea buscar al piloto? (1-2): ")
            while not criterio.isdigit() or (int(criterio) != 1 and int(criterio) != 2):
                criterio = input("Opcion invalida, intente nuevamente (1-2): ")
            criterio = int(criterio)

            if criterio == 1:
                nombre = input("Ingrese el nombre del piloto: ")
                pos = buscar_piloto_por_nombre(pilotos, nombre)
            else:
                numero = input("Ingrese el numero de monoplaza: ")
                while not numero.isdigit() or int(numero) <= 0:
                    numero = input("Debe ser un numero entero positivo: ")
                numero = int(numero)
                pos = buscar_piloto_por_numero(pilotos, numero)

            if pos == -1:
                print("No se encontro ningun piloto con los datos ingresados.")
            else:
                MenuModificacion(pilotos, pos)
        elif opcion == 4:
            print("\n [Acceso] Informe General")
            informeGeneral(pilotos)
        elif opcion == 5:
            print("\n Saliendo del sistema de Velocity Racing Team ===")
        else:
            print("\n Opcion invalida. Debe elegir un numero entre 1 y 5")
    
            
if __name__ == "__main__":
    main()