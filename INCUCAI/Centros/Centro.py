from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from geopy.exc import GeocoderTimedOut
import time
from datetime import datetime

from INCUCAI.Centros.Cirujanos.Especialista import Especialista
from INCUCAI.Centros.Cirujanos.General import General 
from INCUCAI.Vehiculo.Ambulancia import Ambulancia
from INCUCAI.Vehiculo.Avion import Avion
from INCUCAI.Vehiculo.Helicoptero import Helicoptero
from INCUCAI.Organos.Organo import Organo



class Centro_de_salud:

    def __init__(self, nombre_cs, direccion, barrio, provincia, tel_contacto) -> None:
        '''
        Inicializa un centro de salud con su informacion principal

        Args:
            - nombre_cs (str): Nombre del centro.
            - direccion (str): Dirección del centro.
            - barrio (str): Barrio/ciudad del centro.
            - provincia (str): Provincia donde se ubica.
            - tel_contacto (str): Teléfono de contacto.

        Return:
            - None
        '''
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

    def direccion_completa(self) -> str:
        '''
        Devuelve la dirección completa del centro formateada.

        Return:
            - str: Dirección en formato "calle, ciudad, provincia, Argentina"
        '''
        return f"{self.direccion}, {self.ciudad}, {self.provincia}, {self.pais}"

    def geolocalizar_direccion(self, geolocator, intentos=3):
        '''
        Obtiene las coordenadas (latitud, longitud) de la dirección del centro usando un geolocalizador externo.

        Args:
            - geolocator: objeto de geolocalización (como Nominatim de geopy).
            - intentos (int): cantidad de intentos antes de abandonar si ocurre timeout.

        Retorna:
            - location: objeto con atributos .latitude y .longitude, o None si no se logró geolocalizar.
        '''
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

    def calcular_distancia_a(self, otro_centro) -> float:
        '''
        Calcula la distancia en kilómetros entre un centro y otro.

        Args:
            - otro_centro (Centro_de_salud): Otro centro con coordenadas.

        Return:
            - float: Distancia en kilómetros.
        '''
        if self.coords is None or otro_centro.coords is None:
            print("\nUno o ambos centros no tienen coordenadas geográficas.")
        return geodesic(self.coords, otro_centro.coords).kilometers  
    
    def agregar_cirujano(self, cirujano) -> None:
        '''
        Agrega un cirujano general o especialista a la lista general.

        Args:
            - cirujano (Cirujano): Objeto cirujano a agregar.

        Return:
            - None
        '''
        if cirujano not in self.cirujanos:
            self.cirujanos.append(cirujano)
    
    def agregar_cirujano_especialista(self, cirujano: Especialista) -> None:
        '''
        Agrega un cirujano especialista a la lista de especialistas.

        Atributos:
            - cirujano (Especialista): Objeto especialista.

        Return:
            - None
        '''
        if cirujano not in self.especialistas:
            self.especialistas.append(cirujano)
    
    def agregar_cirujano_general(self, cirujano: General) -> None:
        '''
        Agrega un cirujano general a la lista de general.

        Atributos:
            - cirujano (General): Objeto general.

        Return:
            - None
        '''
        if cirujano not in self.especialistas:
            self.generales.append(cirujano)
            
    def agregar_vehiculo(self, vehiculo) -> None:
        '''
        Agrega un vehículo a la lista general del centro.

        Atributos:
            - vehiculo (Vehiculo): Instancia de vehículo.

        Return:
            - None
        '''
        if vehiculo not in self.vehiculos:
            self.vehiculos.append(vehiculo)
    
    def agregar_ambulancia(self, vehiculo: Ambulancia) -> None:
        '''
        Agrega una ambulancia a la lista de ambulancias.

        Atributos:
            - vehiculo (Ambulancia): Vehículo tipo ambulancia.

        Return:
            - None
        '''
        if vehiculo not in self.ambulancias:
            self.ambulancias.append(vehiculo)  
        self.agregar_vehiculo(vehiculo)
            
    def agregar_avion(self, vehiculo: Avion) -> None:
        '''
        Agrega un avión a la lista de aviones.

        Atributos:
            - vehiculo (Avion): Vehículo tipo avión.

        Return:
            - None
        '''
        if vehiculo not in self.aviones:
            self.aviones.append(vehiculo)
        self.agregar_vehiculo(vehiculo)

    def agregar_helicoptero(self, vehiculo: Helicoptero) -> None:
        '''
        Agrega un helicóptero a la lista de helicópteros.

        Atributos:
            - vehiculo (Helicoptero): Vehículo tipo helicóptero.

        Return:
            - None
        '''
        if vehiculo not in self.helicopteros:
            self.helicopteros.append(vehiculo)
        self.agregar_vehiculo(vehiculo)

    def tiene_vehiculos_disponibles(self) -> bool:
        """
        Devuelve True si al menos un vehículo del centro está marcado como disponible.
        Si aún no manejás disponibilidad, simplemente comprueba que la lista no esté vacía.
        """
        return any(getattr(v, "disponible", True) for v in self.vehiculos)
            
    def seleccionar_vehiculo(self, centro_destino):
        '''
        Selecciona el mejor vehículo para transportar un órgano al centro destino,
        considerando ciudad/provincia.

        Args:
            - centro_destino (Centro_de_salud): Centro de destino.

        Return:
            - Vehiculo: Vehículo seleccionado.
        '''
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
    
    def seleccionar_cirujano(self, organo: Organo):
        '''
        Selecciona un cirujano disponible especializado en el órgano si es posible.

        Args:
            - organo (Organo): Órgano a trasplantar.

        Return:
            - Cirujano | None: Cirujano seleccionado o None si no hay disponible.
        '''
        disponibles = [c for c in self.cirujanos if c.cirujano_disponible()]
        for c in disponibles:
            if hasattr(c, 'especialidad') and organo.lower() in c.organos.get(c.especialidad, []):
                return c
        return disponibles[0] if disponibles else None
        
    def realizar_ablacion(self, organo, donante) -> bool:
        """
        Realiza la ablación de un órgano.

        Args:
            -organo (Organo): Órgano 
            -donante: Paciente donante
            
        Return:
            -bool: True si la ablación fue exitosa
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
            print(f"❌ Error durante la ablación: {e}")
            return False

    def realizar_transplante(self, organo, receptor, cirujano) -> bool:
        """
        Realiza el trasplante de un órgano.

        Args:
            -organo: a trasplantar
            -receptor: Paciente receptor
            -cirujano: Cirujano que realizará la operación
        Return:
            -bool: True si el trasplante fue exitoso
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
    
    def __str__(self) -> str:
        '''
        Devuelve una representación string del centro (nombre y ubicación).

        Return:
            - str: "Nombre - ciudad, provincia, Argentina"
        '''
        return f"{self.nombre_cs} - {self.ciudad}, {self.provincia}, Argentina"

    def __len__(self) -> int:
        '''
        Devuelve la cantidad total de cirujanos y vehículos en el centro.

        Return:
            - int: Total de elementos humanos y móviles.
        '''
        return len(self.cirujanos) + len(self.vehiculos)

    def __eq__(self, otro) -> bool:
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