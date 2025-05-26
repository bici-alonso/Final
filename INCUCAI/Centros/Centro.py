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
            raise ValueError("Uno o ambos centros no tienen coordenadas geográficas.")
        return geodesic(self.coords, otro_centro.coords).kilometers
    
    
    def agregar_cirujano(self, cirujano):
        if cirujano not in self.cirujanos:
            self.cirujanos.append(cirujano)
            
    def agregar_vehiculo(self, vehiculo):
        if vehiculo not in self.vehiculos:
            self.vehiculos.append(vehiculo)
            
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
    
    def realizar_ablacion(self, organo, donante):
        """
        Realiza la ablación de un órgano.
            organo (Organo): Órgano 
            donante: Paciente donante
            
            retorna bool: True si la ablación fue exitosa
        """
        from datetime import datetime
        
        try:
            # Setear fecha y hora de ablación usando el método de la clase Organo
            ahora = datetime.now()
            organo.set_ablacion_auto(ahora.date(), ahora.time())
            
            # Quitar órgano de la lista del donante
            if organo in donante.organos_a_donar:
                donante.organos_a_donar.remove(organo)
                print(f"✅ Ablación exitosa de {organo.tipo.capitalize()} en {self.nombre_cs}")
                print(f"⏰ Tiempo máximo de conservación: {organo.get_tiempo_conservacion()} horas")
                return True
            
            print(f"❌ Error: el órgano no está en la lista del donante")
            return False
            
        except Exception as e:
            print(f"❌ Error durante la ablación: {e}")
            return False

    def realizar_trasplante(self, organo, receptor, cirujano):
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
            print(f"❌ Órgano no viable - han pasado {tiempo_transcurrido:.1f} horas desde la ablación")
            print(f"⏰ Tiempo máximo permitido: {organo.get_tiempo_conservacion()} horas")
            return False
        
        #info del organo antes del trasplante
        tiempo_restante = organo.calcular_tiempo_restante()
        print(f"\nTiempo restante para trasplante: {tiempo_restante:.1f} horas")
        
        # Realizar trasplante usando el cirujano
        try:
            exito = cirujano.realizar_operacion(organo.tipo)
            
            if exito:
                print(f"✅ Trasplante exitoso de {organo.tipo.capitalize()} en {self.nombre_cs}")
                print(f"\nCirujano: {cirujano.nombre}")
            else:
                print(f"❌ Trasplante fallido de {organo.tipo.capitalize()} en {self.nombre_cs}")
                # Cambiar prioridad del receptor y estado
                receptor.prioridad = 1  # Mayor prioridad
                receptor.estado = "Inestable"
                print(f"\nReceptor {receptor.nombre} cambiado a estado INESTABLE con prioridad máxima")
            
            return exito
            
        except Exception as e:
            print(f"❌ Error durante el trasplante: {e}")
            return False
    
    def __str__(self):
        """ Descripción del centro
        """
        return f"{self.nombre_cs} - {self.ciudad}, {self.provincia}"

    def __len__(self):
        """
        Retorna el número total de recursos (cirujanos + vehículos).
        
        Returns:
            int: Cantidad total de recursos
        """
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


