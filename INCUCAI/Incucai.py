'''
TRABAJO PRACTICO FINAL - LABO DE PROGRAMACION I. 
SIMULACION SIST. DONACION DE ORGANOS

Alonso Victoria
Pfeifer Zoe
'''
'''

El INCUCAI se encarga de la coordinación y logística de la donación de tejidos y órganos. 
Debido a que su sistema quedó desactualizado por el paso del tiempo, le solicitaron realizar una nueva versión dónde tendrá que mejorar la automatización y
la logística para optimizar la llegada de órganos a los pacientes que se encuentran en la lista de espera. 
Este consta de una lista de receptores, una lista de donantes y una lista de centros de salud habilitados.

El Sistema tiene que permitir:
    -Registrar pacientes nuevos (Validando que no se encuentre en otra lista ni se repita).
    -Quitar de la lista de donantes a aquellos cuyos organos ya han sido utilizados en su totalidad.
    -Quitar de la lista a un receptor una vez que ha recibido su organo exitosamente.
    -Buscar por centro de salud los pacientes de la lista de espera.
    -Buscar un receptor e informar qué prioridad tiene en la lista de espera.
    -Imprimir listado de pacientes donantes y receptores.
    -Realizar correctamente todo el proceso de asignación y derivación de un organo a un receptor,
    contemplando el viaje, la disponibilidad en ese horario de los vehiculos de un centro medico y el tiempo de viaje.

'''

#La clase INCUCAI la uso como manager de mis demas clases --> Permite manejar/linkear mis clases y listas

from INCUCAI.Paciente.Paciente import Paciente
from INCUCAI.Paciente.Donante import Donante #no me esta dejando importar, como esta en carpetas chat me dijo q le ponga ese punto pero tampoco funciona
from INCUCAI.Paciente.Receptor import Receptor #lo dejo asi con todo hecho pero nose si esta funcionando bien porque no puedo correrlo
from INCUCAI.Centros.Centro import Centro_de_salud 
from datetime import datetime

