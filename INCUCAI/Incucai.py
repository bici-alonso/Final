'''
TRABAJO PRACTICO FINAL - LABO DE PROGRAMACION I. SIMULACION SIST. DONACION DE ORGANOS - INCUCAI
El INCUCAI se encarga de la coordinación y logística de la donación de tejidos y órganos. 
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
from INCUCAI.Paciente.Donante import Donante 
from INCUCAI.Paciente.Receptor import Receptor
from INCUCAI.Centros.Centro import Centro_de_salud 
from geopy.geocoders import Nominatim
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
    
    #incucai debe tener una validacion que ningun paciente se repite
    #debo sacar de la lista a pacientes que no tiene mas organos para donar
    #debo sacar a los receptores que tuvieron un transplante exitoso
    
    
    METODOS DE INCUCAI:
    
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
    
    geolocator = Nominatim(user_agent="incucai_test")
    
    def __init__(self):
        #Constructor de INCUCAI
        self.receptores = []
        self.donantes = []
        self.centros = self.centros()
        
    def centros(self):
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
        
    def clasificar_paciente_ya_existente(self, paciente_existente=None):
            if paciente_existente:
                if isinstance(paciente_existente, Donante):
                    if self.paciente_existente(paciente_existente.DNI): 
                        return
                    self.donantes.append(paciente_existente)
                    self.procesar_donacion_multiple(paciente_existente) #cuando uso el de donacion de un organo?
                    return
                    
                if isinstance(paciente_existente, Receptor):
                    if self.paciente_existente(paciente_existente.DNI): 
                        return
                    self.receptores.append(paciente_existente)
                    self.buscar_match_para_receptor(paciente_existente)
                    return
    
    def paciente_existente(self, dni):
        if any(p.DNI == dni for p in self.donantes + self.receptores):
            print(f"Ya existe un paciente con DNI {dni}.")
            return True
        return False
    
    def compatibilidad(self, donante, receptor):
        if not donante.es_compatible_sangre(receptor):
            return False
        hla_match, _ = donante.compatibilidad_hla(receptor)
        if hla_match < 3:
            return False
        edad_donante = donante.calculo_edad()
        edad_receptor = receptor.calculo_edad()
        if edad_receptor < 18 and abs(edad_receptor - edad_donante) > 3:
            return False
        return True

    def buscar_receptor_organo_especifico(self, donante, organo):
        print(f"\nBuscando receptor para {organo} del donante {donante.nombre}...")
        compatibles = [r for r in self.receptores if organo.lower() in r.org_recib and self.compatibilidad(donante, r)]
        if compatibles:
            receptor = self.elegir_receptor(compatibles)
            self.procesar_asignacion(donante, receptor, organo)
        else:
            print(f"No se encontro receptor compatible para {organo}.")
            
    def buscar_match_para_receptor(self, receptor):
        for donante in self.donantes:
            for organo in donante.lista_organos:
                if organo.lower() in receptor.org_recib and self.validar_compatibilidad(donante, receptor):
                    self.procesar_asignacion(donante, receptor, organo)
                    return
        print(f"No hay donante compatible para {receptor.nombre}.")

    def procesar_donacion_multiple(self, donante):
        print(f"\nProcesando donación de {donante.nombre}...")
        for organo in donante.lista_organos[:]:  # copia para modificar e iterar
            self.buscar_receptor_organo_especifico(donante, organo)

    def elegir_receptor(self, lista):
        return sorted(lista, key=lambda r: (r.prioridad_numerica(), r.fecha_list_esp))[0]

    def procesar_asignacion(self, donante, receptor, organo):
        print(f"\nAsignación: {organo} de {donante.nombre} a {receptor.nombre}")
        donante.lista_organos = [o for o in donante.lista_organos if o.lower() != organo.lower()]
        if not donante.lista_organos:
            self.donantes.remove(donante)
        self.receptores.remove(receptor)
            
    def procesar_asignacion(self, donante, receptor, organo):
        print(f"\nAsignando {organo} de {donante.nombre} a {receptor.nombre} en {receptor.centro}")
        donante.lista_organos = [o for o in donante.lista_organos if o.lower() != organo.lower()]
        if not donante.lista_organos:
            self.donantes.remove(donante)
            print(f"Donante {donante.nombre} removido (sin órganos disponibles)")
        if receptor in self.receptores:
            self.receptores.remove(receptor)
            print(f"Receptor {receptor.nombre} removido (trasplante programado)")

    def mostrar_centros_salud(self):
        print("\nCentros de salud habilitados:")
        for cs in self.centros:
            print(f"- {cs}")

    def listar_donantes(self):
        for d in self.donantes:
            print(d)

    def listar_receptores(self):
        for r in self.receptores:
            print(r)

    
    '''
    def pedir_datos_basicos_paciente(self):
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
    '''     
    
    '''      
    def validaciones (self, validacion):
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
                
        elif validacion == 'sexo':
            sexos_validos = {
                'M': 'MASCULINO',
                'F': 'FEMENINO'
            }
            while True:
                sexo = input("\nSexo [F/M]: ").strip().upper()
                if sexo in sexos_validos:
                    return sexos_validos[sexo]
                print("\nIngrese 'M' para masculino o 'F' para femenino.")
                
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
                print(f"Tipo de sangre inválido. Opciones validas: A+, A-, B+, B-, AB+, AB-, O+, O-")
                
        elif validacion == 'antigeno-A1':
            while True:
                hla_A1 = input("\nIngrese Antígeno A1 para HLA: ").strip().upper()
                if 2 <= len(hla_A1) <= 6:
                    if any(c.isalpha() for c in hla_A1) and any(c.isdigit() for c in hla_A1):
                        return hla_A1
                    elif hla_A1.isdigit() and len(hla_A1) <= 3:
                        return hla_A1
                print("Formato HLA A1 inválido.")
                
        elif validacion == 'antigeno-A2':
            while True:
                hla_A2 = input("\nIngrese Antígeno A2 para HLA: ").strip().upper()
                if 2 <= len(hla_A2) <= 6:
                    if any(c.isalpha() for c in hla_A2) and any(c.isdigit() for c in hla_A2):
                        return hla_A2
                    elif hla_A2.isdigit() and len(hla_A2) <= 3:
                        return hla_A2
                print("Formato HLA A2 inválido.")
            
        elif validacion == 'antigeno-B1':
            while True:
                hla_B1 = input("\nIngrese Antígeno B1 para HLA: ").strip().upper()
                if 2 <= len(hla_B1) <= 6:
                    if any(c.isalpha() for c in hla_B1) and any(c.isdigit() for c in hla_B1):
                        return hla_B1
                    elif hla_B1.isdigit() and len(hla_B1) <= 3:
                        return hla_B1
                print("Formato HLA B1 inválido.")

        elif validacion== "antigeno-B2":
            while True:
                    hla_B2 = input("   Ingrese Antígeno A2 para HLA: ").strip().upper()
                    if 2 <= len(hla_B2) <= 6:
                        if any(c.isalpha() for c in hla_B2) and any(c.isdigit() for c in hla_B2):
                            return hla_B2
                        elif hla_B2.isdigit() and len(hla_B2) <= 3:
                            return hla_B2
                    print("Formato HLA B2 inválido.")
        
        elif validacion == 'antigeno-DR1':
            while True:
                    hla_DR1 = input("   Ingrese Antígeno DR1 para HLA: ").strip().upper()
                    if 2 <= len(hla_DR1) <= 6:
                        if any(c.isalpha() for c in hla_DR1) and any(c.isdigit() for c in hla_DR1):
                            return hla_DR1
                        elif hla_DR1.isdigit() and len(hla_DR1) <= 3:
                            return hla_DR1
                    print("Formato HLA DR1 inválido.")
        
        elif validacion == 'antigeno-DR2':
            while True:
                    hla_DR2 = input("   Ingrese Antígeno DR2 para HLA: ").strip().upper()
                    if 2 <= len(hla_DR2) <= 6:
                        if any(c.isalpha() for c in hla_DR2) and any(c.isdigit() for c in hla_DR2):
                            return hla_DR2
                        elif hla_DR2.isdigit() and len(hla_DR2) <= 3:
                            return hla_DR2
                    print("Formato HLA DR2 inválido.")
        
        elif validacion=='fecha_nac':
            while True:
                fecha = input("\nFecha de nacimiento (dd/mm/yyyy): ").strip()
                try:
                    fecha = datetime.strptime(fecha, "%d/%m/%Y")
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
                    print("Formato  de fecha invalido. Use dd/mm/yyyy.")
            
        elif validacion == 'centro_salud':
            # Lista de nombres válidos (tal como están cargados)
            nombres_centros_validos = [centro.nombre_cs for centro in self.centros]
            while True:
                nombre_ingresado = input("\nIngrese el nombre del centro de salud: ").strip()
                for centro in self.centros:
                    if centro.nombre_cs.lower() == nombre_ingresado.lower():
                        return centro
                print("Centro de salud no reconocido. Ingrese uno válido.")
                print("Centros disponibles:")
                for nombre in nombres_centros_validos:
                    print(f"   - {nombre}")
        
        elif validacion=='estado_donante':
            estados_donante_validos=["vivo", "muerto"]
            while True:
                estado = input("   Ingrese estado del donante (vivo/muerto): ").strip().lower()
                if estado in estados_donante_validos:
                    return estado
                print("Estado inválido. Debe ingresar 'vivo' o 'muerto'.")
        
        elif validacion=='fecha_fall':
            while True:
        '''  
        
                
    '''           
    def pedir_datos_basicos_paciente(self):
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
        ''' 
        
    '''  
    def carga_manual_donante_nuevo(self):
        print ("\nSelecciono la carga manual de un nuevo paciente del tipo donante...") #--> opcion en el menu
        print("\nDONANTE NUEVO:")
        paciente_nuevo_base=self.pedir_datos_basicos_paciente()
        print("\nDatos extra de donante:")
        datos_donante={}
        datos_donante['estado_donante']=self.validaciones('estado_donante')
        datos_donante['fecha_fall'] = self.validaciones('fecha_fall')
        datos_donante['hora_fall']=self.validaciones('hora_fall')
        datos_donante['organos_a_donar']=self.validaciones('organos_a_donar')
        
        self.donantes.append(donante_nuevo)
        
    '''  
        
    
    '''  
    def carga_manual_receptor_nuevo(self):
        print ("\nSelecciono la carga manual de un nuevo paciente del tipo receptor...") #--> opcion en el menu
        print("\nRECEPTOR NUEVO:")
        paciente_nuevo_base=self.pedir_datos_basicos_paciente()
        print("\nDatos extra de receptor:")
        datos_receptor={}
        datos_receptor['patologia']=self.validaciones('patologia')
        datos_receptor['organos_a_recibir']=self.validaciones('organos_a_recibir')
        datos_receptor['estado'] = self.validaciones('estado')
        datos_receptor['fecha_lista_espera']=self.validaciones('lista_espera')
    
        
        
        self.receptores.append(receptor_nuevo)
    '''  
    
    #def cargar_nuevo_centro(self):
        #print ("\nSelecciono la carga manual de un nuevo centro de salud...") #--> opcion en el menu
        #print("\nCENTRO DE SALUD NUEVO:")
        