def main():
    geolocator = Nominatim(user_agent="incucai_test")

    cs1 = Centro_de_salud("Hospital Garrahan", "Pichincha 1890", "Comuna 1", "Ciudad Autónoma de Buenos Aires", "011-12345678")
    cs2 = Centro_de_salud("Hospital El Cruce", "Av. Calchaquí 5401", "Florencio Varela", "Buenos Aires", "011-98765432")
    cs3 = Centro_de_salud("Fundacion Favaloro", "Av. Belgrano 1746", "C1093", "Ciudad Autónoma de Buenos Aires", "011-4378-1200")
    cs4 = Centro_de_salud("Hospital General de Niños Dr. R. Gutierrez", "Gallo 1330", "C1425EFD", "Ciudad Autónoma de Buenos Aires", "011 4962-9247")
    cs5 = Centro_de_salud("Hospital Italiano de La Plata", "Av. 51, B1900 La Plata", "La Plata", "Provincia de Buenos Aires", "022-15129500")
    cs6 = Centro_de_salud("Hospital Universitario Austral", "Mariano Acosta 1611", "Pilar", "Buenos Aires", "023-04388888")
    cs9 = Centro_de_salud("Hospital Gral. de Agudos Carlos G. Durand", "Av. Diaz Velez 5044", "Caballito", "Ciudad Autónoma de Buenos Aires", "011 4982-5555")
    cs10 = Centro_de_salud("Sanatorio Pasteur", "Chacabuco 675", "San Fernando del Valle de Catamarca", "Catamarca", "038 3443-2000")
    cs12= Centro_de_salud ("Hospital Zonal Alvear", "Juan Ramón Balcarce, Comodoro Rivadavia, Chubut", "Comodoro Rivadavia", "Chubut", "029 7455-9952")
    cs13= Centro_de_salud ("Hospital de Urgencias", "Catamarca 441, X5000 Córdoba", "Barrio Centro" , "Córdoba", "0351 427-6200")
    cs19= Centro_de_salud ("Hospital El Carmen", "Godoy Cruz 5504", "Godoy Cruz", "Mendoza", "081 0810-1033" ) 
    cs20= Centro_de_salud ("Hospital Samic Alem de autogestión nivel II", "Misiónes, N3315 Leandro N. Alem", "Misiones", "Misiones", "037 6415-6950") 
    cs22 = Centro_de_salud ("Hospital Area Programa Cipoletti Dr. Pedro Moguillansky", "Naciones Unidas 1450", "Cipolletti", "Río Negro" , "0299 4775-469")#rio negro
    cs23 = Centro_de_salud ("Hospital Papa Francisco", "C. 120 S/N, A4400 Salta", "Salta", "Salta", "0387 438-5022" )
    cs24 = Centro_de_salud ("Hospital Dr. Guillermo Rawson", "Av. Guillermo Rawson Sur 494", "J5400 San Juan", "San Juan", "026 4422-4005")
    cs25 = Centro_de_salud ("Hospital Dr. Clemente Alvarez", "Av. Pellegrini 3205", "Rosario Centro", "Santa Fe", "034 1480-8111") #santa fe
    #cs26 = Centro_de_salud ("Hospital Regional Dr. Ramon Carrillo", "", "", "", ""  )
    cs27 = Centro_de_salud ("Hospital Regional Rio Grande", "Florentino Ameghino 709", "Rio Grande", "Tierra del Fuego", "029 6442-2042")#tierra del fuego
    cs28 = Centro_de_salud ("Clinica Mayo SRL", "9 de Julio 279", "San Miguel de Tucumán", "Tucuman", "038 1450-2600") #tucuman
    

    #Lista de centros habilitados por el INCUCAI:
    centros = [cs1, cs2, cs3, cs4, cs5, cs6, cs9, cs10, cs12, cs13, cs19, cs20, cs22, cs23, cs24, cs25, cs27, cs28] #cs7, cs8, cs11, cs14, cs15, cs16, cs17, cs18, cs21, cs25, cs26, cs27, cs28] 

    for centro in centros:
        print(f"\n📍 {centro.nombre_cs}")
        print(f"Dirección completa: {centro.direccion_completa()}")
        location = centro.geolocalizar_direccion(geolocator)
        if location:
            print(f"🔢 Coordenadas: ({location.latitude}, {location.longitude})")
        else:
            print("⚠️ No se pudo obtener coordenadas.")
        time.sleep(1)

    
    try:
        distancia_km = cs1.calcular_distancia_a(cs2)
        print(f"\n Distancia entre {cs1.nombre_cs} y {cs2.nombre_cs}: {distancia_km:.2f} km")
    except ValueError as e:
        print(f"⚠️ Error al calcular distancia: {e}")

def nombrar_centros(centros):
    return [centro.nombre_cs for centro in centros]


if __name__ == "__main__":
    main()