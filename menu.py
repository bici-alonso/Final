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
        print("6- Ver lista de espera ordenada")
        print("7- Lista centros de salud")
        print("8- Cirujanos en cada centro de salud")
        print("9- ")
        print("9- Buscar paciente por DNI")
        print("10- Estadisticas de cirujanos")
        print("11- Vehiculos (disponibles y viajes)")
        print("12- Modificar datos") #buscar apciente mediante dni y meodificar dato 
        print("13- ")
        print("0- Cerrar programa")
        opcion = int(input("Seleccione una opcion: "))

        if opcion == 1: 
            print("no disponible.")
            #incucai.clasificar_pac(que_es = "donante")
        elif opcion == 2:
            #incucai.clasificar_pac(que_es = "receptor")
            print("no disponible.")
        elif opcion == 3:
            print("\n--------------------lista donantes---------------")
            for d in Donante.listar(): #ESTO PARA QUE IMPRIMA LISTAS Y VER Q ETSAN BIEN
                print(d)
        elif opcion == 4:
            print("\n---------------------lista receptores------------------")
            for r in Receptor.listar():
                print(r)
        elif opcion == 5:
            paciente = Donante("Zoe", 46821489, "6/11/2005", "F", 1126485713, 1125365869, "O+", "Favaloro", "Donante", fecha_fall= "10/05/2024", hora_fall="14:30", hora_ablacion="15:00", fecha_ablacion="10/05/2024", lista_organos=["corazón", "riñón"]) 
            paciente2 = Receptor("Victoria", 46821487, "25/03/2005", "F", 1135857168, 1158694552, "O+", "Favaloro", "Receptor", org_recib="Corazon", fecha_list_esp="15/05/2024", patologia="cardiopatía", estado="inestable")
            paciente3 = Receptor("Dante", 49291429, "26/06/2009", "M", 1125365869, 1147455246, "B+", "Hospital Italiano", "Receptor", org_recib= "piel", fecha_list_esp="16/04/2023", patologia="cancer", estado="estable")
            paciente4 = Donante("Luis Dalmata", 22456831, "10/12/1986", "M", 11457238, 11225498, "AB-", "Hospital El Cruce", "Doanante", fecha_fall = "26/05/2025", hora_fall= "16:00", hora_ablacion= "16:30", fecha_ablacion= "26/05/2025", lista_organos= ["corazon", "riñon", "piel", "corneas", "higado"])
            paciente5 = Receptor("Andrea Boretti", 39742568, "14/10/2001", "F", 11472394, 11566994, "O-", "Hospital Dr. Clemente Alvarez", "Receptor", org_recib = "Higado", fecha_list_esp = "18/03/2016", patologia = "Cirrosis", estado = "critico")
            incucai.clasificar_pac(paciente_exist = paciente)
            incucai.clasificar_pac(paciente_exist = paciente2)
            incucai.clasificar_pac(paciente_exist = paciente3)
            incucai.clasificar_pac(paciente_exist = paciente4)
            incucai.clasificar_pac(paciente_exist = paciente5)
            print("Pacientes de prueba agregados con éxito.")

        elif opcion == 6:
            print("\n-------Lista de receptores por fecha de ingreso a la lista de espera---------------\n")
            for r in Receptor.lista_espera_ordenada():
                print(r)

        elif opcion == 7:
            nombres = nombrar_centros(centros)
            print("\n-------Los centros de salud disponibles-----------------------------\n")
            for nombre in nombres:
                print(f"- {nombre}")

        elif opcion == 0:
            print("\n¡Gracias por utilizar el programa!")
            break
        else:
            print("\nOpcion no valida. Seleccione una de las opciones enlistadas")