#from INCUCAI.Centros.Centro import Centro
from INCUCAI.Incucai import Incucai
from INCUCAI.Paciente.Donante import Donante
from INCUCAI.Organos.Organo import Organo
from INCUCAI.Paciente.Paciente import Paciente
from INCUCAI.Paciente.Receptor import Receptor
#from INCUCAI.Vehiculo.Vehiculo import Vehiculo
from datetime import time, date


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
            dpaciente1 = Donante("Ana López", 45012345, date(1990, 5, 15), "F", "1123456789", "1198765432", "A+", "Hospital Italiano", "Donante", "02", "24", "07", "35", "11", "04", date(2025, 5, 20), time(14, 0), time(16, 0), date(2025, 5, 21), ["riñón", "corazón"])
            #dpaciente2 = Donante("Carlos Pérez", 43123456, date(1985, 7, 10), "M", "1134567890", "1191234567", "O-", "Favaloro", "Donante", "01", "03", "08", "15", "13", "07", date(2025, 5, 18), time(13, 0), time(15, 0), date(2025, 5, 19), ["hígado"])
            #dpaciente3 = Donante("Luis Gomez", 42456789, date(1992, 2, 22), "M", "1145678901", "1198761234", "B+", "Hospital El Cruce", "Donante", "A11", "A26", "B14", "B18", "DR1", "DR16", date(2025, 5, 25), time(12, 0), time(14, 0), date(2025, 5, 26), ["corneas", "piel"])
            #dpaciente4 = Donante("Lucía Torres", 46098765, date(2000, 11, 5), "F", "1156789012", "1192345678", "AB+", "Hospital Garrahan", "Donante", "A23", "A31", "B38", "B44", "DR15", "DR17", date(2025, 5, 24), time(10, 0), time(12, 0), date(2025, 5, 25), ["hígado", "riñón"])
            #dpaciente5 = Donante("Sofía Díaz", 47000001, date(1999, 8, 13), "F", "1167890123", "1193456789", "O+", "Hospital Zonal Alvear", "Donante", "A24", "A32", "B7", "B41", "DR9", "DR4", date(2025, 5, 23), time(9, 30), time(11, 30), date(2025, 5, 24), ["riñón", "corazón"])
            #dpaciente6 = Donante("Matías Herrera", 42234567, date(1988, 3, 30), "M", "1178901234", "1194567890", "A-", "Hospital de Urgencias", "Donante", date(2025, 5, 21), time(11, 0), time(13, 0), date(2025, 5, 22), ["hígado"])
            #dpaciente7 = Donante("Elena Ríos", 41023456, date(1978, 12, 19), "F", "1189012345", "1195678901", "AB-", "Hospital Papa Francisco", "Donante", date(2025, 5, 19), time(15, 0), time(17, 0), date(2025, 5, 20), ["corneas", "piel"])
            #dpaciente8 = Donante("Diego Luna", 46543210, date(1996, 4, 8), "M", "1190123456", "1196789012", "B-", "Hospital Clemente Alvarez", "Donante", date(2025, 5, 27), time(13, 30), time(15, 30), date(2025, 5, 28), ["corazón", "riñón"])
            #dpaciente9 = Donante("Micaela Suárez", 45987654, date(2001, 6, 17), "F", "1191234567", "1197890123", "A+", "Clinica Mayo SRL", "Donante", date(2025, 5, 26), time(14, 15), time(16, 15), date(2025, 5, 27), ["riñón"])
            #dpaciente10 = Donante("Federico Blanco", 44098765, date(1995, 1, 11), "M", "1192345678", "1198901234", "O-", "Hospital Samic Alem", "Donante", date(2025, 5, 22), time(12, 45), time(14, 45), date(2025, 5, 23), ["corazón", "hígado"])

            rpaciente11 = Receptor("Valentina Rossi", 48012345, date(2002, 5, 10), "F", "1112345678", "1123456789", "A+", "Hospital Italiano", "Receptor", "01", "02", "01", "02", "11", "22", ["riñón"], date(2024, 6, 1), "insuficiencia renal", "inestable")
            #rpaciente12 = Receptor("Julián Navarro", 47876543, date(1998, 4, 22), "M", "1123456789", "1134567890", "O-", "Favaloro", "Receptor", "A2", "A3", "B5", "B6", "DR4", "DR7", ["hígado"], date(2023, 11, 3), "cirrosis", "estable")
            #rpaciente13 = Receptor("Martina Silva", 47765432, date(2004, 8, 5), "F", "1134567890", "1145678901", "B+", "Hospital El Cruce", "Receptor", "A1", "A24", "B8", "B27", "DR3", "DR15", ["corazón"], date(2023, 9, 12), "miocardiopatía", "estable")
            rpaciente14 = Receptor("Bruno Castro", 47654321, date(2001, 10, 19), "M", "1145678901", "1156789012", "AB+", "Hospital Garrahan", "Receptor", "11", "23", "18", "35", "06", "13", ["riñón"], date(2024, 2, 18), "glomerulonefritis", "inestable")
            #rpaciente15 = Receptor("Agustina Paz", 47543210, date(1995, 12, 1), "F", "1156789012", "1167890123", "O+", "Hospital Zonal Alvear", "Receptor", "A2", "A68", "B7", "B44", "DR11", "DR17", ["corneas"], date(2024, 4, 25), "queratocono", "estable")
            #rpaciente16 = Receptor("Lucas Molina", 47432109, date(1993, 7, 7), "M", "1167890123", "1178901234", "A-", "Hospital de Urgencias", "Receptor", "A3", "A30", "B13", "B14", "DR9", "DR10", ["hígado"], date(2024, 1, 6), "hepatitis", "inestable")
            #rpaciente17 = Receptor("Camila Sosa", 47321098, date(2000, 3, 9), "F", "1178901234", "1189012345", "AB-", "Hospital Papa Francisco", "Receptor", "A25", "A66", "B62", "B65", "DR14", "DR16", ["piel"], date(2023, 10, 20), "quemaduras", "inestable")
            #rpaciente18 = Receptor("Tomás Aguirre", 47210987, date(1999, 11, 30), "M", "1189012345", "1190123456", "B-", "Hospital Clemente Alvarez", "Receptor", "A1", "A11", "B27", "B38", "DR1", "DR4", ["corazón"], date(2024, 3, 3), "cardiopatía", "inestable")
            #rpaciente19 = Receptor("Luciana Medina", 47109876, date(1996, 6, 14), "F", "1190123456", "1191234567", "A+", "Clinica Mayo SRL", "Receptor", "A29", "A32", "B35", "B52", "DR2", "DR7", ["riñón"], date(2023, 12, 11), "nefropatía", "estable")
            #rpaciente20 = Receptor("Nicolás Vera", 47098765, date(1997, 2, 4), "M", "1191234567", "1192345678", "O-", "Hospital Samic Alem", "Receptor", "A26", "A33", "B37", "B40", "DR5", "DR12", ["hígado"], date(2024, 5, 9), "insuficiencia hepática", "estable")

            
            #incucai.clasificar_paciente_ya_existente(dpaciente1)
            #incucai.clasificar_paciente_ya_existente(dpaciente2)
            #incucai.clasificar_paciente_ya_existente(dpaciente3)
            #incucai.clasificar_paciente_ya_existente(dpaciente4)
            #incucai.clasificar_paciente_ya_existente(dpaciente5)
            #incucai.clasificar_paciente_ya_existente(dpaciente6)
            #incucai.clasificar_paciente_ya_existente(dpaciente7)
            #incucai.clasificar_paciente_ya_existente(dpaciente8)
            #incucai.clasificar_paciente_ya_existente(dpaciente9)
            #incucai.clasificar_paciente_ya_existente(dpaciente10)
            #incucai.clasificar_paciente_ya_existente(rpaciente11)
            #incucai.clasificar_paciente_ya_existente(rpaciente12)
            #incucai.clasificar_paciente_ya_existente(rpaciente13)
            #incucai.clasificar_paciente_ya_existente(rpaciente14)
            #incucai.clasificar_paciente_ya_existente(rpaciente15)
            #incucai.clasificar_paciente_ya_existente(rpaciente16)
            #incucai.clasificar_paciente_ya_existente(rpaciente17)
            #incucai.clasificar_paciente_ya_existente(rpaciente18)
            #incucai.clasificar_paciente_ya_existente(rpaciente19)
            #incucai.clasificar_paciente_ya_existente(rpaciente20)
            Receptor.agregar(rpaciente11)

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