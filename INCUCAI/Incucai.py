'''
Alonso Victoria
Pfeifer Zoe

El Sistema tiene que permitir:
    -Registrar pacientes nuevos (Validando que no se encuentre en otra lista ni se repita).
    -Quitar de la lista de donantes a aquellos cuyos organos ya han sido utilizados en su totalidad.
    -Quitar de la lista a un receptor una vez que ha recibido su organo exitosamente.
    -Buscar por centro de salud los pacientes de la lista de espera.
    -Buscar un receptor e informar qué prioridad tiene en la lista de espera.
    -Imprimir listado de pacientes donantes y receptores.
    -Realizar correctamente todo el proceso de asignación y derivación de un organo a un receptor,
    contemplando el viaje, la disponibilidad en ese horario de los vehiculos de un centro medico y el tiempo de viaje.

El INCUCAI sabe recibir un paciente. Cuando lo hace recibe al Paciente, y lo ingresa:
    Si el paciente es donante, al ser ingresado se lo agrega a la lista de pacientes donantes.
    Luego se busca los posibles receptores para cada órgano que el donante puede donar, para esto se busca en su lista de pacientes receptores todos los pacientes que necesitan ese órgano y tienen el mismo tipo de sangre. 
    Finalmente, se elige el receptor, en función a la prioridad del paciente (si tienen la misma prioridad elige al que tiene una fecha anterior de ingreso a la lista de espera). En tal caso, se envia el organo correspondiente a la ubicación del paciente
    receptor y se quita de la lista de donantes la disponibilidad de ese organo para ese donante en particular. Si el paciente es receptor, se lo agrega a la lista de pacientes receptores, y se busca si hay alguna coincidencia en
    la lista de donantes. De haberlo se despacha el organo para el receptor, actualizando de igual manera la lista de donantes.  
'''
#Importaciones de librerias estandar:
from geopy.geocoders import Nominatim
from datetime import datetime
from unidecode import unidecode
#Importaciones de clases creadas: Notese que no importamos clases abstractas porque no pueden instanciarse
from INCUCAI.Paciente.Paciente import Paciente
from INCUCAI.Paciente.Donante import Donante 
from INCUCAI.Paciente.Receptor import Receptor
from INCUCAI.Centros.Centro import Centro_de_salud 
from INCUCAI.Centros.Cirujanos.Especialista import Especialista
from INCUCAI.Centros.Cirujanos.General import General
from INCUCAI.Vehiculo.Avion import Avion
from INCUCAI.Vehiculo.Helicoptero import Helicoptero
from INCUCAI.Vehiculo.Ambulancia import Ambulancia
from INCUCAI.Organos.Organo import Organo
from Testing import *
import traceback



class Incucai:
    '''    
    Metodos de Incucai:
    centros()
    clasificar_paciente_ya_existente(paciente_exist=None, que_es=None)
    registrar_donante(paciente_base)
    registrar_receptor(paciente_base)
    
    buscar_match_para_receptor(receptor)
    buscar_receptor_organo_especifico(donante, organo)
    procesar_donacion_multiple(donante)
    elegir_receptor(lista_receptores) --> (usa HLA, sangre, edad, prioridad, fecha)
    
    procesar_asignacion(donante, receptor, organo)
    validar_compatibilidad(donante, receptor, organo) --> (centraliza sangre, HLA, edad pediátrica)
    
    mostrar_centros_salud()
    estadisticas_transplantes_realizados() (opcional si llevás registro)
    vehiculos_disponibles_por_centro()
    '''
    geolocator = Nominatim(user_agent="incucai_test") #Instancia de Nominatim [necesaria para coordenadas]
    
    def __init__(self) -> None:
        """
        Permite instanciar Incucai
            - receptores: Un array para la carga de receptores de INCUCAI
            - donantes: Un array para la carga de donantes de INCUCAI
            - vehiculos: Un array para la carga de vehiculos de INCUCAI
            - cirujano: Un array para la carga de cirujanos de INCUCAI
            - centros: Un array para la carga de los centros habilitados de INCUCAI

        returns:
            - None
        """
        self.receptores = []
        self.donantes = []
        aux_centro=self.centros()
        self.centro = aux_centro
        self.vehiculos = []
        self.ambulancias = []
        self.aviones = []
        self.helicopteros = []
        self.cirujano = []
        self.generales = []
        self.especialistas = []
             
    def centros(self) -> list:
        """
        Crea y devuelve una lista de instancias de Centro_de_salud que representan centros habilitados por el INCUCAI,
        distribuidos en distintas provincias argentinas.
        Args:
            - None
        Returns:
            - list: Lista de objetos de tipo Centro_de_salud, uno por provincia aproximadamente.
        """
        return [
            Centro_de_salud("Hospital Garrahan", "Pichincha 1890", "Comuna 1", "Ciudad Autónoma de Buenos Aires", "011-12345678"),
            Centro_de_salud("Hospital El Cruce", "Av. Calchaquí 5401", "Florencio Varela", "Buenos Aires", "011-98765432"),
            Centro_de_salud("Fundacion Favaloro", "Av. Belgrano 1746", "C1093", "Ciudad Autónoma de Buenos Aires", "011-4378-1200"),
            Centro_de_salud("Hospital General de Niños Dr. R. Gutierrez", "Gallo 1330", "C1425EFD", "Ciudad Autónoma de Buenos Aires", "011 4962-9247"),
            Centro_de_salud("Hospital Italiano de La Plata", "Av. 51, B1900 La Plata", "La Plata", "Provincia de Buenos Aires", "022-15129500"),
            Centro_de_salud("Hospital Universitario Austral", "Mariano Acosta 1611", "Pilar", "Buenos Aires", "023-04388888"),
            Centro_de_salud("Hospital Gral. de Agudos Carlos G. Durand", "Av. Diaz Velez 5044", "Caballito", "Ciudad Autónoma de Buenos Aires", "011 4982-5555"),
            Centro_de_salud("Sanatorio Pasteur", "Chacabuco 675", "San Fernando del Valle de Catamarca", "Catamarca", "038 3443-2000"),
            Centro_de_salud ("Hospital Zonal Alvear", "Juan Ramón Balcarce, Comodoro Rivadavia, Chubut", "Comodoro Rivadavia", "Chubut", "029 7455-9952"),
            Centro_de_salud ("Hospital de Urgencias", "Catamarca 441, X5000 Córdoba", "Barrio Centro" , "Córdoba", "0351 427-6200"),
            Centro_de_salud ("Hospital El Carmen", "Godoy Cruz 5504", "Godoy Cruz", "Mendoza", "081 0810-1033"), 
            Centro_de_salud ("Hospital Samic Alem de autogestión nivel II", "Misiónes, N3315 Leandro N. Alem", "Misiones", "Misiones", "037 6415-6950"), 
            Centro_de_salud ("Hospital Area Programa Cipoletti Dr. Pedro Moguillansky", "Naciones Unidas 1450", "Cipolletti", "Río Negro" , "0299 4775-469"), #rio negro
            Centro_de_salud ("Hospital Papa Francisco", "C. 120 S/N, A4400 Salta", "Salta", "Salta", "0387 438-5022"),
            Centro_de_salud ("Hospital Dr. Guillermo Rawson", "Av. Guillermo Rawson Sur 494", "J5400 San Juan", "San Juan", "026 4422-4005"),
            Centro_de_salud ("Hospital Dr. Clemente Alvarez", "Av. Pellegrini 3205", "Rosario Centro", "Santa Fe", "034 1480-8111"), #santa fe
            Centro_de_salud ("Hospital Regional Rio Grande", "Florentino Ameghino 709", "Rio Grande", "Tierra del Fuego", "029 6442-2042"), #tierra del fuego
            Centro_de_salud ("Clinica Mayo SRL", "9 de Julio 279", "San Miguel de Tucumán", "Tucuman", "038 1450-2600"), #tucuman               
        ]
    
