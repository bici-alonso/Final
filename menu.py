from INCUCAI.Incucai import Incucai



class Menu:
    """
    Clase que representa el menú principal de interacción con el sistema INCUCAI.

    Esta clase ofrece una interfaz de texto para que el usuario pueda interactuar con las funcionalidades
    del sistema INCUCAI, como registrar pacientes, consultar información, y gestionar donaciones y trasplantes.

    Atributos:
    ----------
    incucai : Incucai
        Instancia del sistema central que contiene la lógica principal de gestión de pacientes, centros,
        órganos y procedimientos de trasplante.

    Métodos:
    --------
    menu():
        Inicia la interfaz de usuario por consola, permite seleccionar opciones del menú y ejecuta
        las acciones correspondientes.
    """
    def __init__(self):
        """
        Constructor del menú. Inicializa una instancia del sistema INCUCAI.
        """
        self.incucai = Incucai()

    def menu (self):
        """
        Muestra el menú principal del sistema INCUCAI y gestiona la interacción con el usuario.

        El menú incluye opciones para:
            - Inicializar pacientes y centros con datos de prueba
            - Registrar manualmente donantes y receptores
            - Listar donantes, receptores y centros de salud
            - Consultar listas de espera y compatibilidades
            - Realizar procesos de donación y trasplante específicos
            - Buscar información sobre pacientes y centros

        El programa continúa ejecutándose en bucle hasta que el usuario seleccione la opción de salida (0).
        """
        incucai = Incucai()
        print("-------------------------------------------------------    INCUCAI    ----------------------------------------------------")
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
            print("\n8- Iniciar protocolo de transplante") # !!
            print("\n9- Buscar informacion de un paciente por DNI")
            print("\n10- Buscar en un centro de salud sus pacientes en lista de espera")
            print("\n11- Buscar receptor por DNI e informar posicion en la lista de espera")
            print("\n12- Donacion especifica entre un donante y un receptor por DNI") 
            print("\n13- Revisar compatibilidad entre 2 pacientes especificos")
            print("\n14- Imprimir informacion sobre un centro de salud") 
            print("\n15- Informacion sobre INCUCAI")
            print("\n0- Cerrar programa")
            
            try:
                opcion = int(input("Seleccione una opción: "))
            except ValueError:
                print("❌ Entrada inválida. Por favor ingrese un número entero.")
                continue  # vuelve a mostrar el menú
            
            if opcion == 1:
                incucai.crear_objetos_prueba()
                    
            elif opcion == 2:
                incucai.carga_manual_donante_nuevo()
                
            elif opcion == 3: 
                incucai.carga_manual_receptor_nuevo()
                    
            elif opcion == 4:
                print("\n--------------------   DONANTES REGISTRADOS EN INCUCAI:  ---------------")
                incucai.listar_donantes()
                
            elif opcion == 5:
                print("\n---------------------   RECEPTORES REGISTRADOS EN INCUCAI:   ------------------")
                incucai.listar_receptores()
                
            elif opcion == 6:
                print("\n---------------------   CENTROS DE SALUD REGISTRADOS EN INCUCAI:   ------------------")
                incucai.mostrar_centros_salud()
            
            elif opcion == 7:
                print("\n-----------------------------Lista de receptores por fecha de ingreso a la lista de espera-----------------------------\n")
                incucai.lista_espera_ordenada()
            
            elif opcion == 8: 
                print("\nIniciando protocolo de transplante....")
                incucai.pedir_receptor_para_realizar_transplante()

            elif opcion == 9: 
                dni = incucai.pedir_dni()
                paciente = incucai.buscar_paciente_por_dni(dni)
                if paciente:
                    print("\n✅ Datos del paciente encontrados: \n")
                    print(paciente)
                else:
                    print("❌ Paciente no encontrado.")
            
            elif opcion == 10:
                print("\n📍 Centros de salud disponibles:")
                incucai.mostrar_centros_salud()
                
                nombre_centro = input("\n▶ Ingrese exactamente el nombre del centro de salud: ").strip()

                if incucai.centro_valido(nombre_centro):
                    incucai.receptores_por_centro_salud(nombre_centro)
                else:
                    print("❌ El centro ingresado no está registrado. Verifique el nombre exacto.")
            
            elif opcion == 11:
                dni_receptor = incucai.pedir_dni("receptor")
                receptor = incucai.buscar_receptor_por_dni(dni_receptor)
                if receptor:
                    print("\n✅ Datos del paciente encontrados:\n")
                    print(receptor)
                else:
                    print("❌ Paciente no encontrado.")

            elif opcion == 12:
                print("\nDonacion especifica entre donante y receptor:")
                incucai.donar_organo_de_donante_a_receptor_especifico()
            
            elif opcion == 13: 
                print ("\nCompatibilidades entre 2 pacientes elegidos:")
                incucai.compatibilidad_2_pacientes()
            
            elif opcion ==14:
                print ("\nINFORMACION DE CENTRO:")
                incucai.mostrar_info_centro_salud()
                
            elif opcion ==15:
                incucai.informacion_incucai()
                
            elif opcion == 0:
                print("\n¡Gracias por utilizar el programa!")
                print("\n -------------------------------------------------------------------------------------------------------")
                break
            
            else: 
                print("\nOpcion no valida. Seleccione una de las opciones enlistadas")