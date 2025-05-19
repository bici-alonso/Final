#from INCUCAI.Centros.Centro import Centro
from INCUCAI.Incucai import Incucai
from INCUCAI.Paciente.Donante import Donante
#from INCUCAI.Organos.Organo import Organo
from INCUCAI.Paciente.Paciente import Paciente
from INCUCAI.Paciente.Receptor import Receptor
#from INCUCAI.Vehiculo.Vehiculo import Vehiculo


def menu ():
    incucai = Incucai()
    #---------------------------------------------------------------- MENU ---------------------------------------------------------------------------
    print("INICIO DEL PROGRAMA")
    pregunta = int(input("Desea incializar el programa? presione 1 para SI o 0 para cerrar"))
    
    while not (pregunta == 0 or pregunta == 1):
        print("El numero ingresado debe ser 0 o 1")
        pregunta = int(input("¿Desea inicializar el programa? Presione 1 para iniciar, y 0 para cerrar: "))
    
    if pregunta == 0:
        print("Muchas gracias por utilizar el programa!")
        return

    while (pregunta == 1):
        print("\n-------------MENU PRINCIPAL-----------")
        print("1- Agregar donante")
        print("2- Agregar Receptor")
        print("3- Ver lista de donantes")
        print("4- Ver lista de receptores")
        print("0- Cerrar programa")
        opcion = int(input("Seleccione una opcion: "))

        if opcion == 1: 
            incucai.clasificar_pac(que_es = "donante")
        elif opcion == 2:
            incucai.clasificar_pac(que_es = "receptor")
        elif opcion == 3:
            print("--------------------lista donantes---------------")
            for d in Donante.listar(): #ESTO PARA QUE IMPRIMA LISTAS Y VER Q ETSAN BIEN
                print(d)
        elif opcion == 4:
            print("---------------------lista receptores------------------")
            for r in Receptor.listar():
                print(r)
        elif opcion == 0:
            print("¡Gracias por utilizar el programa!")
            break
        else:
            print("Opcion no valida. Seleccione una de las opciones")