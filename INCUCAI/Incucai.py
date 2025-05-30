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
import unicodedata

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
        aux_centro=self.centros()
        self.centro = aux_centro
        
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
        
    def registrar_donante(self, donante):
        if not  self.paciente_existente(donante.DNI):
            self.donantes.append(donante)

    def registrar_receptor(self, receptor):
        if not self.paciente_existente(receptor.DNI):
            self.receptores.append(receptor)
    
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
    
    def proceso_transplante():
        return
    
    def buscar_paciente_por_dni(self, dni):
        for p in self.donantes + self.receptores:
            if p.DNI == dni:
                return p 
        return None
    
    
    def buscar_centro_por_nombre(self, nombre_centro):
        for centro in self.centro:
            if nombre_centro.strip().lower() == centro.nombre_cs.strip().lower():
                return centro

        print(f"❌ No se encontró el centro: '{nombre_centro}'")
        return None


    
    def buscar_receptor_por_dni(self, dni):
        try:
            dni = int(dni)
        except ValueError:
            print("❌ El DNI ingresado no es válido.")
            return None

        # Ordenar por fecha de ingreso a la lista de espera
        lista_ordenada = sorted(self.receptores, key=lambda r: r.fecha_list_esp)

        for idx, receptor in enumerate(lista_ordenada):
            if int(receptor.DNI) == dni:
                print(f"\n🔍 El paciente '{receptor.nombre}' (DNI: {dni}) está en la posición {idx + 1} de la lista de espera.")
                print(f"📋 Hay {idx} paciente(s) antes en la lista.")
                return receptor

        print(f"❌ No se encontró ningún receptor con el DNI {dni} en la lista de espera.")
        return None
    
    

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
                if organo.lower() in receptor.org_recib and self.compatibilidad(donante, receptor):
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
        for cs in self.centro:
            print(f"- {cs}")
            
    def receptores_por_centro_salud(self, nombre_centro):
        # Usamos el atributo correcto: nombre_cs
        nombres_validos = [c.nombre_cs.lower() for c in self.centro]

        if nombre_centro.lower() not in nombres_validos:
            print("❌ Centro de salud no registrado. Intente nuevamente con un nombre válido.")
            print("\n📋 Centros disponibles:")
            for c in self.centro:
                print(f"- {c.nombre_cs}")
            return

        # Filtrar receptores según centro
        receptores_centro = [r for r in self.receptores if r.centro.lower() == nombre_centro.lower()]
        
        if not receptores_centro:
            print("⚠️ No hay receptores en lista de espera en ese centro.")
            return

        print(f"\n📋 Receptores en el centro '{nombre_centro}':\n")
        for r in sorted(receptores_centro, key=lambda r: r.fecha_list_esp):
            print(f"- {r.nombre} (DNI: {r.DNI}, Fecha ingreso: {r.fecha_list_esp}, Estado: {r.estado}, Órganos: {', '.join(r.org_recib)})")

    def centro_valido(self, nombre_centro):
        nombres_validos = [c.nombre_cs.lower() for c in self.centro]
        return nombre_centro.lower() in nombres_validos

    def listar_donantes(self):
        for d in self.donantes:
            print(d)

    def listar_receptores(self):
        for r in self.receptores:
            print(r)
    
    def lista_espera_ordenada(self):
        if not self.receptores:
            print("No hay receptores en la lista de espera.")
            return []
        receptores_ordenados = sorted(self.receptores, key=lambda r: r.fecha_list_esp)
    
        print("\n📋 Lista de espera ordenada por fecha de ingreso:")
        for idx, receptor in enumerate(receptores_ordenados, 1):
            print(f"{idx}. {receptor.nombre} (DNI: {receptor.DNI}) - "
                f"Fecha ingreso: {receptor.fecha_list_esp.strftime('%d/%m/%Y')} - "
                f"Estado: {receptor.estado} - Prioridad: {receptor.prioridad_numerica()}")
        return receptores_ordenados
        
    def realizar_transplante(self, receptor, donante, organo):
        print(f"Centros cargados en INCUCAI: {[c.nombre_cs for c in self.centro]}")

        print(f"\n➡️ Iniciando protocolo de trasplante para {receptor.nombre} (DNI: {receptor.DNI}) con órgano {organo.upper()}")

        centro_donante = self.buscar_centro_por_nombre(donante.centro)
        centro_receptor = self.buscar_centro_por_nombre(receptor.centro)

        print(f"Donante centro: '{donante.centro}'")
        print(f"Receptor centro: '{receptor.centro}'")


        if not centro_donante or not centro_receptor:
            print("❌ No se encontraron los centros de salud correspondientes.")
            return
        
        if centro_donante.coords is None:
            centro_donante.geolocalizar_direccion(self.geolocator)
        if centro_receptor.coords is None:
            centro_receptor.geolocalizar_direccion(self.geolocator)
        
        if not centro_donante.realizar_ablacion(organo, donante):
            print("❌ Error en la ablación. Operación cancelada.")
            return
        
        vehiculo = centro_donante.seleccionar_vehiculo(centro_receptor)
        if vehiculo is None:
            print("❌ No hay vehículos disponibles para trasladar el órgano.")
            return
        
        distancia = centro_donante.calcular_distancia_a(centro_receptor)
        trafico = vehiculo.nivel_trafico()
        tiempo_traslado = vehiculo.calculo_tiempo(distancia, trafico)
        print(f"\n🚑 Vehículo seleccionado: {vehiculo}")
        print(f"Distancia entre centros: {distancia:.2f} km | Tráfico: {trafico:.2f} | Tiempo estimado: {tiempo_traslado:.2f} h")

        cirujano = centro_receptor.seleccionar_cirujano(organo.tipo)
        if cirujano is None:
            print("❌ No hay cirujano disponible para ese órgano.")
            return
        
        print(f"🩺 Cirujano asignado: {cirujano}")

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

    def pedir_receptor_para_realizar_transplante(self):
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
                if organo.lower() in organos_necesarios and self.compatibilidad(donante, receptor):
                    compatibles.append((donante, organo))

        if not compatibles:
            print("❌ No hay donantes compatibles para este receptor.")
            return
        
        print(f"\n✅ Donantes compatibles encontrados para {receptor.nombre}:")
        for i, (d, o) in enumerate(compatibles):
            print(f"{i+1}. Donante: {d.nombre} (DNI: {d.DNI}) - Órgano: {o}")

        try:
            seleccion = int(input("\nSeleccione el numero del donnate con el que desea proceder: "))
            donante, organo = compatibles[seleccion - 1]
            self.realizar_transplante(receptor, donante, organo)
        except (IndexError, ValueError):
            print("❌ Selección inválida.")

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
                fecha = input("   Fecha de fallecimiento (dd/mm/yyyy): ").strip()
                try:
                    return datetime.strptime(fecha, "%d/%m/%Y")
                except ValueError:
                    print("Fecha inválida. Use formato dd/mm/yyyy.")

        elif validacion == 'hora_fall':
            while True:
                hora = input("   Hora de fallecimiento (HH:MM): ").strip()
                try:
                    return datetime.strptime(hora, "%H:%M").time()
                except ValueError:
                    print("Hora inválida. Use formato HH:MM.")

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
                patologia = input("   Ingrese la patología del receptor: ").strip()
                if len(patologia) >= 3:
                    return patologia
                print("Patología inválida.")

        elif validacion == 'organos_a_recibir':
            print("Ingrese los órganos que necesita (separados por coma):")
            while True:
                entrada = input("   Ej: riñón, hígado: ").strip()
                organos = [o.strip().lower() for o in entrada.split(',') if o.strip()]
                if organos:
                    return organos
                print("Debe ingresar al menos un órgano.")

        elif validacion == 'estado':
            opciones = ["activo", "inactivo", "urgente"]
            while True:
                estado = input("   Estado del receptor (activo/inactivo/urgente): ").strip().lower()
                if estado in opciones:
                    return estado
                print("Estado inválido. Opciones: activo, inactivo, urgente.")

        elif validacion == 'lista_espera':
            while True:
                fecha = input("   Fecha de ingreso a lista de espera (dd/mm/yyyy): ").strip()
                try:
                    return datetime.strptime(fecha, "%d/%m/%Y")
                except ValueError:
                    print("Fecha inválida. Use formato dd/mm/yyyy.")
                    
        
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
        
        
    def carga_manual_donante_nuevo(self):
        print("\nSeleccionó la carga manual de un nuevo paciente del tipo donante...")
        print("\nDONANTE NUEVO:")
        paciente_nuevo_base = self.pedir_datos_basicos_paciente()
        
        print("\nDatos extra de donante:")
        datos_donante = {}
        datos_donante['estado_donante'] = self.validaciones('estado_donante')
        datos_donante['fecha_fall'] = self.validaciones('fecha_fall')
        datos_donante['hora_fall'] = self.validaciones('hora_fall')
        datos_donante['organos_a_donar'] = self.validaciones('organos_a_donar')
        
        datos_completos = {**paciente_nuevo_base, **datos_donante}
        donante_nuevo = Donante(**datos_completos)
        
        self.donantes.append(donante_nuevo)
        print(f"\nDonante {donante_nuevo.nombre} cargado exitosamente.")
            
    
    
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

        datos_completos = {**paciente_nuevo_base, **datos_receptor}
        receptor_nuevo = Receptor(**datos_completos)
    
        self.receptores.append(receptor_nuevo)
        print(f"\nReceptor {receptor_nuevo.nombre} cargado exitosamente.")
    
    
        