#-------------------------------------------------------------------INICIO DE REGISTROS----------------------------------------------------------------------------------
    def registrar_donante(self, donante:Donante) -> None:
        """
        Agrega un nuevo array a la lista de donantes de INCUCAI
        
        Args:
            -donante (a agregar): Donante

        returns:
            - None
        """
        if not  self.paciente_existente(donante.DNI): #Invoca a funcion .paciente_existente para revisar que no exista ya un donante del mismo DNI
            self.donantes.append(donante)
        return None
            
    def registrar_receptor(self, receptor: Receptor) -> None:
        """
        Agrega un nuevo array a la lista de receptores de INCUCAI
        
        Args:
            -receptor (a agregar)

        returns:
            - None
        """
        if not self.paciente_existente(receptor.DNI): #Invoca a funcion .paciente_existente para revisar que no exista ya un receptor del mismo DNI
            self.receptores.append(receptor)
        return None

    def registrar_ambulancia(self, vehiculo: Ambulancia) -> tuple:
        """
        Agrega una nueva ambulancia a la lista de vehiculos y de ambulancias de INCUCAI
        
        Args:
        vehiculo (Ambulancia): Objeto de tipo Ambulancia a registrar.

        Returns:
            tuple: (ambulancia registrada, cantidad total de vehículos en INCUCAI)
        """
        centro = self.buscar_centro_por_nombre(vehiculo.centro_vehiculo)
        self.vehiculos.append(vehiculo) #Nota: Notese que no estamos instanciando Vehiculo, a la lista vehiculos le agrego el vehiculo pasado por atributo
        self.ambulancias.append(vehiculo)
        print(f"Ambulancia agregada al centro: {centro.nombre_cs}")
        centro.agregar_ambulancia(vehiculo)
        return (vehiculo, len(self.vehiculos))
        
    def registrar_avion(self, vehiculo: Avion) -> tuple:
        """
        Registra un avión en el sistema y lo asocia a su centro de salud correspondiente.

        Args:
            vehiculo (Avion): Objeto de tipo Avion a registrar.

        Returns:
            tuple: (avión registrado, total de vehículos en INCUCAI, total de aviones en INCUCAI)
        """
        
        centro = self.buscar_centro_por_nombre(vehiculo.centro_vehiculo)
        self.vehiculos.append(vehiculo) #Nota: Notese que no estamos instanciando Vehiculo, a la lista vehiculos le agrego el vehiculo pasado por atributo
        self.aviones.append(vehiculo)
        print(f"Avion agregado al centro: {centro.nombre_cs}")
        centro.agregar_avion(vehiculo)
        return (vehiculo, len(self.vehiculos), len(self.aviones))
    
    def registrar_helicoptero(self, vehiculo: Helicoptero) -> tuple:
        """
        Registra un helicóptero en el sistema y lo asocia a su centro de salud correspondiente.

        Args:
            vehiculo (Helicoptero): Objeto de tipo Helicoptero a registrar.

        Returns:
            tuple: (helicóptero registrado, total de vehículos en INCUCAI, total de helicópteros en INCUCAI)
        """
        centro = self.buscar_centro_por_nombre(vehiculo.centro_vehiculo)
        self.vehiculos.append(vehiculo) #Nota: Notese que no estamos instanciando Vehiculo, a la lista vehiculos le agrego el vehiculo pasado por atributo
        self.helicopteros.append(vehiculo)
        print(f"Helicoptero agregado al centro: {centro.nombre_cs}")
        centro.agregar_vehiculo(vehiculo)
        return (vehiculo, len(self.vehiculos), len(self.helicopteros))
    
    def registrar_cirujano_general(self, cirujano: General) -> tuple:
        """
        Registra un cirujano general en el sistema y lo asocia al centro correspondiente.

        Args:
            cirujano (General): Objeto de tipo General a registrar.

        Returns:
            tuple: (cirujano registrado, total de cirujanos, total de cirujanos generales)
        """
        centro = self.buscar_centro_por_nombre(cirujano.centro)
        self.cirujano.append(cirujano)
        self.generales.append(cirujano)
        centro.agregar_cirujano_general(cirujano)
        return (cirujano, len(self.cirujano), len(self.generales))
    
    def registrar_cirujano_especialista(self, cirujano: Especialista) -> tuple:
        """
        Registra un cirujano especialista en el sistema y lo asocia al centro correspondiente.

        Args:
            cirujano (Especialista): Objeto de tipo Especialista a registrar.

        Returns:
            tuple: (cirujano registrado, total de cirujanos, total de especialistas)
        """
        centro = self.buscar_centro_por_nombre(cirujano.centro)
        self.cirujano.append(cirujano)
        self.especialistas.append(cirujano)
        centro.agregar_cirujano_especialista(cirujano)
        return (cirujano, len(self.cirujano), len(self.especialistas))
    
    def crear_objetos_prueba(self) -> None:
        """
        Crea y registra automáticamente pacientes, vehículos y cirujanos de prueba en el sistema INCUCAI.

        Agrupa llamadas a funciones externas de creación y luego registra:
            - Donantes y receptores
            - Aviones, ambulancias, helicópteros
            - Cirujanos generales y especialistas

        Returns:
            None
        """

        try:
            print("\n-----------------------   Buscando pacientes anteriores...   -----------------------")
            lista_pacientes_test = creacion_pacientes()
            
            lista_donantes_test = [p for p in lista_pacientes_test if isinstance(p, Donante)]
            lista_receptores_test = [p for p in lista_pacientes_test if isinstance(p, Receptor)]
            
            print("\n-----------------------   Iniciando registro de donantes anteriores...   -----------------------")
            for i, donante in enumerate(lista_donantes_test):
                print(f"{i} Registrando donante DNI: {donante.DNI}")
                self.registrar_donante(donante)
                print(f"Donante registrado")
            
            print("\n-----------------------    Iniciando registro de receptores anteriores...    -----------------------")
            for i, receptor in enumerate(lista_receptores_test):
                print(f"{i} Registrando receptor DNI: {receptor.DNI}")
                self.registrar_receptor(receptor)
                print(f"Receptor registrado")
                
            print(f"\nTOTAL donantes: {len(self.donantes)}")
            print(f"TOTAL receptores: {len(self.receptores)}")
        
        except Exception as e:
            print(f"ERROR CAPTURADO: {e}")
            
            traceback.print_exc()
        
        lista_aviones_test = creacion_aviones()
        lista_ambulancias_test = creacion_ambulancias ()
        lista_helicoptero_test = creacion_helicoptero ()
        lista_cirujanos_generales_test = creacion_cirujanos_generales()
        lista_cirujanos_especialistas_test = creacion_cirujanos_especialistas()
        
        for vehiculo in lista_aviones_test:
            self.registrar_avion(vehiculo)
        for vehiculo in lista_ambulancias_test:
            self.registrar_ambulancia(vehiculo) 
        for vehiculo in lista_helicoptero_test:
            self.registrar_helicoptero(vehiculo)           
        for cirujano in lista_cirujanos_generales_test:
            self.registrar_cirujano_general(cirujano)   
        for cirujano in lista_cirujanos_especialistas_test:
            self.registrar_cirujano_especialista(cirujano)
        
        return        
