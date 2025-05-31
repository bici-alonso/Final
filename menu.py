from INCUCAI.Incucai import Incucai
from INCUCAI.Paciente.Donante import Donante
from INCUCAI.Organos.Organo import Organo
from INCUCAI.Paciente.Paciente import Paciente
from INCUCAI.Paciente.Receptor import Receptor
from INCUCAI.Vehiculo.Helicoptero import Helicoptero
from INCUCAI.Vehiculo.Avion import Avion
from INCUCAI.Vehiculo.Ambulancia import Ambulancia
from datetime import time, date
from INCUCAI.Centros.Centro import Centro_de_salud
from INCUCAI.Centros.Cirujanos.General import General
from INCUCAI.Centros.Cirujanos.Especialista import Especialista

def menu ():
    
    incucai = Incucai()
    
    print("-------------------------------------INCUCAI-------------------------------------")
    
    
    pregunta = None

    while pregunta not in [0, 1]:
        try:
            pregunta = int(input("\n¿Desea inicializar el programa? Presione 1 para INICIAR  o 0 para CERRAR: "))
            if pregunta not in [0, 1]:
                print("❌ El número ingresado debe ser 0 o 1.")
        except ValueError:
            print("❌ Entrada inválida. Solo puede ingresar 0 o 1.")
        
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
        print("\n8- Iniciar protocolo de transplante")
        print("\n9- Buscar informacion de un paciente por DNI")
        print("\n10- Buscar en un centro de salud sus pacientes en lista de espera") #imprime para un centro de salud, todos sus pacientes en espera
        print("\n11- Buscar receptor por DNI e informar posicion en la lista de espera")
        print("\n0- Cerrar programa")
        
        opcion = int(input("Seleccione una opcion: "))
        if opcion == 1: #funciona

            dpaciente1 = Donante("Ana López", 45012345, date(1990, 5, 15), "F", "1123456789", "1198765432", "A+", "Hospital Italiano de La Plata", "Donante", "02", "24", "07", "35", "11", "04", date(2025, 5, 20), time(14, 0), time(16, 0), date(2025, 5, 21), ["rinon"])
            dpaciente2 = Donante("Carlos Pérez", 43123456, date(1985, 7, 10), "M", "1134567890", "1191234567", "O-", "Fundacion Favaloro", "Donante", "03", "30", "08", "15", "13", "07", date(2025, 5, 18), time(13, 0), time(15, 0), date(2025, 5, 19), ["rinon", "corazon"])
            '''dpaciente4 = Donante("Lucía Torres", 46098765, date(2000, 11, 5), "F", "1156789012", "1192345678", "A-", "Hospital Garrahan", "Donante", "23", "31", "35", "44", "13", "17", date(2025, 5, 24), time(10, 0), time(12, 0), date(2025, 5, 25), ["hígado", "riñón"])
            dpaciente5 = Donante("Sofía Díaz", 47000001, date(1999, 8, 13), "F", "1167890123", "1193456789", "O+", "Hospital Zonal Alvear", "Donante", "24", "32", "07", "44", "11", "17", date(2025, 5, 23), time(9, 30), time(11, 30), date(2025, 5, 24), ["corneas", "corazón"])
            dpaciente6 = Donante("Matías Herrera", 42234567, date(1988, 3, 30), "M", "1178901234", "1194567890", "A-", "Hospital de Urgencias", "Donante", "22", "30", "31", "54", "13", "17",  date(2025, 5, 21), time(11, 0), time(13, 0), date(2025, 5, 22), ["hígado"])
            dpaciente7 = Donante("Elena Ríos", 41023456, date(1978, 12, 19), "F", "1189012345", "1195678901", "AB-", "Hospital Papa Francisco", "Donante", "23", "33", "25", "40", "12", "17", date(2025, 5, 19), time(15, 0), time(17, 0), date(2025, 5, 20), ["corneas", "piel"])
            dpaciente8 = Donante("Diego Luna", 46543210, date(1996, 4, 8), "M", "1190123456", "1196789012", "B-", "Hospital Clemente Alvarez", "Donante", "23", "30", "32", "42", "10", "17", date(2025, 5, 27), time(13, 30), time(15, 30), date(2025, 5, 28), ["corazón", "riñón"])
            dpaciente9 = Donante("Micaela Suárez", 45987654, date(2001, 6, 17), "F", "1191234567", "1197890123", "A+", "Clinica Mayo SRL", "Donante", "23", "30", "35", "44", "13", "17", date(2025, 5, 26), time(14, 15), time(16, 15), date(2025, 5, 27), ["riñón"])
            dpaciente10 = Donante("Federico Blanco", 44098765, date(1995, 1, 11), "M", "1192345678", "1198901234", "O-", "Hospital Samic Alem", "Donante", "23", "31", "35", "44", "19", "10",date(2025, 5, 22), time(12, 45), time(14, 45), date(2025, 5, 23), ["corazón", "hígado"])
            '''

            rpaciente11 = Receptor("Valentina Rossi", 48012345, date(2002, 5, 10), "F", "1112345678", "1123456789", "A+", "Fundacion Favaloro", "Receptor", "02", "24", "07", "35", "11", "04", "rinon", date(2024, 6, 1), "insuficiencia renal", "inestable")
            rpaciente12 = Receptor("Julián Navarro", 47876543, date(1998, 4, 22), "M", "1123456789", "1134567890", "O-", "Fundacion Favaloro", "Receptor", "03", "30", "08", "15", "13", "07", "rinon", date(2023, 11, 3), "cirrosis", "estable")
            ''' rpaciente13 = Receptor("Martina Silva", 47765432, date(2004, 8, 5), "F", "1134567890", "1145678901", "A-", "Fundacion Favaloro", "Receptor", "24", "32", "07", "44", "11", "17", "corazón", date(2023, 9, 12), "miocardiopatía", "estable")
            rpaciente14 = Receptor("Bruno Castro", 47654321, date(2001, 10, 19), "M", "1145678901", "1156789012", "AB+", "Hospital Garrahan", "Receptor", "23", "30", "35", "44", "13", "17", "riñón", date(2024, 2, 18), "glomerulonefritis", "inestable")
            rpaciente15 = Receptor("Agustina Paz", 47543210, date(1995, 12, 1), "F", "1156789012", "1167890123", "O+", "Hospital Zonal Alvear", "Receptor", "24", "32", "07", "44", "11", "17", "corneas", date(2024, 4, 25), "queratocono", "estable")
            rpaciente16 = Receptor("Lucas Molina", 47432109, date(1993, 7, 7), "M", "1167890123", "1178901234", "A-", "Hospital de Urgencias", "Receptor", "22", "30", "31", "54", "13", "17", "hígado", date(2024, 1, 6), "hepatitis", "inestable")
            rpaciente17 = Receptor("Camila Sosa", 47321098, date(2000, 3, 9), "F", "1178901234", "1189012345", "AB-", "Hospital Papa Francisco", "Receptor", "23", "33", "25", "40", "12", "17", "piel", date(2023, 10, 20), "quemaduras", "inestable")
            rpaciente18 = Receptor("Tomás Aguirre", 47210987, date(1999, 11, 30), "M", "1189012345", "1190123456", "B-", "Hospital Clemente Alvarez", "Receptor", "23", "30", "32", "42", "10", "17", "corazón", date(2024, 3, 3), "cardiopatía", "inestable")
            rpaciente19 = Receptor("Luciana Medina", 47109876, date(1996, 6, 14), "F", "1190123456", "1191234567", "A+", "Clinica Mayo SRL", "Receptor", "23", "30", "35", "44", "13", "17", "riñón", date(2023, 12, 11), "nefropatía", "estable")
            rpaciente20 = Receptor("Nicolás Vera", 47098765, date(1997, 2, 4), "M", "1191234567", "1192345678", "O-", "Hospital Samic Alem", "Receptor", "23", "31", "35", "44", "19", "10", "hígado", date(2024, 5, 9), "insuficiencia hepática", "estable")
            '''

            helicoptero4 = Helicoptero(150, "AA150AA", "Fundacion Favaloro")
            avion4 = Avion(280, "AB456AP", "Fundacion Favaloro")
            ambulancia4 = Ambulancia(80, "CPP189", "Fundacion Favaloro")

            '''
            helicoptero1 = Helicoptero(150, "AA150AA", "Hospital Garrahan")
            avion1 = Avion(280, "AB456AP", "Hospital Garrahan")
            ambulancia1 = Ambulancia(80, "CPP189", "Hospital Garrahan")
            helicoptero2 = Helicoptero(150, "AA150AA", "Clinica Mayo SRL")
            avion2 = Avion(280, "AB456AP", "Clinica Mayo SRL")
            ambulancia2 = Ambulancia(80, "CPP189", "Clinica Mayo SRL")
            helicoptero3 = Helicoptero(150, "AA150AA", "Hospital El Cruce")
            avion3 = Avion(280, "AB456AP", "Hospital El Cruce")
            ambulancia3 = Ambulancia(80, "CPP189", "Hospital El Cruce")
            helicoptero5 = Helicoptero(150, "AA150AA", "Hospital General de Niños Dr. R. Gutierrez")
            avion5 = Avion(280, "AB456AP", "Hospital General de Niños Dr. R. Gutierrez")
            ambulancia5 = Ambulancia(80, "CPP189", "Hospital General de Niños Dr. R. Gutierrez")
            helicoptero6 = Helicoptero(150, "AA150AA", "Hospital Italiano de La Plata")
            avion6 = Avion(280, "AB456AP", "Hospital Italiano de La Plata")
            ambulancia6 = Ambulancia(80, "CPP189", "Hospital Italiano de La Plata")
            helicoptero7 = Helicoptero(150, "AA150AA", "Hospital Universitario Austral")
            avion7 = Avion(280, "AB456AP", "Hospital Universitario Austral")
            ambulancia7 = Ambulancia(80, "CPP189", "Hospital Universitario Austral")
            helicoptero8 = Helicoptero(150, "AA150AA", "Hospital Gral. de Agudos Carlos G. Durand")
            avion8 = Avion(280, "AB456AP", "Hospital Gral. de Agudos Carlos G. Durand")
            ambulancia8 = Ambulancia(80, "CPP189", "Hospital Gral. de Agudos Carlos G. Durand")
            helicoptero9 = Helicoptero(150, "AA150AA", "Sanatorio Pasteur")
            avion9 = Avion(280, "AB456AP", "Sanatorio Pasteur")
            ambulancia9 = Ambulancia(80, "CPP189", "Sanatorio Pasteur")
            helicoptero10 = Helicoptero(150, "AA150AA", "Hospital Zonal Alvear")
            avion10 = Avion(280, "AB456AP", "Hospital Zonal Alvear")
            ambulancia10 = Ambulancia(80, "CPP189", "Hospital Zonal Alvear")
            helicoptero11 = Helicoptero(150, "AA150AA", "Hospital de Urgencias")
            avion11 = Avion(280, "AB456AP", "Hospital de Urgencias")
            ambulancia11 = Ambulancia(80, "CPP189", "Hospital de Urgencias")
            helicoptero12 = Helicoptero(150, "AA150AA", "Hospital El Carmen")
            avion12 = Avion(280, "AB456AP", "Hospital El Carmen")
            ambulancia12 = Ambulancia(80, "CPP189", "Hospital El Carmen")
            helicoptero13 = Helicoptero(150, "AA150AA", "Hospital Samic Alem de autogestión nivel II")
            avion13 = Avion(280, "AB456AP", "Hospital Samic Alem de autogestión nivel II")
            ambulancia13 = Ambulancia(80, "CPP189", "Hospital Samic Alem de autogestión nivel II")
            helicoptero14 = Helicoptero(150, "AA150AA", "Hospital Area Programa Cipoletti Dr. Pedro Moguillansky")
            avion14 = Avion(280, "AB456AP", "Hospital Area Programa Cipoletti Dr. Pedro Moguillansky")
            ambulancia14 = Ambulancia(80, "CPP189", "Hospital Area Programa Cipoletti Dr. Pedro Moguillansky")
            helicoptero15 = Helicoptero(150, "AA150AA", "Hospital Papa Francisco")
            avion15 = Avion(280, "AB456AP", "Hospital Papa Francisco")
            ambulancia15 = Ambulancia(80, "CPP189", "Hospital Papa Francisco")
            helicoptero16 = Helicoptero(150, "AA150AA", "Hospital Dr. Guillermo Rawson")
            avion16 = Avion(280, "AB456AP", "Hospital Dr. Guillermo Rawson")
            ambulancia16 = Ambulancia(80, "CPP189", "Hospital Dr. Guillermo Rawson")
            helicoptero17 = Helicoptero(150, "AA150AA", "Hospital Dr. Clemente Alvare")
            avion17 = Avion(280, "AB456AP", "Hospital Dr. Clemente Alvare")
            ambulancia17 = Ambulancia(80, "CPP189", "Hospital Dr. Clemente Alvare")
            helicoptero18 = Helicoptero(150, "AA150AA", "Hospital Regional Rio Grande")
            avion18 = Avion(280, "AB456AP", "Hospital Regional Rio Grande")
            ambulancia18 = Ambulancia(80, "CPP189", "Hospital Regional Rio Grande")
            '''

            '''general = General("Juana", "Hospital Garrahan")
            especialista = Especialista("Paloma", "Hospital Garrahan", "gastroenterologo")

            general1 = General("Juana", "Clinica Mayo SRL")
            especialista1 = Especialista("Paloma", "Clinica Mayo SRL", "gastroenterologo")

            general2 = General("Juana", "Fundacion Favaloro")
            especialista2 = Especialista("Paloma", "Fundacion Favaloro", "cardiovascular")'''

            #HOSPITAL ITALIANO DE LA PLATA
            general1 = General("Juana", "Hospital Italiano de La Plata")
            general1 = General("Mateo", "Hospital Italiano de La Plata")
            especialista1 = Especialista("Juan", "Hospital Italiano de La Plata", "gastroenterologo")
            especialista1 = Especialista("Matias", "Hospital Italiano de La Plata", "cardiovascular")
            especialista1 = Especialista ("Marto", "Hospital Italiano de La Plata", "pulmonar")
            especialista1 = Especialista ("Jose", "Hospital Italiano de La Plata", "traumatologo")

            #Hospital General de Niños Dr. R. Gutierrez
            general2 = General("Juana", "Hospital General de Niños Dr. R. Gutierrez")
            general2= General("Mateo", "Hospital General de Niños Dr. R. Gutierrez")
            especialista2 = Especialista("Juan", "Hospital General de Niños Dr. R. Gutierrez", "gastroenterologo")
            especialista2 = Especialista("Matias", "Hospital General de Niños Dr. R. Gutierrez", "cardiovascular")
            especialista2= Especialista ("Angeles", "Hospital General de Niños Dr. R. Gutierrez", "pulmonar")
            especialista2= Especialista ("Josefina", "Hospital General de Niños Dr. R. Gutierrez", "traumatologo")

            #Fundacion Favaloro
            general3 = General("Juana", "Fundacion Favaloro")
            general3= General("Mateo", "Fundacion Favaloro")
            especialista3 = Especialista("Juan", "Fundacion Favaloro", "gastroenterologo")
            especialista3 = Especialista("Matias", "Fundacion Favaloro", "cardiovascular")
            especialista3= Especialista ("Angeles", "Fundacion Favaloro", "pulmonar")
            especialista3= Especialista ("Josefina", "Fundacion Favaloro", "traumatologo")
            especialista3= Especialista ("Pablo", "Fundacion Favaloro", "plastico")


            '''incucai.registrar_vehiculos(helicoptero1)
            incucai.registrar_vehiculos(avion1)
            incucai.registrar_vehiculos(ambulancia1)
            incucai.registrar_vehiculos(helicoptero2)
            incucai.registrar_vehiculos(avion2)
            incucai.registrar_vehiculos(ambulancia2)
            incucai.registrar_vehiculos(helicoptero3)
            incucai.registrar_vehiculos(avion3)
            incucai.registrar_vehiculos(ambulancia3)'''
            incucai.registrar_vehiculos(helicoptero4)
            incucai.registrar_vehiculos(avion4)
            incucai.registrar_vehiculos(ambulancia4)
            '''incucai.registrar_vehiculos(helicoptero5)
            incucai.registrar_vehiculos(avion5)
            incucai.registrar_vehiculos(ambulancia5)
            incucai.registrar_vehiculos(helicoptero6)
            incucai.registrar_vehiculos(avion6)
            incucai.registrar_vehiculos(ambulancia6)
            incucai.registrar_vehiculos(helicoptero7)
            incucai.registrar_vehiculos(avion7)
            incucai.registrar_vehiculos(ambulancia7)
            incucai.registrar_vehiculos(helicoptero8)
            incucai.registrar_vehiculos(avion8)
            incucai.registrar_vehiculos(ambulancia8)
            incucai.registrar_vehiculos(helicoptero9)
            incucai.registrar_vehiculos(avion9)
            incucai.registrar_vehiculos(ambulancia9)
            incucai.registrar_vehiculos(helicoptero10)
            incucai.registrar_vehiculos(avion10)
            incucai.registrar_vehiculos(ambulancia10)
            incucai.registrar_vehiculos(helicoptero11)
            incucai.registrar_vehiculos(avion11)
            incucai.registrar_vehiculos(ambulancia11)
            incucai.registrar_vehiculos(helicoptero12)
            incucai.registrar_vehiculos(avion12)
            incucai.registrar_vehiculos(ambulancia12)
            incucai.registrar_vehiculos(helicoptero13)
            incucai.registrar_vehiculos(avion13)
            incucai.registrar_vehiculos(ambulancia13)
            incucai.registrar_vehiculos(helicoptero14)
            incucai.registrar_vehiculos(avion14)
            incucai.registrar_vehiculos(ambulancia14)
            incucai.registrar_vehiculos(helicoptero15)
            incucai.registrar_vehiculos(avion15)
            incucai.registrar_vehiculos(ambulancia15)
            incucai.registrar_vehiculos(helicoptero16)
            incucai.registrar_vehiculos(avion16)
            incucai.registrar_vehiculos(ambulancia16)
            incucai.registrar_vehiculos(helicoptero17)
            incucai.registrar_vehiculos(avion17)
            incucai.registrar_vehiculos(ambulancia17)
            incucai.registrar_vehiculos(helicoptero18)
            incucai.registrar_vehiculos(avion18)
            incucai.registrar_vehiculos(ambulancia18)'''

            incucai.registrar_cirujano(general3)
            incucai.registrar_cirujano(especialista3)
            incucai.registrar_cirujano(general1)
            incucai.registrar_cirujano(especialista1)
            incucai.registrar_cirujano(general2)
            incucai.registrar_cirujano(especialista2)

            incucai.registrar_donante(dpaciente1)
            incucai.registrar_donante(dpaciente2)
            '''incucai.registrar_donante(dpaciente4)
            incucai.registrar_donante(dpaciente5)
            incucai.registrar_donante(dpaciente6)
            incucai.registrar_donante(dpaciente7)
            incucai.registrar_donante(dpaciente8)
            incucai.registrar_donante(dpaciente9)
            incucai.registrar_donante(dpaciente10)'''
            incucai.registrar_receptor(rpaciente11)
            incucai.registrar_receptor(rpaciente12)
            '''incucai.registrar_receptor(rpaciente13)
            incucai.registrar_receptor(rpaciente14)
            incucai.registrar_receptor(rpaciente15)
            incucai.registrar_receptor(rpaciente16)
            incucai.registrar_receptor(rpaciente17)
            incucai.registrar_receptor(rpaciente18)
            incucai.registrar_receptor(rpaciente19)
            incucai.registrar_receptor(rpaciente20)'''

            print("Pacientes de prueba agregados con éxito...")
            
            
        elif opcion == 2: #funciona
            incucai.carga_manual_receptor_nuevo()
            
            
        elif opcion == 3: #funciona
            incucai.carga_manual_donante_nuevo()
            
            
        elif opcion == 4: #funciona
            print("\n--------------------DONANTES REGISTRADOS EN INCUCAI:---------------")
            incucai.listar_donantes()
            
            
        elif opcion == 5: #funciona
            print("\n---------------------RECEPTORES REGISTRADOS EN INCUCAI:------------------")
            incucai.listar_receptores()
            
        elif opcion == 6: #funciona
            print("\n---------------------CENTROS DE SALUD REGISTRADOS EN INCUCAI:------------------")
            incucai.mostrar_centros_salud()
        
        elif opcion == 7: #funciona
            print("\n-----------------------------Lista de receptores por fecha de ingreso a la lista de espera-----------------------------\n")
            incucai.lista_espera_ordenada()
        
        elif opcion == 8: #Inicio transplante para un receptor especifico
            print("\nIniciando protocolo de transplante....")
            incucai.pedir_receptor_para_realizar_transplante()

        elif opcion == 9: #funciona
            dni = int(input("\nIngrese DNI del paciente a buscar: "))
            paciente = incucai.buscar_paciente_por_dni(dni)
            if paciente:
                print("\n Datos del paciente encontrados: \n")
                print(paciente)
            else:
                print("❌ Paciente no encontrado.")
        
        
        elif opcion == 10: #funciona
            print("\n📍 Centros de salud disponibles:")
            incucai.mostrar_centros_salud()
            
            nombre_centro = input("\n▶ Ingrese exactamente el nombre del centro de salud: ").strip()

            if incucai.centro_valido(nombre_centro):
                incucai.receptores_por_centro_salud(nombre_centro)
            else:
                print("❌ El centro ingresado no está registrado. Verifique el nombre exacto.")
        
        elif opcion == 11: #funciona
            dni_receptor = input("\nIngrese DNI del receptor a buscar: ").strip()
            receptor = incucai.buscar_receptor_por_dni(dni_receptor)
            if receptor:
                print("\n✅ Datos del paciente encontrados:\n")
                print(receptor)
            else:
                print("❌ Paciente no encontrado.")

        elif opcion == 0:
            print("\n¡Gracias por utilizar el programa!")
            break
        else:
            print("\nOpcion no valida. Seleccione una de las opciones enlistadas")