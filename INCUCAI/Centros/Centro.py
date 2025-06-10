'''
TRABAJO PRACTICO FINAL - LABO DE PROGRAMACION I. 
SIMULACION SIST. DONACION DE ORGANOS

Alonso Victoria - Pfeifer Zoe

CLASE DE CENTROS DE SALUD: 
Requisitos, estructura y comportamiento:

Acerca de los centros de salud: 
-> Tienen los siguientes datos: [ATRIBUTOS]
        Nombre
        Dirección
        Partido
        Provincia
        Teléfono
        Una lista de cirujanos 
        Una lista de vehículos.

-> Los centros de salud asignan un vehiculo para el transporte del órgano.  Esta selección de vehículos se realiza en base a la distancia:
        Si se encuentra en la misma provincia y partido: Uso del vehiculo disponible de mayor velocidad pero que no se use para distancias mayores. 
        Si se encuentra en la misma provincia, pero en un partido distinto, se utiliza el helicóptero.
        Si discierne la provincia se utiliza el avión.

Una vez que el INCUCAI encontró un match, inicia el protocolo de transporte y trasplante:
    Este le pide al centro de salud del DONANTE que asigne un vehículo y un cirujano. 
    Una vez que se asignó el vehículo, el centro procede a realizar la ablación del órgano que necesita el receptor. 
    En la ablación se setea la fecha y horario de ablación del órgano y se quita el órgano removido de la lista de órganos del paciente donante.
    Ese vehículo realiza el transporte (el cual demora un tiempo dependiendo de la distancia). 

Finalmente, el centro de salud del receptor realiza el trasplante: 
Para realizar el trasplante se verifica que no hayan transcurrido más de 20 horas desde la ablación del órgano y procede a realizar el trasplante con el cirujano elegido: 
        -> Si el trasplante es exitoso, se remueve al paciente receptor de la lista de pacientes receptores. 
        -> Si el trasplante falla, se cambia la prioridad del paciente receptor a la de mayor prioridad y se setea su estado a inestable.
    Si el trasplante es exitoso o no se define con un valor aleatorio que varia dependiendo de la especialidad del cirujano.

'''


#LIBRERIAS
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from geopy.exc import GeocoderTimedOut
import time
from datetime import datetime

from INCUCAI.Centros.Cirujanos.Especialista import Especialista
from INCUCAI.Centros.Cirujanos.General import General #ESTO ES LEGAL????????????????????????/ CREO QUE NO


from INCUCAI.Vehiculo.Ambulancia import Ambulancia
from INCUCAI.Vehiculo.Avion import Avion
from INCUCAI.Vehiculo.Helicoptero import Helicoptero