#-------------------------------------------------------------------FIN DE REGISTROS----------------------------------------------------------------------------------

#-------------------------------------------------------------------INICIO IMPRESIONES----------------------------------------------------------------------------------
    def listar_donantes(self) -> None:
        """
        Imprime la lista de donantes registrados en el sistema.
        
        Args:
            -None
        Return:
            -None  
        """
        if not self.donantes:
            print("No hay donantes registrados.")
            return
        print("\n--- DONANTES: --- ")
        for d in self.donantes:
            print(f"- {d}")

    def listar_receptores(self) -> None:
        """
        Imprime la lista de receptor registrados en el sistema.
        
        Args:
            -None
        Return:
            -None           
        """
        if not self.receptores:
            print("No hay receptores registrados.")
            return
        for r in self.receptores:
            print(f"- {r}")
    
    def mostrar_centros_salud(self) -> None:
        """
        Imprime la lista de centros de salud registrados en el sistema.
        
        Args:
            -None
        Return:
            -None 
        """
        if not self.centro:
            print("No hay centros de salud habilitados.")
            return
        print("\nCentros de salud habilitados:")
        for cs in self.centro:
            print(f"- {cs}")
        
    def receptores_por_centro_salud(self, nombre_centro: str) -> None:
        """
        Muestra los receptores en lista de espera asociados a un centro de salud.

        Args:
            nombre_centro (str): Nombre exacto del centro a consultar.

        Return:
            None
        """
        # 1) Validar que el centro exista (self.centro_valido debe devolver bool)
        if not self.centro_valido(nombre_centro):
            print("❌ Centro de salud no registrado. Intente nuevamente con un nombre válido.")
            print("\n📋 Centros disponibles:")
            for c in self.centro:
                print(f"- {c.nombre_cs}")
            return

        # 2) Filtrar receptores cuyo centro coincide
        receptores_centro = [
            r for r in self.receptores
            if r.centro and r.centro.lower() == nombre_centro.lower()
        ]

        if not receptores_centro:
            print("⚠️ No hay receptores en lista de espera en ese centro.")
            return

        # 3) Mostrar receptores ordenados por fecha de ingreso
        print(f"\n📋 Receptores en el centro '{nombre_centro}':\n")
        for r in sorted(receptores_centro, key=lambda r: r.fecha_list_esp):
            organos = ", ".join(r.org_recib)
            print(f"- {r.nombre} (DNI: {r.DNI}, Fecha ingreso: {r.fecha_list_esp}, "
                f"Estado: {r.estado}, Órganos: {organos})")


    
        
#-------------------------------------------------------------------FIN DE IMPRESIONES----------------------------------------------------------------------------------

#------------------------------------------------------INICIO DE BUSQUEDAS, ORDENAMIENTOS Y VALIDACIONES-------------------------------------------------------------------------------
    def buscar_paciente_por_dni(self, dni: int) -> Donante | Receptor | None:
        """
        Busca un paciente (donante o receptor) por su DNI.

        Args:
            -dni (str | int): DNI del paciente a buscar.

        Returns:
            - Donante | Receptor | None: Devuelve el paciente si lo encuentra, o None si no existe.
        """
        for p in self.donantes + self.receptores:
            if p.DNI == dni:
                return p 
        return None
    
    def pedir_dni(self, tipo="paciente") -> int:
        """
        Solicita al usuario que ingrese un DNI válido de 7 u 8 dígitos numéricos.

        Args:
            - tipo (str): Tipo de persona a solicitar (por ejemplo "donante", "receptor"). Default: "paciente".

        Returns:
            - int: DNI ingresado, convertido a entero.
        """
        while True:
            dni = input(f"\nIngrese el DNI del {tipo}: ").strip()
            if dni.isdigit() and 7 <= len(dni) <= 8:
                return int(dni)
            print("❌ DNI inválido. Debe tener 7 u 8 dígitos numéricos.")
        
    def paciente_existente(self, dni: int) -> bool:
        """
        Verifica si ya existe un paciente (donante o receptor) registrado con el DNI dado.

        Args:
            - dni (int): Número de DNI a verificar.

        Returns:
            - bool: True si el paciente ya existe, False en caso contrario.
        """
        if any(p.DNI == dni for p in self.donantes + self.receptores):
            print(f"Ya existe un paciente con DNI {dni}.") #podria omitirse y esta responsabilidad que la haga quien use a la funcion
            return True
        return False
    
    def centro_valido(self, nombre_centro) -> bool:
        """
        Verifica si el nombre de centro de salud ingresado corresponde a un centro registrado.

        Args:
            - nombre_centro (str): Nombre del centro de salud a validar.

        Returns:
            - bool: True si el centro está registrado, False en caso contrario.
        """
        nombres_validos = [c.nombre_cs.lower() for c in self.centro]
        return nombre_centro.lower() in nombres_validos
    
    def lista_espera_ordenada(self) -> list:
        """
        Ordena y muestra la lista de receptores en espera por fecha de ingreso.

        Atributos: 
            - None
        Returns:
            - list: Lista de objetos Receptor ordenada por fecha de ingreso (`fecha_list_esp`).
        """
        if not self.receptores:
            print("No hay receptores en la lista de espera.")
            return []
        # Ordenar por fecha de ingreso
        receptores_ordenados = sorted(self.receptores, key=lambda r: r.fecha_list_esp)
    
        print("\n Lista de espera ordenada por fecha de ingreso:")
        for idx, receptor in enumerate(receptores_ordenados, 1):
            print(f"{idx}. {receptor.nombre} (DNI: {receptor.DNI}) - "
                f"Fecha ingreso: {receptor.fecha_list_esp.strftime('%d/%m/%Y')} - "
                f"Estado: {receptor.estado} - Prioridad: {receptor.prioridad_numerica()}")
        
        return receptores_ordenados
    
    def buscar_centro_por_nombre(self, nombre_centro) -> None: #nose q ponerle a centrosalud aca 
        """
        Busca un centro de salud por su nombre (ignorando mayúsculas y espacios).

        Args:
            - nombre_centro (str): Nombre del centro de salud a buscar.

        Returns:
            - CentroSalud | None: El objeto centro encontrado, o None si no existe.
        """
        for centro in self.centro:
            if nombre_centro.strip().lower() == centro.nombre_cs.strip().lower():
                return centro
        print(f"No se encontró el centro: '{nombre_centro}'")
        return None

    def buscar_receptor_por_dni(self, dni: int) -> Receptor | None:
        """
        Busca un receptor en la lista de espera por su DNI y muestra su posición en la lista ordenada por fecha de ingreso.

        Args:
            - dni (int): Número de DNI del receptor a buscar.

        Returns:
            - Receptor | None: Devuelve el receptor si se encuentra, o None si no está en la lista o el DNI no es válido.
        """
        
        try:
            dni = int(dni) #Para posibles problemas con strings
        
        except ValueError:
            print("❌ El DNI ingresado no es válido.")
            return None
        
        lista_ordenada = self.lista_espera_ordenada()
        
        for idx, receptor in enumerate(lista_ordenada):
            if int(receptor.DNI) == dni:
                print(f"\n🔍 El paciente '{receptor.nombre}' (DNI: {dni}) está en la posición {idx + 1} de la lista de espera.")
                print(f"📋 Hay {idx} paciente(s) antes en la lista.")
                return receptor
        
        print(f"❌ No se encontró ningún receptor con el DNI {dni} en la lista de espera.")
        return None
    