class Incucai:
    
    '''
    El INCUCAI sabe recibir un paciente. Cuando lo hace recibe al Paciente, y lo ingresa.
    
    Si el paciente es donante, al ser ingresado se lo agrega a la lista de pacientes donantes.
    Luego se busca los posibles receptores para cada órgano que el donante puede donar, 
    para esto se busca en su lista de pacientes receptores todos los pacientes que necesitan ese órgano y tienen el mismo tipo de sangre. 
    Finalmente, se elige el receptor, en función a la prioridad del paciente (si tienen la misma prioridad elige al que tiene una fecha anterior de
    ingreso a la lista de espera). En tal caso, se envia el organo correspondiente a la ubicación del paciente
    receptor y se quita de la lista de donantes la disponibilidad de ese organo para ese donante en particular. Si el
    paciente es receptor, se lo agrega a la lista de pacientes receptores, y se busca si hay alguna coincidencia en
    la lista de donantes. De haberlo se despacha el organo para el receptor, actualizando de igual manera la lista
    de donantes.

    '''
    

    def __init__(self):
        #Constructor de INCUCAI
        self.receptores = []
        self.donantes = []
        self.Centros_de_salud = []
        
        
        
    def clasificar_paciente(self, que_es=None, paciente_exist=None):
            if paciente_exist:
            # Si ya se pasó un objeto paciente creado, reviso de que tipo es:
            
                if isinstance(paciente_exist, Donante):
                    if any(p.DNI == paciente_exist.DNI for p in self.donantes + self.receptores): #reviso que no exista un paciente con ese dni ya cargado en mis arrays
                        print(f"Ya existe un paciente del tipo donante con DNI {paciente_exist.DNI}.")
                        return
                    self.donantes.append(paciente_exist)  #agrego al donante a mi array de donantes de incucai
                    
                    #donacion  --> depende si es multiple o de todo
                    self.hacer_donacion(paciente_exist)
                    return
            
                if isinstance(paciente_exist, Receptor):
                    if any(p.DNI == paciente_exist.DNI for p in self.donantes + self.receptores):  #reviso que no exista un paciente con ese dni ya cargado en mis arrays
                        print(f"Ya existe un paciente del tipo receptor con DNI {paciente_exist.DNI}.")
                        return
                    self.receptores.append(paciente_exist)
                    self.buscar_match_receptor(paciente_exist)
                    return
            
        # Si es un paciente base, obtener el tipo
                paciente_base = paciente_exist
                que_es = paciente_base.que_es.lower()
                
            else:
                paciente_base = Paciente.agregar(que_es)

            dni_a_verificar = paciente_base.DNI
            if any(p.DNI == dni_a_verificar for p in self.donantes + self.receptores):
                print(f"Ya existe un paciente con DNI {dni_a_verificar} en el sistema. No se puede agregar.")
                return

            if que_es == "donante":
                self.registrar_donante(paciente_base)
            elif que_es == "receptor":
                self.registrar_receptor(paciente_base)
                

    def registrar_donante(self, paciente_base):
        """
        Registra un donante y maneja la lógica de donación según su estado.
        """
        # Preguntar si está vivo o muerto
        print("\n--- REGISTRO DE DONANTE ---")
        while True:
            donante_vivo = input("¿El donante está vivo? (si/no): ").lower().strip()
            if donante_vivo in ['si', 'sí']:
                esta_vivo = True
                break
            elif donante_vivo in ['no']:
                esta_vivo = False
                break
            else:
                print("❌ Responda con sí o no.")

        if esta_vivo==True:
            # DONANTE VIVO - Un solo órgano
            print("\n--- DONANTE VIVO ---")
            organo_a_donar = input("Ingrese el órgano que va a donar: ").strip().upper()
            
            # Crear donante con un solo órgano
            donante = Donante(
                paciente_base.nombre,
                paciente_base.DNI,
                paciente_base.fecha_nac,
                paciente_base.sexo,
                paciente_base.telefono,
                paciente_base.contacto,
                paciente_base.tipo_sangre,
                paciente_base.centro,
                "donante",
                None,  # fecha_fall
                None,  # hora_fall
                None,  # hora_ablacion - se definirá cuando se programe la cirugía
                None,  # fecha_ablacion
                [organo_a_donar]  # lista con un solo órgano
            )
            
            self.donantes.append(donante)
            print(f"✅ Donante vivo registrado. Órgano disponible: {organo_a_donar}")
            
            #receptor para un organo 
            self.buscar_receptor_organo_especifico (donante, organo_a_donar)
            
        else:
            # DONANTE MUERTO - Todos los órganos
            print("\n--- DONANTE FALLECIDO ---")
            
            # Solicitar datos de fallecimiento
            while True:
                fecha_fall = input("Ingrese fecha de fallecimiento (dd/mm/yyyy): ")
                try:
                    datetime.strptime(fecha_fall, "%d/%m/%Y")
                    break
                except ValueError:
                    print("❌ Fecha inválida. Use el formato dd/mm/yyyy.")

            while True:
                hora_fall = input("Ingrese hora de fallecimiento (HH:MM): ")
                try:
                    datetime.strptime(hora_fall, "%H:%M")
                    break
                except ValueError:
                    print("❌ Hora inválida. Use el formato HH:MM (24 hs).")

            while True:
                fecha_ablacion = input("Ingrese fecha de ablación (dd/mm/yyyy): ")
                try:
                    datetime.strptime(fecha_ablacion, "%d/%m/%Y")
                    break
                except ValueError:
                    print("❌ Fecha inválida. Use el formato dd/mm/yyyy.")

            while True:
                hora_ablacion = input("Ingrese hora de ablación (HH:MM): ")
                try:
                    datetime.strptime(hora_ablacion, "%H:%M")
                    break
                except ValueError:
                    print("❌ Hora inválida. Use el formato HH:MM (24 hs).")

            while True:
                print("\n¿El paciente tiene algún órgano que NO sea apto para la donación?")
                excepcion_organo_donar = input("Responda (sí/no): ").lower().strip()

                if excepcion_organo_donar in ['si', 'sí']:
                    print("\nIngrese órganos aptos para donación:")
                    lista_organos_input = input("Órganos (separados por coma): ")
                    lista_organos = [organo.strip().upper() for organo in lista_organos_input.split(',')]
                    break

                elif excepcion_organo_donar == 'no':
                    lista_organos = ["corazon", "pulmon", "pulmon", "corneas", "pancreas", "higado", "riñon", "riñon", "piel", "huesos", "intestino"]
                    print("\n10 órganos disponibles para donación:")
                    print(lista_organos)
                    break

                else:
                    print("\n❌ Responda con si o no")
            
            
            # Crear donante fallecido
            donante = Donante(
                paciente_base.nombre,
                paciente_base.DNI,
                paciente_base.fecha_nac,
                paciente_base.sexo,
                paciente_base.telefono,
                paciente_base.contacto,
                paciente_base.tipo_sangre,
                paciente_base.centro,
                "donante",
                fecha_fall,
                hora_fall,
                hora_ablacion,
                fecha_ablacion,
                lista_organos
            )
            
            self.donantes.append(donante)
            print(f"✅ Donante fallecido registrado. Órganos disponibles: {', '.join(lista_organos)}")
            self.procesar_donacion_multiple(donante)

    def registrar_receptor(self, paciente_base):
        """
        Registra un receptor y busca matches con donantes existentes.
        """
        print("\n--- REGISTRO DE RECEPTOR ---")
    
        organo = input("Ingrese órgano que necesita: ").strip().upper()
    
        while True:
            fecha_lista = input("Ingrese fecha de ingreso a lista de espera (dd/mm/yyyy): ")
            try:
                fecha_lista = datetime.strptime(fecha_lista, "%d/%m/%Y")
                break
            except ValueError:
                print("❌ Formato de fecha inválido. Use dd/mm/yyyy.")
    
        patologia = input("Ingrese patología: ").strip()
    
        # Obtener estado del paciente
        estado = self.estado_receptor()
    
        # Crear receptor
        receptor = Receptor(
            paciente_base.nombre,
            paciente_base.DNI,
            paciente_base.fecha_nac,
            paciente_base.sexo,
            paciente_base.telefono,
            paciente_base.contacto,
            paciente_base.tipo_sangre,
            paciente_base.centro,
            "receptor",
            organo,
            fecha_lista,
            patologia,
            estado
        )
    
        self.receptores.append(receptor)
        print(f"✅ Receptor registrado en lista de espera para {organo}")
        
        # Buscar match inmediato con donantes existentes
        self.buscar_match_para_receptor(receptor)

            
    def estado_receptor():
        estados_validos = ["ESTABLE", "INESTABLE"]
        while True:
            estado = input("Ingrese estado [ESTABLE/INESTABLE]: ").upper().strip()
            if estado in estados_validos:
                return estado
            print("❌ Estado inválido. Ingrese 'ESTABLE' o 'INESTABLE' solamente.")



    def buscar_receptor_organo_especifico (self, donante, organo):
        print(f"\n🔍 Buscando receptor para {organo} del donante {donante.nombre}...")
        
        receptores_compatibles = []
        
        for receptor in self.receptores:
            if (receptor.organo_necesario.upper() == organo.upper() and 
                receptor.tipo_sangre == donante.tipo_sangre):
                receptores_compatibles.append(receptor)
        
        if receptores_compatibles:
            # Ordenar por prioridad y fecha de lista
            mejor_receptor = self.elegir_receptor(receptores_compatibles)
            print(f"✅ Match encontrado: {mejor_receptor.nombre} recibirá {organo}")

            self.procesar_asignacion(donante, mejor_receptor, organo)
        else:
            print(f"❌ No se encontró receptor compatible para {organo}")

    def procesar_donacion_multiple(self, donante):
        """
        Busca receptores para todos los órganos de un donante fallecido.
        """
        print(f"\n🔍 Procesando donación múltiple de {donante.nombre}...")
        
        asignaciones_realizadas = []
        
        for organo in donante.lista_organos:
            print(f"\n--- Buscando receptor para {organo} ---")
            
            receptores_compatibles = []
            for receptor in self.receptores:
                if (receptor.organo_necesario.upper() == organo.upper() and 
                    receptor.tipo_sangre == donante.tipo_sangre):
                    receptores_compatibles.append(receptor)
            
            if receptores_compatibles:
                mejor_receptor = self.elegir_receptor(receptores_compatibles)
                print(f"✅ Match: {mejor_receptor.nombre} recibirá {organo}")
                asignaciones_realizadas.append((mejor_receptor, organo))
                
                # Procesar asignación
                self.procesar_asignacion(donante, mejor_receptor, organo)
            else:
                print(f"❌ No hay receptor compatible para {organo}")
        
        # Resumen de asignaciones
        if asignaciones_realizadas:
            print(f"\n📋 RESUMEN DE ASIGNACIONES:")
            for receptor, organo in asignaciones_realizadas:
                print(f"  • {organo} → {receptor.nombre}")
        else:
            print("\n❌ No se realizaron asignaciones para este donante")

    def buscar_match_para_receptor(self, receptor):
        """
        Busca matches para un receptor recién registrado.
        """
        print(f"\n🔍 Buscando donante compatible para {receptor.nombre}...")
        
        for donante in self.donantes:
            # Verificar si el donante tiene el órgano necesario y tipo de sangre compatible
            if (receptor.organo_necesario.upper() in [org.upper() for org in donante.lista_organos] and
                receptor.tipo_sangre == donante.tipo_sangre):
                
                print(f"✅ Match encontrado: Donante {donante.nombre} puede donar {receptor.organo_necesario}")
                self.procesar_asignacion(donante, receptor, receptor.organo_necesario)
                return
        
        print(f"❌ No se encontró donante compatible para {receptor.nombre}")

    def elegir_receptor(self, receptores_compatibles):
        """
        Elige el mejor receptor basado en prioridad y fecha de lista.
        """
        # Ordenar por estado (INESTABLE primero) y luego por fecha de lista
        receptores_compatibles.sort(key=lambda r: (
            r.estado != "INESTABLE",  # INESTABLE tiene prioridad (False viene antes que True)
            r.fecha_lista  # Fecha más antigua primero
        ))
        
        return receptores_compatibles[0]

    def procesar_asignacion(self, donante, receptor, organo):
        """
        Procesa la asignación de un órgano a un receptor.
        Aquí se implementaría la lógica de transporte, tiempos, etc.
        """
        print(f"\n PROCESANDO ASIGNACIÓN:")
        print(f"   Donante: {donante.nombre}")
        print(f"   Receptor: {receptor.nombre}")
        print(f"   Órgano: {organo}")
        print(f"   Centro destino: {receptor.centro}")
        
        # saco organo de la lista del donante
        if organo.upper() in [org.upper() for org in donante.lista_organos]:
            donante.lista_organos = [org for org in donante.lista_organos 
                                    if org.upper() != organo.upper()]
        
        # Si el donante no tiene más órganos, removerlo de la lista
        if not donante.lista_organos:
            self.donantes.remove(donante)
            print(f"   ℹ️  Donante {donante.nombre} removido (sin órganos disponibles)")
        
        #remover receptor de la lista (transplante exitoso)
        if receptor in self.receptores:
            self.receptores.remove(receptor)
            print(f"   ✅ Receptor {receptor.nombre} removido (transplante programado)")
        #si no es exitoso tengo que cambiar la prioridad del receptor
        
        # falta implementar transporte 
        # self.transporte(donante, receptor, organo)
        
        
        
        
        
        
        
        
        '''
        def buscar_match(self, donante):
            return
        
        def buscar_receptores(self, organo, donante):
            receptores_compatibles=[]
            
            return receptores_compatibles  
        '''
        
    
            
    #incucai debe tener una validacion que ningun paciente se repite
    #debo sacar de la lista a pacientes que no tiene mas organos para donar
    #debo sacar a los receptores que tuvieron un transplante exitoso
    
    

    '''
    def clasificar_pac (self,que_es = None, paciente_exist = None):
    
        if paciente_exist:
            if isinstance(paciente_exist, Donante):
                if any(p.DNI == paciente_exist.DNI for p in self.donantes + self.receptores):
                    print(f"Ya existe un paciente con DNI {paciente_exist.DNI}.")
                    return
                Donante.agregar(paciente_exist)
                self.donantes.append(paciente_exist)
                return

            if isinstance(paciente_exist, Receptor):
                if any(p.DNI == paciente_exist.DNI for p in self.donantes + self.receptores):
                    print(f"Ya existe un paciente con DNI {paciente_exist.DNI}.")
                    return
                Receptor.agregar(paciente_exist)
                self.receptores.append(paciente_exist)
                return
            paciente_base = paciente_exist
            que_es = paciente_base.que_es.lower()
            
                else:
                    opcion_don_rec=int(input("A que lista quiere agregar?\n1- Lista Receptores\n2-Lista donantes\n"))
                
                if opcion_don_rec == 1:
                    que_es = 'receptor'
                elif opcion_don_rec == 2:
                    que_es = 'donante' 
                else:
                    print("\nOpcion no valida. El paciente DEBE SER DONANTE O RECEPTOR")
                    return
            else:
            paciente_base = Paciente.agregar(que_es)

        dni_a_verificar = paciente_base.DNI

        if any(p.DNI == dni_a_verificar for p in self.donantes + self.receptores):
            print(f" Ya existe un paciente con DNI {dni_a_verificar} en el sistema. No se puede agregar.")
            return
        
        #datos = paciente_base.__dict__  #este dict toma los datos que se guardaron en pqciente y los pasa como uno solo, pata guardarlo en la lista

        if que_es == "donante":
            
            preguntar si esta vivo o no y agregar funcion proveniente de organos de pedir los datos de ablacion
            while True:
                fecha_fall = input("Ingrese fecha de fallecimiento (dd/mm/yyyy): ")
                try:
                    datetime.strptime(fecha_fall, "%d/%m/%Y")
                    break
                except ValueError:
                    print("❌ Fecha inválida. Use el formato dd/mm/yyyy.")

            while True:
                hora_fall = input("Ingrese hora de fallecimiento (HH:MM): ")
                try:
                    datetime.strptime(hora_fall, "%H:%M")
                    break
                except ValueError:
                    print("❌ Hora inválida. Use el formato HH:MM (24 hs).")

            while True:
                fecha_ablacion = input("Ingrese fecha de ablación (dd/mm/yyyy): ")
                try:
                    datetime.strptime(fecha_ablacion, "%d/%m/%Y")
                    break
                except ValueError:
                    print("❌ Fecha inválida. Use el formato dd/mm/yyyy.")

            while True:
                hora_ablacion = input("Ingrese hora de ablación (HH:MM): ")
                try:
                    datetime.strptime(hora_ablacion, "%H:%M")
                    break
                except ValueError:
                    print("❌ Hora inválida. Use el formato HH:MM (24 hs).")

            lista_organos = input("Ingrese lista de órganos disponibles (separados por coma): ").split(',')
            
            donante = Donante(
                paciente_base.nombre,
                paciente_base.DNI,
                paciente_base.fecha_nac,
                paciente_base.sexo,
                paciente_base.telefono,
                paciente_base.contacto,
                paciente_base.tipo_sangre,
                paciente_base.centro,
                que_es,
                fecha_fall, #iniciar variables de fallecimiento vacias y llenarlas depedenidnedo si esta vivo o no
                hora_fall,
                hora_ablacion,
                fecha_ablacion,
                lista_organos)

            Donante.agregar(donante)
            self.donantes.append(donante)

        elif que_es == "receptor":
            organo = input("Ingrese órgano que recibe: ")

            fecha_lista = input("Ingrese fecha en lista de espera (dd/mm/yyyy): ")
            try:
                fecha_lista = datetime.strptime(fecha_lista, "%d/%m/%Y")
            except ValueError:
                print("Formato de fecha invalido. Use dd/mm/yyyy.")
                return
            
            patologia = input("Ingrese patología: ")
            
            
        
            

            receptor = Receptor(
                paciente_base.nombre,
                paciente_base.DNI,
                paciente_base.fecha_nac,
                paciente_base.sexo,
                paciente_base.telefono,
                paciente_base.contacto,
                paciente_base.tipo_sangre,
                paciente_base.centro,
                que_es,
                organo,
                fecha_lista,
                patologia,
                estado)

            Receptor.agregar(receptor)
            self.receptores.append(receptor)
            '''
            
            



'''    
- match (sangre,hla, edad) y prioridad

- menu dar datos de estadisticas (impirmir centros de salud, cuantos cirjuanos de los centros, vehiculos disponibles)
- cuando pedis dato de centro, dar las opciones q hay y ahi determianrlo

- restringir los datos pedidos extras
-impresion de datos del paciente 

'''