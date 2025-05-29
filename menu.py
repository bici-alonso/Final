#from INCUCAI.Centros.Centro import Centro
from INCUCAI.Incucai import Incucai
from INCUCAI.Paciente.Donante import Donante
from INCUCAI.Organos.Organo import Organo
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
            incucai.listar_donantes()
            #for d in Donante.listar(): #ESTO PARA QUE IMPRIMA LISTAS Y VER Q ETSAN BIEN
             #   print(d)
        elif opcion == 4:
            print("\n---------------------lista receptores------------------")
            incucai.listar_receptores()
            #for r in Receptor.listar():
            #    print(r)
        elif opcion == 5:
            paciente1 = Donante("Zoe Pfeifer", 46821489, "6/11/2005", "F", 1126485713, 1125365869, "O+", "Favaloro", "Donante", fecha_fall= "10/05/2024", hora_fall="14:30", hora_ablacion="15:00", fecha_ablacion="10/05/2024", lista_organos=["corazón", "riñón"]) 
            paciente2 = Receptor("Victoria", 46821487, "25/03/2005", "F", 1135857168, 1158694552, "O+", "Favaloro", "Receptor", org_recib="Corazon", fecha_list_esp="15/05/2024", patologia="cardiopatía", estado="inestable")
            paciente3 = Receptor("Dante", 49291429, "26/06/2009", "M", 1125365869, 1147455246, "B+", "Hospital Italiano", "Receptor", org_recib= "piel", fecha_list_esp="16/04/2023", patologia="cancer", estado="estable")
            paciente4 = Donante("Luis Dalmata", 22456831, "10/12/1986", "M", 11457238, 11225498, "AB-", "Hospital El Cruce", "Doanante", fecha_fall = "26/05/2025", hora_fall= "16:00", hora_ablacion= "16:30", fecha_ablacion= "26/05/2025", lista_organos= ["corazon", "riñon", "piel", "corneas", "higado"])
            paciente5 = Receptor("Andrea Boretti", 39742568, "14/10/2001", "F", 11472394, 11566994, "O-", "Hospital Dr. Clemente Alvarez", "Receptor", org_recib = "Higado", fecha_list_esp = "18/03/2016", patologia = "Cirrosis", estado = "critico")
            '''
            Donante("Ana López", 45012345, date(1990, 5, 15), "F", 1123456789, 1198765432, "A+", "Hospital Italiano", "Donante", date(2025, 5, 20), time(14, 0), time(16, 0), date(2025, 5, 21), ["riñón", "corazón"])
Donante("Carlos Pérez", 43123456, date(1985, 7, 10), "M", 1134567890, 1191234567, "O-", "Favaloro", "Donante",
        date(2025, 5, 18), time(13, 0), time(15, 0), date(2025, 5, 19), ["hígado"])
Donante("Luis Gomez", 42456789, date(1992, 2, 22), "M", 1145678901, 1198761234, "B+", "Hospital El Cruce", "Donante",
        date(2025, 5, 25), time(12, 0), time(14, 0), date(2025, 5, 26), ["corneas", "piel"])
Donante("Lucía Torres", 46098765, date(2000, 11, 5), "F", 1156789012, 1192345678, "AB+", "Hospital Garrahan", "Donante",
        date(2025, 5, 24), time(10, 0), time(12, 0), date(2025, 5, 25), ["hígado", "riñón"])
Donante("Sofía Díaz", 47000001, date(1999, 8, 13), "F", 1167890123, 1193456789, "O+", "Hospital Zonal Alvear", "Donante",
        date(2025, 5, 23), time(9, 30), time(11, 30), date(2025, 5, 24), ["riñón", "corazón"])
Donante("Matías Herrera", 42234567, date(1988, 3, 30), "M", 1178901234, 1194567890, "A-", "Hospital de Urgencias", "Donante",
        date(2025, 5, 21), time(11, 0), time(13, 0), date(2025, 5, 22), ["hígado"])
Donante("Elena Ríos", 41023456, date(1978, 12, 19), "F", 1189012345, 1195678901, "AB-", "Hospital Papa Francisco", "Donante",
        date(2025, 5, 19), time(15, 0), time(17, 0), date(2025, 5, 20), ["corneas", "piel"])
Donante("Diego Luna", 46543210, date(1996, 4, 8), "M", 1190123456, 1196789012, "B-", "Hospital Clemente Alvarez", "Donante",
        date(2025, 5, 27), time(13, 30), time(15, 30), date(2025, 5, 28), ["corazón", "riñón"])
Donante("Micaela Suárez", 45987654, date(2001, 6, 17), "F", 1191234567, 1197890123, "A+", "Clinica Mayo SRL", "Donante",
        date(2025, 5, 26), time(14, 15), time(16, 15), date(2025, 5, 27), ["riñón"])
Donante("Federico Blanco", 44098765, date(1995, 1, 11), "M", 1192345678, 1198901234, "O-", "Hospital Samic Alem", "Donante",
        date(2025, 5, 22), time(12, 45), time(14, 45), date(2025, 5, 23), ["corazón", "hígado"])
'''

            incucai.clasificar_paciente_ya_existente(paciente_existente = paciente1)
            incucai.clasificar_paciente_ya_existente(paciente_existente = paciente2)
            incucai.clasificar_paciente_ya_existente(paciente_existente = paciente3)
            incucai.clasificar_paciente_ya_existente(paciente_existente = paciente4)
            incucai.clasificar_paciente_ya_existente(paciente_existente = paciente5)
            print("Pacientes de prueba agregados con éxito.")

        elif opcion == 6:
            print("\n-------Lista de receptores por fecha de ingreso a la lista de espera---------------\n")
            for r in Receptor.lista_espera_ordenada():
                print(r)

        elif opcion == 7:
            print("\n-------Los centros de salud disponibles-----------------------------\n")
            for nombre_cs in incucai.centros():
                print(f"- {nombre_cs}")

        elif opcion == 0:
            print("\n¡Gracias por utilizar el programa!")
            break
        else:
            print("\nOpcion no valida. Seleccione una de las opciones enlistadas")