#--------------------------------------------------------FIN DE BUSQUEDAS, ORDENAMIENTOS Y VALIDACIONES-------------------------------------------------------------------------------

#----------------------------------------------------------------INICIO DE LOGICA DE DONACION-----------------------------------------------------------------------
    
    def clasificar_paciente_ya_existente(self, paciente_existente: Paciente) -> None:
        """
        Clasifica un paciente previamente creado según su tipo (Donante o Receptor) 
        y ejecuta las acciones correspondientes según su estado.
        Si el paciente ya existe en el sistema (por su DNI), no se realiza ninguna acción.

        Args:
            - paciente_existente (Donante | Receptor, opcional): Instancia de paciente a clasificar.
        Return:
            - None
        """
        if not paciente_existente:
            return
        dni = paciente_existente.DNI
        if self.paciente_existente(dni):
            return  # No agregar duplicados
        
        if paciente_existente:
                if isinstance(paciente_existente, Donante):
                    if self.paciente_existente(paciente_existente.DNI): 
                        return
                    self.donantes.append(paciente_existente)
                    donante1=paciente_existente
                    if (donante1.estado_donante=='muerto'):
                        self.procesar_donacion_multiple(paciente_existente)
                        return
                    if (donante1.estado_donante=='vivo'):
                        self.donar_organo_especifico(paciente_existente)
                    
                if isinstance(paciente_existente, Receptor):
                    if self.paciente_existente(paciente_existente.DNI): 
                        return
                    self.receptores.append(paciente_existente)
                    self.buscar_match_para_receptor(paciente_existente)
                    return

    def donar_organo_especifico(self, paciente_existente: Donante) -> None:
        '''
        Permite seleccionar un órgano específico de un donante para iniciar búsqueda de receptor compatible.
        Args: 
            -paciente_existente (Donante): Objeto donante con organos disponibles.
        Return:
            - None
        '''
        if not paciente_existente.lista_organos:
            print(f"❌ {paciente_existente.nombre} no tiene órganos disponibles para donar.")
            return

        print(f"\nÓrganos disponibles para donar de {paciente_existente.nombre}:")
        for i, organo in enumerate(paciente_existente.lista_organos):
            print(f"{i+1}. {organo}")

        while True:
            seleccion = input("\nSeleccione el número del órgano que desea donar: ")

            if seleccion.isdigit():
                seleccion = int(seleccion)
                if 1 <= seleccion <= len(paciente_existente.lista_organos):
                    organo_elegido = paciente_existente.lista_organos[seleccion - 1]
                    self.buscar_receptor_organo_especifico(paciente_existente, organo_elegido)
                    break
                else:
                    print("❌ Selección fuera de rango. Intente de nuevo.")
            else:
                print("❌ Entrada inválida. Por favor, ingrese un número.")
        
    def compatibilidad(self, donante: Donante, receptor:Receptor) -> bool:
        '''
        Verifica si un donante y receptor son compatibles según sangre, HLA y edad.
        ArgS: 
            - donante (Donante): Objeto donante.
            - receptor (Receptor): Objeto receptor.
        Return: 
            - bool: True si son compatibles, False en caso contrario.
        '''
        
        if not donante.es_compatible_sangre(receptor):
            return False

        match_hla, total = donante.compatibilidad_hla(receptor) 
        if match_hla  < 3:
            return False
        
        edad_donante = donante.calculo_edad()
        edad_receptor = receptor.calculo_edad()
        if edad_receptor < 18 and abs(edad_receptor - edad_donante) > 3:
            return False
        
        print(f"\nPaciente {receptor.nombre} compatible con: {donante.nombre}")
        print (f"\nCOMPATIBILIDAD:")
        print(f"\nSangre de {receptor.nombre}: {receptor.tipo_sangre} (compatible con sangre de {donante.nombre} de tipo: {donante.tipo_sangre})")
        print (f"\nMatchs de HLA entre pacientes: {match_hla}/{total}")
        
        return True

    def buscar_receptor_organo_especifico(self, donante, organo) -> None:
        """
        Busca un receptor compatible para un órgano específico de un donante.

        Args:
            - donante (Donante): Objeto donante.
            - organo (Órgano): Órgano que se desea donar.

        Returns:
            - None
        """
        print(f"\nBuscando receptor para {organo} del donante {donante.nombre}...")
        compatibles = [r for r in self.receptores if organo.lower() in r.org_recib and self.compatibilidad(donante, r)]
        if compatibles:
            receptor = self.elegir_receptor(compatibles)
            self.procesar_asignacion(donante, receptor, organo)
        else:
            print(f"No se encontro receptor compatible para {organo}.")
            
    def buscar_match_para_receptor(self, receptor) -> None:
        """
        Busca donante compatible para un receptor.

        Args:
            - receptor (Receptor): Objeto receptor que necesita órgano.

        Returns:
            - None
        """
        for donante in self.donantes:
            for organo in donante.lista_organos:
                if organo.lower() in receptor.org_recib and self.compatibilidad(donante, receptor):
                    self.procesar_asignacion(donante, receptor, organo)
                    return
        print(f"No hay donante compatible para {receptor.nombre}.")

    def procesar_donacion_multiple(self, donante) -> None:
        """
        Procesa donación múltiple de órganos de un donante.

        Args:
            - donante (Donante): Objeto donante.

        Returns:
            - None
        """
        print(f"\nProcesando donación de {donante.nombre}...")
        for organo in donante.lista_organos[:]:  # copia para modificar e iterar
            self.buscar_receptor_organo_especifico(donante, organo)

    def elegir_receptor(self, lista) -> Receptor:
        """
        Elige receptor con mayor prioridad y antigüedad de una lista.

        Args:
            - lista (list): Lista de objetos Receptor.

        Returns:
            - Receptor: Objeto receptor con prioridad más alta y más antiguo en lista de espera.
        """
        return sorted(lista, key=lambda r: (r.prioridad_numerica(), r.fecha_list_esp))[0]
            
    def procesar_asignacion(self, donante, receptor, organo) -> None:
        """
        Asigna un órgano del donante a un receptor y actualiza listas.

        Args:
            - donante (Donante): Donante que dona el órgano.
            - receptor (Receptor): Receptor que recibe el órgano.
            - organo (Órgano): Órgano donado.

        Returns:
            - None
        """
        print(f"\nAsignando {organo} de {donante.nombre} a {receptor.nombre} en {receptor.centro}")

        nombre_organo = unidecode(organo.tipo.lower().strip())

        donante.lista_organos = [o for o in donante.lista_organos if unidecode(o.tipo.lower().strip()) != nombre_organo]
        
        if not donante.lista_organos:
            if donante in self.donantes:
                self.donantes.remove(donante)
            print(f"Donante {donante.nombre} removido (sin órganos disponibles)")

        if receptor in self.receptores:
            self.receptores.remove(receptor)
            print(f"Receptor {receptor.nombre} removido (trasplante programado)")
        
    def realizar_transplante(self, receptor: Receptor, donante: Donante, organo) -> bool:
        """
        Ejecuta protocolo completo de trasplante.

        Args:
            - receptor (Receptor): Paciente receptor.
            - donante (Donante): Paciente donante.
            - organo (Órgano): Órgano a trasplantar.

        Returns:
            bool: True si trasplante exitoso, False si falló o hubo errores.
        """
        print(f"\n ➡️ Iniciando protocolo de trasplante para {receptor.nombre} (DNI: {receptor.DNI}) con órgano {organo.tipo}")

        #centro_donante = self.buscar_centro_por_nombre(donante.centro)
        #centro_receptor = self.buscar_centro_por_nombre(receptor.centro)

        centro_donante = self.buscar_centro_por_nombre(donante.centro)
        centro_receptor = self.buscar_centro_por_nombre(receptor.centro)

        if centro_donante is None or centro_receptor is None:
            print("❌ No se encontró el centro de salud del donante o receptor.")
            return False

        if centro_donante.coords is None:
            centro_donante.geolocalizar_direccion(self.geolocator)
        if centro_receptor.coords is None:
            centro_receptor.geolocalizar_direccion(self.geolocator)

        if not centro_donante.realizar_ablacion(organo, donante):
            print("❌ Error en la ablación. Operación cancelada.")
            return False
        
        vehiculo = centro_receptor.seleccionar_vehiculo(centro_receptor)
        
        if vehiculo is None:
            print("❌ No hay vehículos disponibles para trasladar el órgano.")
            return False

        distancia = centro_donante.calcular_distancia_a(centro_receptor)
        trafico = vehiculo.nivel_trafico()
        tiempo_traslado = vehiculo.calculo_tiempo(distancia, trafico)
        
        print(f"\nCentro de donante: {donante.centro}")
        print(f"\nCentro de receptor: {receptor.centro}")
        print(f"\n🚑 Vehículo seleccionado: {vehiculo}")
        print(f"Distancia entre centros: {distancia:.2f} km | Tráfico: {trafico:.2f} | Tiempo estimado: {tiempo_traslado:.2f} h")

        cirujano = centro_receptor.seleccionar_cirujano(organo.tipo)
        if cirujano is None:
            print("No hay cirujano disponible para ese órgano.")
            return False

        print(f"🩺 Cirujano asignado para transplante: {cirujano}")
        exito = centro_receptor.realizar_transplante(organo, receptor, cirujano)
        if exito:
            if receptor in self.receptores:
                self.receptores.remove(receptor)
                print(f"🧾 Receptor {receptor.nombre} eliminado de la lista tras trasplante exitoso.")
            else:
                receptor.estado = "Inestable"
                print(f"⚠️ Receptor {receptor.nombre} ahora en estado INESTABLE tras fallo del trasplante.")

        if organo in donante.lista_organos:
            donante.lista_organos.remove(organo)
            print(f"🗑️ Órgano {organo.tipo} eliminado del donante.")

        if not donante.lista_organos:
            if donante in self.donantes:
                self.donantes.remove(donante)
                print(f"📤 Donante {donante.nombre} eliminado (sin órganos restantes).")

        return True

    def pedir_receptor_para_realizar_transplante(self) -> None:
        """
        Solicita DNI de receptor y ejecuta protocolo para realizar trasplante.

        Args:
            - None

        Returns:
            - None
        """
        try:
            dni = int(input("Ingrese el DNI del receptor que desea trasplantar: "))
        except ValueError:
            print("❌ DNI inválido.")
            return

        receptor = self.buscar_paciente_por_dni(dni)
        if not receptor or not isinstance(receptor, Receptor):
            print("❌ Receptor no encontrado.")
            return

        organos_necesarios = receptor.org_recib
        compatibles = []

        for donante in self.donantes:
            for organo in donante.lista_organos:
                if organo.tipo == organos_necesarios:
                    if self.compatibilidad(donante, receptor):
                        compatibles.append((donante, organo))

        if not compatibles:
            print("❌ No hay donantes compatibles para este receptor.")
            return

        print(f"\n✅ Donantes compatibles encontrados para {receptor.nombre}:")
        for i, (d, o) in enumerate(compatibles):
            print(f"{i+1}. Donante: {d.nombre} (DNI: {d.DNI}) - Órgano: {o.tipo}")

        try:
            seleccion = int(input("\nSeleccione el número del donante con el que desea proceder: "))
            if 1 <= seleccion <= len(compatibles):
                donante, organo = compatibles[seleccion - 1]

                # Validación adicional antes de iniciar el trasplante
                centro_donante = self.buscar_centro_por_nombre(donante.centro)
                centro_receptor = self.buscar_centro_por_nombre(receptor.centro)

                if centro_receptor is None or centro_donante is None:
                    print("❌ No se encontró el centro de salud asociado para el receptor o donante.")
                    return
                
                if not centro_receptor.tiene_vehiculos_disponibles():  # Este método lo debés definir
                    print("❌ El centro del receptor no tiene vehículos disponibles para realizar el trasplante.")
                    return

                funcionotrasplante = self.realizar_transplante(receptor, donante, organo)
                if not funcionotrasplante:
                    print("Algo falló.")
            else:
                print("❌ Número fuera de rango.")
        except ValueError:
            print("❌ Entrada inválida. Debe ingresar un número.")

