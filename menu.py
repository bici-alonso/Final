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
    
    print("-------------------------------------INCUCAI-------------------------------------")
    pregunta = int(input("\nDesea incializar el programa? presione 1 para SI o 0 para cerrar:  "))
    
    while not (pregunta == 0 or pregunta == 1):
        print("\nEl numero ingresado debe ser 0 o 1")
        pregunta = int(input("\n¿Desea inicializar el programa? Presione 1 para iniciar, y 0 para cerrar:  "))
    
    if pregunta == 0:
        print("\nMuchas gracias por utilizar el programa!")
        return

    while (pregunta == 1):
        print("\n---------------------------------------MENU PRINCIPAL-------------------------------------")
        print("\n1- Inicializar pacientes anteriores de INCUCAI")
        print("\n2- Agregar donante manualmente")
        print("\n3- Agregar receptor manualmente")
        print("\n4- Ver lista de donantes")
        print("\n5- Ver lista de receptores")
        print("\n6- Ver lista de centros de salud")
        print("\n7- Ver lista de espera de receptores en orden")
        print("\n8- Ver cirujanos en un centro de salud")
        print("\n9- Ver vehiculos disponibles en un centro de salud")
        print("\n10- Estadisticas de tasa de exito de un cirujano")
        print ("\n11- Iniciar protocolo de transplante")
        print("\n12- Buscar informacion de un paciente por DNI")
        print("\n13- Buscar en un centro de salud sus pacientes en lista de espera") #imprime para un centro de salud, todos sus pacientes en espera
        print ("\n14- Buscar receptor por DNI e informar posicion en la lista de espera")
        print("\n15- Modificar datos de un paciente por DNI") #buscar apciente mediante dni y meodificar dato 
        print("\n0- Cerrar programa")
        
        opcion = int(input("Seleccione una opcion: "))
        if opcion == 1: #funciona
            dpaciente1 = Donante("Ana López", 45012345, date(1990, 5, 15), "F", "1123456789", "1198765432", "A+", "Hospital Italiano de La Plata", "Donante", "02", "24", "07", "35", "11", "04", date(2025, 5, 20), time(14, 0), time(16, 0), date(2025, 5, 21), ["riñón", "corazón"])
            dpaciente2 = Donante("Carlos Pérez", 43123456, date(1985, 7, 10), "M", "1134567890", "1191234567", "O-", "Fundacion Favaloro", "Donante", "03", "30", "08", "15", "13", "07", date(2025, 5, 18), time(13, 0), time(15, 0), date(2025, 5, 19), ["hígado"])
            #dpaciente4 = Donante("Lucía Torres", 46098765, date(2000, 11, 5), "F", "1156789012", "1192345678", "AB+", "Hospital Garrahan", "Donante", "23", "31", "35", "44", "13", "17", date(2025, 5, 24), time(10, 0), time(12, 0), date(2025, 5, 25), ["hígado", "riñón"])
            #dpaciente5 = Donante("Sofía Díaz", 47000001, date(1999, 8, 13), "F", "1167890123", "1193456789", "O+", "Hospital Zonal Alvear", "Donante", "24", "32", "07", "44", "11", "17", date(2025, 5, 23), time(9, 30), time(11, 30), date(2025, 5, 24), ["corneas", "corazón"])
            #dpaciente6 = Donante("Matías Herrera", 42234567, date(1988, 3, 30), "M", "1178901234", "1194567890", "A-", "Hospital de Urgencias", "Donante", "22", "30", "31", "54", "13", "17",  date(2025, 5, 21), time(11, 0), time(13, 0), date(2025, 5, 22), ["hígado"])
            #dpaciente7 = Donante("Elena Ríos", 41023456, date(1978, 12, 19), "F", "1189012345", "1195678901", "AB-", "Hospital Papa Francisco", "Donante", "23", "33", "25", "40", "12", "17", date(2025, 5, 19), time(15, 0), time(17, 0), date(2025, 5, 20), ["corneas", "piel"])
            #dpaciente8 = Donante("Diego Luna", 46543210, date(1996, 4, 8), "M", "1190123456", "1196789012", "B-", "Hospital Clemente Alvarez", "Donante", "23", "30", "32", "42", "10", "17", date(2025, 5, 27), time(13, 30), time(15, 30), date(2025, 5, 28), ["corazón", "riñón"])
            #dpaciente9 = Donante("Micaela Suárez", 45987654, date(2001, 6, 17), "F", "1191234567", "1197890123", "A+", "Clinica Mayo SRL", "Donante", "23", "30", "35", "44", "13", "17", date(2025, 5, 26), time(14, 15), time(16, 15), date(2025, 5, 27), ["riñón"])
            #dpaciente10 = Donante("Federico Blanco", 44098765, date(1995, 1, 11), "M", "1192345678", "1198901234", "O-", "Hospital Samic Alem", "Donante", "23", "31", "35", "44", "19", "10",date(2025, 5, 22), time(12, 45), time(14, 45), date(2025, 5, 23), ["corazón", "hígado"])

            rpaciente11 = Receptor("Valentina Rossi", 48012345, date(2002, 5, 10), "F", "1112345678", "1123456789", "A+", "Hospital Garrahan", "Receptor", "02", "24", "07", "44", "11", "15", ["riñón"], date(2024, 6, 1), "insuficiencia renal", "inestable")
            rpaciente12 = Receptor("Julián Navarro", 47876543, date(1998, 4, 22), "M", "1123456789", "1134567890", "O-", "Hospital El Cruce", "Receptor", "03", "30", "05", "15", "13", "07", ["hígado"], date(2023, 11, 3), "cirrosis", "estable")
            #rpaciente13 = Receptor("Martina Silva", 47765432, date(2004, 8, 5), "F", "1134567890", "1145678901", "B+", "Hospital El Cruce", "Receptor", "A1", "A24", "B8", "B27", "DR3", "DR15", ["corazón"], date(2023, 9, 12), "miocardiopatía", "estable")
            #rpaciente14 = Receptor("Bruno Castro", 47654321, date(2001, 10, 19), "M", "1145678901", "1156789012", "AB+", "Hospital Garrahan", "Receptor", "11", "23", "18", "35", "06", "13", ["riñón"], date(2024, 2, 18), "glomerulonefritis", "inestable")
            #rpaciente15 = Receptor("Agustina Paz", 47543210, date(1995, 12, 1), "F", "1156789012", "1167890123", "O+", "Hospital Zonal Alvear", "Receptor", "07", "A68", "07", "44", "11", "17", ["corneas"], date(2024, 4, 25), "queratocono", "estable")
            #rpaciente16 = Receptor("Lucas Molina", 47432109, date(1993, 7, 7), "M", "1167890123", "1178901234", "A-", "Hospital de Urgencias", "Receptor", "03", "30", "13", "14", "09", "10", ["hígado"], date(2024, 1, 6), "hepatitis", "inestable")
            #rpaciente17 = Receptor("Camila Sosa", 47321098, date(2000, 3, 9), "F", "1178901234", "1189012345", "AB-", "Hospital Papa Francisco", "Receptor", "A25", "A66", "B62", "B65", "DR14", "DR16", ["piel"], date(2023, 10, 20), "quemaduras", "inestable")
            #rpaciente18 = Receptor("Tomás Aguirre", 47210987, date(1999, 11, 30), "M", "1189012345", "1190123456", "B-", "Hospital Clemente Alvarez", "Receptor", "A1", "A11", "B27", "B38", "DR1", "DR4", ["corazón"], date(2024, 3, 3), "cardiopatía", "inestable")
            #rpaciente19 = Receptor("Luciana Medina", 47109876, date(1996, 6, 14), "F", "1190123456", "1191234567", "A+", "Clinica Mayo SRL", "Receptor", "A29", "A32", "B35", "B52", "DR2", "DR7", ["riñón"], date(2023, 12, 11), "nefropatía", "estable")
            #rpaciente20 = Receptor("Nicolás Vera", 47098765, date(1997, 2, 4), "M", "1191234567", "1192345678", "O-", "Hospital Samic Alem", "Receptor", "A26", "A33", "B37", "B40", "DR5", "DR12", ["hígado"], date(2024, 5, 9), "insuficiencia hepática", "estable")

            
            incucai.registrar_donante(dpaciente1)
            incucai.registrar_donante(dpaciente2)
            #incucai.registrar_donante(dpaciente4)
            #incucai.registrar_donante(dpaciente5)
            #incucai.registrar_donante(dpaciente6)
            #incucai.registrar_donante(dpaciente7)
            #incucai.registrar_donante(dpaciente8)
            #incucai.registrar_donante(dpaciente9)
            #incucai.registrar_donante(dpaciente10)
            incucai.registrar_receptor(rpaciente11)
            incucai.registrar_receptor(rpaciente12)
            #incucai.registrar_receptor(rpaciente13)
            #incucai.registrar_receptor(rpaciente14)
            #incucai.registrar_receptor(rpaciente15)
            #incucai.registra_receptor(rpaciente16)
            #incucai.registra_receptor(rpaciente17)
            #incucai.registra_receptor(rpaciente18)
            #incucai.registra_receptor(rpaciente19)
            #incucai.registra_receptor(rpaciente20)

            print("Pacientes de prueba agregados con éxito...")
            
            
            
        elif opcion == 2: #no desarrollada 
            #incucai.clasificar_pac(que_es = "receptor")
            print("no disponible.")
            
        elif opcion == 3: #no desarrollada
            print ("opcion no disponible.")
            
        elif opcion == 4: #funciona
            print("\n--------------------DONANTES REGISTRADOS EN INCUCAI:---------------")
            incucai.listar_donantes()
            
            
        elif opcion == 5: #funciona
            print("\n---------------------RECEPTORES REGISTRADOS EN INCUCAI:------------------")
            incucai.listar_receptores()
            
        elif opcion == 6: #funciona
            print("\n---------------------CENTROS DE SALUD REGISTRADOS EN INCUCAI:------------------")
            for nombre_cs in incucai.centros():
                print(f"- {nombre_cs}")
        
        elif opcion == 7:
            print("\n-----------------------------Lista de receptores por fecha de ingreso a la lista de espera-----------------------------\n")
            for r in Receptor.lista_espera_ordenada():
                print(r)

        elif opcion == 8:
            print("\n-----------------------------Ver cirujanos de un centro de salud-----------------------------\n")
            print("\nIngrese centro de salud: \n")

        elif opcion == 9:
            print("\n-----------------------------Ver vehiculos disponibles de un centro de salud-----------------------------")
            print("\nIngrese centro de salud: ")
        
        elif opcion == 10: #no aplica
            print("\n-----------------------------Estadisticas de Cirujano-----------------------------")
            print("\nIngrese nombre del cirujano: ")
        
        elif opcion == 11: #Inicio transplante para un receptor especifico
            print("\nIniciando protocolo de transplante....")
            incucai.pedir_receptor_para_realizar_transplante()

        elif opcion == 12:
            dni = int(input("\nIngrese DNI del paciente a buscar: "))
            paciente = incucai.buscar_paciente_por_dni(dni)
            if paciente:
                print("\n Datos del paciente encontrados: \n")
                print(paciente)
            else:
                print("❌ Paciente no encontrado.")
        
        elif opcion == 13:
            print("\nIngrese centro de salud: ")
        
        elif opcion == 14:
            print("\nIngrese DNI del receptor a buscar: ")
        
        elif opcion ==15:
            print("\nIngrese DNI del paciente a modificar: ")

        elif opcion == 0:
            print("\n¡Gracias por utilizar el programa!")
            break
        else:
            print("\nOpcion no valida. Seleccione una de las opciones enlistadas")