class Centro_de_salud:

    def __init__(self, nombre_cs, direccion, barrio, provincia, tel_contacto):
        if not all([nombre_cs, direccion, barrio, provincia, tel_contacto]):
            raise ValueError("Todos los campos son obligatorios.")        
        
        self.pais = "Argentina"
        self.nombre_cs = nombre_cs.strip()
        self.direccion = direccion.strip()
        self.ciudad = barrio.strip()
        self.provincia = provincia.strip()
        self.tel_contacto = tel_contacto.strip()
        self.cirujanos = []
        self.vehiculos = []
        
        self.especialistas =[]
        self.generales =[]
        
        self.ambulancias=[]
        self.aviones=[]
        self.helicopteros=[]
        
        self.coords = None

    def direccion_completa(self):
        return f"{self.direccion}, {self.ciudad}, {self.provincia}, {self.pais}"

    def geolocalizar_direccion(self, geolocator, intentos=3):
        direccion = self.direccion_completa()
        for i in range(intentos):
            try:
                location = geolocator.geocode(direccion)
                if location:
                    self.coords = (location.latitude, location.longitude)
                    return location
            except GeocoderTimedOut:
                print(f"⏱️ Timeout al intentar geolocalizar '{direccion}', intento {i + 1} de {intentos}")
                time.sleep(1)
        print(f"❌ No se pudo geolocalizar '{direccion}' después de {intentos} intentos")
        return None

    def calcular_distancia_a(self, otro_centro):
        if self.coords is None or otro_centro.coords is None:
            print("\nUno o ambos centros no tienen coordenadas geográficas.")
        return geodesic(self.coords, otro_centro.coords).kilometers
    
    
    def agregar_cirujano(self, cirujano):
        if cirujano not in self.cirujanos:
            self.cirujanos.append(cirujano)
    
    def agregar_cirujano_especialista(self, cirujano: Especialista):
        if cirujano not in self.especialistas:
            self.especialistas.append(cirujano)
    
    def agregar_cirujano_general(self, cirujano: General):
        if cirujano not in self.especialistas:
            self.generales.append(cirujano)
    
            
    def agregar_vehiculo(self, vehiculo):
        if vehiculo not in self.vehiculos:
            self.vehiculos.append(vehiculo)
    
    def agregar_ambulancia(self, vehiculo: Ambulancia):
        if vehiculo not in self.ambulancias:
            self.ambulancias.append(vehiculo)
    
            
    def agregar_avion(self, vehiculo: Avion):
        if vehiculo not in self.aviones:
            self.aviones.append(vehiculo)

    def agregar_helicoptero(self, vehiculo: Helicoptero):
        if vehiculo not in self.helicoptero:
            self.helicopteros.append(vehiculo)
            
    def seleccionar_vehiculo(self, centro_destino):
        if not self.vehiculos:
            raise ValueError("No hay vehículos disponibles en este centro")
            
        #misma provincia y ciudad/barrio:
        if (self.provincia.lower() == centro_destino.provincia.lower() and 
            self.ciudad.lower() == centro_destino.ciudad.lower()):

            ambulancias = [v for v in self.vehiculos if v.__class__.__name__ == 'Ambulancia'] #crea nuevo array de ambulancias, solo incluye a las ambulancias de mi array de vehiculos
            '''
            equivalente a:
            ambulancias = []
            for vehiculo in self.vehiculos:
                if isinstance(vehiculo, Ambulancia):
                    ambulancias.append(vehiculo)
                if ambulancias:
                    ambulancia_mas_rapida = ambulancias[0]
                    for ambulancia in ambulancias:
                        if ambulancia.velocidad > ambulancia_mas_rapida.velocidad:
                            ambulancia_mas_rapida = ambulancia
            return ambulancia_mas_rapida
            '''
            if ambulancias:
                return max(ambulancias, key=lambda x: x.velocidad) #usa el atributo de velocidad para elegir a la ambulancia de mayor velocidad
        
        #misma provincia pero diferente ciudad
        elif self.provincia.lower() == centro_destino.provincia.lower():
            #buscar helicóptero
            helicopteros = [v for v in self.vehiculos if v.__class__.__name__ == 'Helicoptero']
            if helicopteros:
                return helicopteros[0]  # Primer helicóptero disponible
        
        #diferentes provincias
        else:
            # Buscar avión
            aviones = [v for v in self.vehiculos if v.__class__.__name__ == 'Avion']
            if aviones:
                return aviones[0]  # Primer avión disponible
        
        
        return self.vehiculos[0] if self.vehiculos else None #usar cualquiera disponible si no hay el tipo deseado
    
    def seleccionar_cirujano(self, organo):
        disponibles = [c for c in self.cirujanos if c.cirujano_disponible()]
        for c in disponibles:
            if hasattr(c, 'especialidad') and organo.lower() in c.organos.get(c.especialidad, []):
                return c
        return disponibles[0] if disponibles else None
        
    def realizar_ablacion(self, organo, donante):
        """
        Realiza la ablación de un órgano.
            organo (Organo): Órgano 
            donante: Paciente donante
            
            retorna bool: True si la ablación fue exitosa
        """
        try:
            # Setear fecha y hora de ablación usando el método de la clase Organo
            ahora = datetime.now()
            organo.set_ablacion_auto(ahora.date(), ahora.time())
            
            # Quitar órgano de la lista del donante
            if organo in donante.lista_organos:
                donante.lista_organos.remove(organo)
                print(f"✅ Ablación exitosa de {organo.tipo.capitalize()} en {self.nombre_cs}")
                print(f"⏰ Tiempo máximo de conservación: {organo.get_tiempo_conservacion()} horas")
                return True
            
            print(f"❌ Error: el órgano no está en la lista del donante")
            return False
            
        except Exception as e:
            print("hola5")
            print(f"❌ Error durante la ablación: {e}")
            return False

    def realizar_transplante(self, organo, receptor, cirujano):
        """
        Realiza el trasplante de un órgano.
            organo: a trasplantar
            receptor: Paciente receptor
            cirujano: Cirujano que realizará la operación
            
            retorna bool: True si el trasplante fue exitoso
        """
        # Verificar viabilidad del órgano usando los métodos de la clase Organo
        if not organo.es_viable_para_trasplante():
            tiempo_transcurrido = organo.calcular_tiempo_transcurrido()
            print(f"Órgano no viable - han pasado {tiempo_transcurrido:.1f} horas desde la ablación")
            print(f"Tiempo máximo permitido: {organo.get_tiempo_conservacion()} horas")
            return False
        
        #info del organo antes del trasplante
        tiempo_restante = organo.calcular_tiempo_restante()
        print(f"\nTiempo restante para trasplante: {tiempo_restante:.1f} horas")
        
        # Realizar trasplante usando el cirujano
        try:
            exito = cirujano.exito_operacion(organo)
            
            if exito:
                print(f"✅ Trasplante exitoso de {organo.tipo.capitalize()} en {self.nombre_cs}")
                print(f"\nCirujano: {cirujano.nombre}")
            else:
                print(f"Trasplante fallido de {organo.tipo.capitalize()} en {self.nombre_cs}")
                # Cambiar prioridad del receptor y estado
                receptor.prioridad = 1  # Mayor prioridad
                receptor.estado = "INESTABLE"
                print(f"\nReceptor {receptor.nombre} cambiado a estado INESTABLE con prioridad máxima")
            return exito
            
        except Exception as e:
            print(f"❌ Error durante el trasplante: {e}")
            return False
    
    def __str__(self):
        return f"{self.nombre_cs} - {self.ciudad}, {self.provincia}, Argentina"

    def __len__(self):
        return len(self.cirujanos) + len(self.vehiculos)

    def __eq__(self, otro):
        """
        Compara dos centros de salud por nombre y dirección.
        
        Args:
            other (Centro_de_salud): Otro centro a comparar
            
        Returns:
            bool: True si son el mismo centro
        """
        if not isinstance(otro, Centro_de_salud):
            return False
        return (self.nombre_cs == otro.nombre_cs and 
                self.direccion == otro.direccion)