#------------------------------------------------------------------------FIN DE LOGICA DE DONACION-------------------------------------------------------------------------------
#------------------------------------------------------------------------INICIO METODOS ADICIONALES DE MENU-------------------------------------------------------------------------------
    def compatibilidad_2_pacientes(self) -> None:
        """
        Revisa la compatibilidad entre dos pacientes ingresando sus DNI.

        Args:
            - None
        Return:
            - None
        """
        print("\n➡️ Compatibilidad dirigida: revisa la compatibilidad entre 2 pacientes de DNI solicitado.")

        try:
            dni_donante = int(input("Ingrese el DNI del donante: "))
            dni_receptor = int(input("Ingrese el DNI del receptor: "))
        except ValueError:
            print("❌ Entrada inválida. DNI debe ser numérico.")
            return

        donante = self.buscar_paciente_por_dni(dni_donante)
        receptor = self.buscar_paciente_por_dni(dni_receptor)

        if not donante or not isinstance(donante, Donante):
            print("❌ Donante no encontrado o inválido.")
            return

        if not receptor or not isinstance(receptor, Receptor):
            print("❌ Receptor no encontrado o inválido.")
            return
        
        es_compatible = self.compatibilidad(donante, receptor)
        if not es_compatible:
            print(f"\n❌ Pacientes {donante.nombre} y {receptor.nombre} NO son compatibles.")
        
        return

    def donar_organo_de_donante_a_receptor_especifico(self) -> None:
        """
        Permite donar un órgano específico de un donante a un receptor ingresando DNI.
        Args:
            - None
        Return:
            - None
        """
        print("\n➡️ Donación dirigida: Donar un órgano específico de un donante a un receptor.")

        dni_donante = self.pedir_dni("donante")
        dni_receptor = self.pedir_dni("receptor")

        donante = self.buscar_paciente_por_dni(dni_donante)
        receptor = self.buscar_paciente_por_dni(dni_receptor)

        if not donante or not isinstance(donante, Donante):
            print("❌ Donante no encontrado o inválido.")
            return

        if donante.estado_donante.lower() != 'vivo':
            print(f"❌ El donante {donante.nombre} no está en estado 'vivo'.")
            return

        if not receptor or not isinstance(receptor, Receptor):
            print("❌ Receptor no encontrado o inválido.")
            return

        if not donante.lista_organos:
            print(f"❌ Donante {donante.nombre} no tiene órganos disponibles para donar.")
            return

        print(f"\nÓrganos disponibles para donar de {donante.nombre}:")
        for i, organo in enumerate(donante.lista_organos):
            print(f"{i+1}. {organo}")

        while True:
            seleccion = input("\nSeleccione el número del órgano que desea donar: ")

            if seleccion.isdigit():
                seleccion = int(seleccion)
                if 1 <= seleccion <= len(donante.lista_organos):
                    organo_elegido = donante.lista_organos[seleccion - 1]

                    nombre_org_elegido = unidecode(organo_elegido.tipo.lower().strip())
                    orgs_requeridos = [unidecode(o.lower().strip()) for o in receptor.org_recib]

                    print(f"Receptor necesita: {orgs_requeridos}")
                    print(f"Órgano seleccionado: {nombre_org_elegido}")


                    if nombre_org_elegido in orgs_requeridos:
                        if self.compatibilidad(donante, receptor):
                            self.procesar_asignacion(donante, receptor, organo_elegido)
                            return
                        else:
                            print("❌ El donante y el receptor no son compatibles.")
                            return
                    else:
                        print(f"❌ El receptor no necesita el órgano '{organo_elegido.tipo}'.")
                        return
                else:
                    print("❌ Selección fuera de rango. Intente de nuevo.")
            else:
                print("❌ Entrada inválida. Por favor, ingrese un número.")

    def mostrar_info_centro_salud(self) -> None:
        """
        Muestra información detallada de un centro de salud, incluyendo ubicación, vehículos y cirujanos.
        Args:
            - None
        Return:
            - None
        """
        nombre_centro = input("\nIngrese el nombre del centro de salud: ").strip()
        centro = self.buscar_centro_por_nombre(nombre_centro)
        if not centro:
            print(f"❌ Centro de salud '{nombre_centro}' no encontrado.")
            return

        print(f"\n🏥 Información del Centro: {centro.nombre_cs}")
        print(f"📍 Dirección: {centro.direccion_completa()}")
        
        if centro.coords:
            print(f"🌐 Coordenadas: {centro.geolocalizar_direccion()}")
        else:
            print("🌐 Coordenadas: No geolocalizado.")

        # Vehículos
        print(f"\n🚑 Vehículos disponibles de {centro.nombre_cs}:")
        print(f"\nAmbulancias de {centro.nombre_cs}")
        if centro.ambulancias:
            for a in centro.ambulancias:
                print(f" - {a} (Patente: {a.patente}")
        else:
            print("🚫 No hay ambulancias registradas en este centro.")
        
        print(f"\nAviones de {centro.nombre_cs}")
        if centro.aviones:
            for av in centro.aviones:
                print(f" - {av} (Patente: {av.patente}")
        else:
            print("🚫 No hay aviones registradas en este centro.")
        
        print(f"\nHelicopteros de {centro.nombre_cs}")
        if centro.helicopteros:
            for h in centro.helicopteros:
                print(f" - {h} (Patente: {h.patente}")
        else:
            print("🚫 No hay helicopteros registradas en este centro.")
        print(f"\nAmbulancias disponibles: {len(centro.ambulancias)}")
        print(f"\nAviones disponibles: {len(centro.aviones)}")
        print(f"\nHelicopteros disponibles: {len(centro.helicopteros)}")
                

        # Cirujanos
        print(f"\n🚑 Cirujanos disponibles de {centro.nombre_cs}:")
        if centro.generales:
            print(f"\n🩺 Cirujanos generales de {centro.nombre_cs}:")
            for g in centro.generales:
                print(f" - {g.nombre}")
        else:
            print("🛑 No hay cirujanos generales registrados en este centro.")
        if centro.especialistas:
            print(f"\n🩺 Cirujanos especialistas de {centro.nombre_cs}:")
            for e in centro.especialistas:
                print(f" - {e.nombre}")
        else:
            print("🛑 No hay cirujanos especialistas registrados en este centro.")
        print(f"\nCirujanos especialistas: {len(centro.especialistas)}")
        print(f"\nCirujanos generales: {len(centro.generales)}")
        return

    def informacion_incucai(self) -> None:
        """
        Muestra información estadística general del INCUCAI sobre donantes, receptores y centros.
        Args:
            - None
        Return:
            - None
        """
        print("\nInformacion sobre INCUCAI:")
        print(f"\nDONANTES REGISTRADOS: {len(self.donantes)}")
        print(f"\nRECEPTORES REGISTRADOS: {len(self.receptores)}")
        print(f"\nCENTROS REGISTRADOS: {len(self.centro)}")
        'agregar info sobre cirujanos y transplantes realizados'
        
