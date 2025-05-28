#from INCUCAI.Centros.Centro import Centro
from INCUCAI.Incucai import Incucai
from INCUCAI.Paciente.Donante import Donante
from INCUCAI.Organos.Organo import *
from INCUCAI.Paciente.Paciente import Paciente
from INCUCAI.Paciente.Receptor import Receptor
#from INCUCAI.Vehiculo.Vehiculo import Vehiculo


def menu ():
    incucai = Incucai()
    
    
    '''paciente= Paciente("Zoe", 46821489, "6/11/2005", "F", 1126485713, 1125365869, "0+", "Favaloro", "Donante") #esta carga deberia resolverse con la funcion agregar
    paciente2=Paciente("Vicky", 46821489, "25/03/2005", "F", 1135857168, 1158694552, "0+", "Favaloro", "Receptor" )
    incucai.clasificar_pac(paciente_exist=paciente)
    incucai.clasificar_pac(paciente_exist=paciente2)'''
    
    #---------------------------------------------------------------- MENU ---------------------------------------------------------------------------
    print("------------------------INICIO DEL PROGRAMA-----------------------------")
    pregunta = int(input("\nDesea incializar el programa? presione 1 para SI o 0 para cerrar:  "))
    
    while not (pregunta == 0 or pregunta == 1):
        print("\nEl numero ingresado debe ser 0 o 1")
        pregunta = int(input("\n¿Desea inicializar el programa? Presione 1 para iniciar, y 0 para cerrar:  "))
    
    if pregunta == 0:
        print("\nMuchas gracias por utilizar el programa!")
        return

    while (pregunta == 1):
        print("\n-------------MENU PRINCIPAL-----------")
        print("1- Agregar donante")
        print("2- Agregar Receptor")
        print("3- Ver lista de donantes")
        print("4- Ver lista de receptores")
        print("5- Agregar los pacientes ya cargados")
        print("0- Cerrar programa")
        opcion = int(input("Seleccione una opcion: "))

        if opcion == 1: 
            incucai.clasificar_pac(que_es = "donante")
        elif opcion == 2:
            incucai.clasificar_pac(que_es = "receptor")
        elif opcion == 3:
            print("\n--------------------lista donantes---------------")
            for d in Donante.listar(): #ESTO PARA QUE IMPRIMA LISTAS Y VER Q ETSAN BIEN
                print(d)
        elif opcion == 4:
            print("\n---------------------lista receptores------------------")
            for r in Receptor.listar():
                print(r)
        elif opcion == 5:
            paciente= Donante("Zoe", 46821489, "6/11/2005", "F", 1126485713, 1125365869, "0+", "Favaloro", "Donante", fecha_fall= "10/05/2024", hora_fall="14:30", hora_ablacion="15:00", fecha_ablacion="10/05/2024", lista_organos=["corazón", "riñón"]) 
            paciente2=Receptor("Vicky", 46821487, "25/03/2005", "F", 1135857168, 1158694552, "0+", "Favaloro", "Receptor", org_recib="Corazon", fecha_list_esp="15/05/2024", patologia="cardiopatía", estado="inestable")
            paciente3=Receptor("Dante", 49291429, "26/06/2009", "M", 1125365869, 1147455246, "B+", "Hospital Italiano", "Receptor", org_recib= "piel", fecha_list_esp="16/04/2023", patologia="cancer", estado="estable")
            incucai.clasificar_pac(paciente_exist=paciente)
            incucai.clasificar_pac(paciente_exist=paciente2)
            incucai.clasificar_pac(paciente_exist=paciente3)
            print("Pacientes de prueba agregados con éxito.")

        elif opcion == 0:
            print("\n¡Gracias por utilizar el programa!")
            break
        else:
            print("\nOpcion no valida. Seleccione una de las opciones enlistadas")