#------------------------------------------------------------------------FIN DE METODOS ADICIONALES DE MENU-------------------------------------------------------------------------------
#------------------------------------------------------------------------INICIO METODOS PARA CARGA MANUAL--------------------------------------------------------------------------------------
    def pedir_datos_basicos_paciente(self):
        """
        Solicita al usuario la carga interactiva de datos básicos de un paciente receptor.
        Argumentos:
            -None
        Retorna:
            -Diccionario con todos los datos validados del paciente, incluyendo datos HLA.
                Campos clave:
                - nombre, DNI, fecha_nac, sexo, telefono, contacto, tipo_sangre, centro
                - hla_a1, hla_a2, hla_b1, hla_b2, hla_dr1, hla_dr2
                - que_es (valor fijo 'receptor')
        """
        datos = {}
        datos['nombre'] = self.validaciones('nombre')
        datos['DNI'] = self.validaciones('dni')
        datos['fecha_nac'] = self.validaciones('fecha_nacimiento')
        datos['sexo'] = self.validaciones('sexo')
        datos['telefono'] = self.validaciones('telefono')
        datos['contacto'] = self.validaciones('contacto_emergencia')
        datos['tipo_sangre'] = self.validaciones('tipo_sangre')
        datos['centro'] = self.validaciones('centro_salud')
        print("\n--- ANTÍGENOS HLA ---")
        datos['hla_a1'] = self.validaciones('antigeno-A1')
        datos['hla_a2'] = self.validaciones('antigeno-A2')
        datos['hla_b1'] = self.validaciones('antigeno-B1')
        datos['hla_b2'] = self.validaciones('antigeno-B2')
        datos['hla_dr1'] = self.validaciones('antigeno-DR1')
        datos['hla_dr2'] = self.validaciones('antigeno-DR2')
        

        return datos   
    
    def validaciones (self, validacion):
        """
        Solicita y valida distintos tipos de datos de entrada según el tipo de validación solicitado.
        Args:
            -validacion : str
                Tipo de dato a validar. 
        Return:
            -cualquier tipo --> El dato validado correspondiente al tipo de entrada solicitada.
        """
        
        if validacion=='nombre':
            while True:
                nombre = input("\nNombre completo: ").strip()
                if len(nombre) >= 2 and all(c.isalpha() or c.isspace() for c in nombre):
                    return nombre.title()
                print("\nNombre inválido. Solo letras y espacios.")     
        
        elif validacion=='dni':
            while True:
                dni = input("\n DNI: ").strip()
                if dni.isdigit() and 7 <= len(dni) <= 8:
                    dni_int = int(dni)
                    if any(p.DNI == dni_int for p in self.donantes + self.receptores):
                        print(f"Ya existe un paciente de DNI {dni} cargado")
                        continue
                    return dni_int
                print("\nDNI inválido. 7 u 8 dígitos.")
                
        elif validacion == "sexo":
            while True:
                sexo = input("Ingrese el sexo (masculino/femenino): ").strip().lower()
                if sexo in ["masculino", "femenino"]:
                    return sexo
                print("Sexo inválido. Debe ser 'masculino' o 'femenino'.")
                
        elif validacion == 'telefono':
            while True:
                telefono = input("\nTelefono: ").strip()
                telefono_solo_nros = ''.join(c for c in telefono if c.isdigit())
                
                if len(telefono_solo_nros) >= 8 and len(telefono_solo_nros) <= 15:
                    return telefono
                print("Teléfono inválido. Debe tener entre 8 y 15 dígitos.")
                
        elif validacion == 'contacto_emergencia':
            print("\nCONTACTO DE EMERGENCIA:")
            while True:
                telefono_contacto = input("   Teléfono: ").strip()
                tel_contacto_solo_nros = ''.join(c for c in telefono_contacto if c.isdigit())
                if len(tel_contacto_solo_nros) >= 8 and len(tel_contacto_solo_nros) <= 15:
                    return telefono_contacto
                print("Teléfono de contacto de emergencia inválido. Debe tener entre 8 y 15 dígitos.")
                
        elif validacion == 'tipo_sangre':
            tipos_sangre_validos = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
            while True:
                tipo = input(f"\nTipo de sangre {tipos_sangre_validos}: ").strip().upper()
                if tipo in tipos_sangre_validos:
                    return tipo
                print(f"Tipo de sangre inválido. Opciones válidas: {', '.join(tipos_sangre_validos)}")
                                
        elif validacion == 'centro_salud':
            print("Centros de salud elegibles para carga:")
            self.mostrar_centros_salud()
            while True:
                nombre_ingresado = input("\nIngrese el nombre del centro de salud: ").strip()
                if self.centro_valido(nombre_ingresado):
                    for centro in self.centro:
                        if centro.nombre_cs.strip().lower() == nombre_ingresado.lower():
                            print(f"Centro reconocido: {centro.nombre_cs}")
                            return centro
                print("Centro de salud no reconocido. Ingrese uno válido.")
                print("Centros disponibles:")
                self.mostrar_centros_salud()
                
        elif validacion == 'antigeno-A1':
            while True:
                hla_A1 = input("\nIngrese Antígeno A1 para HLA: ").strip().upper()
                if 2 <= len(hla_A1) <= 6:
                    if any(c.isdigit() for c in hla_A1):
                        return hla_A1
                    elif hla_A1.isdigit() and len(hla_A1) <= 3:
                        return hla_A1
                print("Formato HLA A1 inválido.")
                
        elif validacion == 'antigeno-A2':
            while True:
                hla_A2 = input("\nIngrese Antígeno A2 para HLA: ").strip().upper()
                if 2 <= len(hla_A2) <= 6:
                    if any(c.isdigit() for c in hla_A2):
                        return hla_A2
                    elif hla_A2.isdigit() and len(hla_A2) <= 3:
                        return hla_A2
                print("Formato HLA A2 inválido.")
            
        elif validacion == 'antigeno-B1':
            while True:
                hla_B1 = input("\nIngrese Antígeno B1 para HLA: ").strip().upper()
                if 2 <= len(hla_B1) <= 6:
                    if any(c.isdigit() for c in hla_B1):
                        return hla_B1
                    elif hla_B1.isdigit() and len(hla_B1) <= 3:
                        return hla_B1
                print("Formato HLA B1 inválido.")

        elif validacion== "antigeno-B2":
            while True:
                    hla_B2 = input("Ingrese Antígeno B2 para HLA: ").strip().upper()
                    if 2 <= len(hla_B2) <= 6:
                        if any(c.isdigit() for c in hla_B2):
                            return hla_B2
                        elif hla_B2.isdigit() and len(hla_B2) <= 3:
                            return hla_B2
                    print("Formato HLA B2 inválido.")
        
        elif validacion == 'antigeno-DR1':
            while True:
                    hla_DR1 = input("Ingrese Antígeno DR1 para HLA: ").strip().upper()
                    if 2 <= len(hla_DR1) <= 6:
                        if any(c.isdigit() for c in hla_DR1):
                            return hla_DR1
                        elif hla_DR1.isdigit() and len(hla_DR1) <= 3:
                            return hla_DR1
                    print("Formato HLA DR1 inválido.")
        
        elif validacion == 'antigeno-DR2':
            while True:
                    hla_DR2 = input("Ingrese Antígeno DR2 para HLA: ").strip().upper()
                    if 2 <= len(hla_DR2) <= 6:
                        if any(c.isdigit() for c in hla_DR2):
                            return hla_DR2
                        elif hla_DR2.isdigit() and len(hla_DR2) <= 3:
                            return hla_DR2
                    print("Formato HLA DR2 inválido.")
        
        elif validacion=='fecha_nacimiento':
            while True:
                fecha = input("\nFecha de nacimiento (yyyy/mm/dd): ").strip()
                try:
                    fecha = datetime.strptime(fecha, "%Y/%m/%d")
                    hoy = datetime.now()
                    edad = (hoy - fecha).days // 365
                    
                    if edad < 0:
                        print("La fecha no puede ser futura.")
                        continue
                    elif edad > 100:
                        print("Fecha demasiado antigua.")
                        continue
                    elif edad < 1:
                        print("El paciente debe tener al menos 1 año para recibir o donar un organo")
                        continue
                    return fecha
                except ValueError:
                    print("Formato  de fecha invalido. Use yyyy/mm/dd.")
        
        elif validacion == 'estado_donante':
            while True:
                estado = input("   Ingrese estado del donante (vivo/muerto): ").strip().lower()
                if estado in ["vivo", "muerto"]:
                    return estado
                print("Estado inválido. Debe ingresar 'vivo' o 'muerto'.")
        
        elif validacion == 'fecha_fall':
            while True:
                fecha = input("Fecha de fallecimiento (yyyy/mm/dd): ").strip()
                try:
                    fecha_obj = datetime.strptime(fecha, "%Y/%m/%d")
                    if fecha_obj > datetime.now():
                        print("La fecha de fallecimiento no puede ser futura.")
                        continue
                    return fecha_obj
                except ValueError:
                    print("Fecha inválida. Use formato yyyy/mm/dd.")

        elif validacion == 'hora_fall':
            while True:
                hora = input("Hora de fallecimiento (HH:MM): ").strip()
                try:
                    return datetime.strptime(hora, "%H:%M").time()
                except ValueError:
                    print("Hora inválida. Use formato HH:MM.")

        elif validacion == 'hora_ablacion':
            while True:
                hora_ablacion = input("Hora de ablacion (HH:MM): ").strip()
                try:
                    return datetime.strptime(hora_ablacion, "%H:%M").time()
                except ValueError:
                    print("Hora inválida. Use formato HH:MM.")
            
        elif validacion == 'fecha_ablacion':    
            while True:
                fecha_ablacion = input("Fecha de ablacion (yyyy/mm/dd): ").strip()
                try:
                    fecha_obj = datetime.strptime(fecha_ablacion, "%Y/%m/%d")
                    if fecha_obj > datetime.now():
                        print("La fecha de ablacion no puede ser futura.")
                        continue
                    return fecha_obj
                except ValueError:
                    print("Fecha inválida. Use formato yyyy/mm/dd.")
            
        elif validacion == 'organos_a_donar':
            print("   Ingrese los órganos a donar (separados por coma):")
            while True:
                entrada = input("   Ej: riñón, hígado, corazón: ").strip()
                organos = [o.strip().lower() for o in entrada.split(',') if o.strip()]
                if organos:
                    return organos
                print("Debe ingresar al menos un órgano.")

        elif validacion == 'patologia':
            while True:
                patologia = input("Ingrese la patología del receptor: ").strip()
                if len(patologia) >= 3:
                    return patologia
                print("Patología inválida.")

        elif validacion == 'organos_a_recibir':
            print("Ingrese los órganos que necesita (separados por coma):")
            while True:
                entrada = input("Ej: riñón, hígado: ").strip()
                organos = [o.strip().lower() for o in entrada.split(',') if o.strip()]
                if organos:
                    return organos
                print("Debe ingresar al menos un órgano.")

        elif validacion == 'estado':
            while True:
                estado = input("   Estado del receptor (estable/inestable): ").strip().lower()
                if estado in ["estable", "inestable"]:
                    return estado
                print("Estado inválido. Opciones válidas: estable / inestable.")

        elif validacion == 'lista_espera':
            while True:
                fecha = input("   Fecha de ingreso a lista de espera (yyyy/mm/dd): ").strip()
                try:
                    return datetime.strptime(fecha, "%Y/%m/%d").date()
                except ValueError:
                    print("Fecha inválida. Use formato yyyy/mm/dd.")
                    
        elif validacion == 'que_es':
            while True:
                que_es = input (" Que tipo de paciente es? DONANTE O RECEPTOR").strip().lower()
                if que_es in ["receptor","donante"]:
                    return que_es
                print ("Tipo de paciente invalido. Opciones validas: receptor / donante")
    
    def carga_manual_donante_nuevo(self):
        '''
        Inicia la carga manual interactiva de un nuevo paciente del tipo donante.
        1. Solicita datos generales del paciente mediante `pedir_datos_basicos_paciente()`.
        2. Solicita datos específicos del donante (estado, fallecimiento, órganos a donar).
        3. Crea una instancia de 'Donante' y la agrega al listado de donantes.
        
        Args:
            -None
        Return:
            -donante_nuevo: Donante, longitud array de donantes: int
        '''
        print("\nSeleccionó la carga manual de un nuevo paciente del tipo donante. Esta funcion es valida para donantes fallecidos. Se tomara la fecha de la ablacion general.")
        print("\n --- DONANTE NUEVO: --- ")
        paciente_nuevo_base = self.pedir_datos_basicos_paciente()
        print("\n -Datos extra de donante:")
        datos_donante = {}
        
        datos_donante['fecha_fall'] = self.validaciones('fecha_fall')
        datos_donante['hora_fall'] = self.validaciones('hora_fall')
        #datos_donante['lista_organos'] = self.validaciones('organos_a_donar')
        datos_donante['hora_ablacion'] = self.validaciones('hora_ablacion')
        datos_donante['fecha_ablacion']=self.validaciones('fecha_ablacion')
        
        paciente_nuevo_base['que_es'] = 'donante'
        datos_donante['estado_donante']='muerto'
        
        
        datos_donante['lista_organos'] = Organo.organos_validos.copy()
        
        datos_completos = {**paciente_nuevo_base, **datos_donante}
        
        donante_nuevo = Donante(**datos_completos)
        self.donantes.append(donante_nuevo)
        print(f"\n-Donante: {donante_nuevo.nombre} cargado exitosamente.")
        return (donante_nuevo, len(self.donantes))
    
    def carga_manual_receptor_nuevo(self):
        '''
        Inicia la carga manual interactiva de un nuevo paciente del tipo receptor.
        1. Solicita datos generales del paciente mediante `pedir_datos_basicos_paciente()`.
        2. Solicita datos específicos del receptor (organos a recibir, fecha lista de espera, patologia, estado).
        3. Crea una instancia de 'Donante' y la agrega al listado de donantes.
        
        Args:
            -None
        Return:
            -receptor_nuevo: Receptor, longitud array de receptores: int
        '''
        print ("\nSeleccionó la carga manual de un nuevo paciente del tipo receptor...") #--> opcion en el menu
        print("\n --- RECEPTOR NUEVO: --- ")
        
        paciente_nuevo_base=self.pedir_datos_basicos_paciente()
        print("\n -Datos extra de receptor:")
        datos_receptor={}
        datos_receptor['org_recib']=self.validaciones('organos_a_recibir')
        datos_receptor['fecha_list_esp']=self.validaciones('lista_espera')   
        datos_receptor['patologia']=self.validaciones('patologia')
        datos_receptor['estado'] = self.validaciones('estado') 
        
        paciente_nuevo_base['que_es'] = 'receptor'
        
        
        datos_completos = {**paciente_nuevo_base, **datos_receptor}
        print(datos_completos)
        receptor_nuevo = Receptor(**datos_completos)
        self.receptores.append(receptor_nuevo)
        print(f"\nReceptor {receptor_nuevo.nombre} cargado exitosamente.")
        return (receptor_nuevo, len(self.receptores))
#------------------------------------------------------------------------FIN METODOS PARA CARGA MANUAL--------------------------------------------------------------------------------------