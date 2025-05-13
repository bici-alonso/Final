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
        self.pais = "Argentina"
        self.nombre_cs = nombre_cs
        self.direccion = direccion
        self.ciudad = barrio
        self.provincia = provincia
        self.tel_contacto = tel_contacto
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

def main():
    geolocator = Nominatim(user_agent="incucai_test")

    cs1 = Centro_de_salud("Hospital Garrahan", "Pichincha 1890", "Comuna 1", "Ciudad Autónoma de Buenos Aires", "011-12345678")
    cs2 = Centro_de_salud("Hospital El Cruce", "Av. Calchaquí 5401", "Florencio Varela", "Buenos Aires", "011-98765432")
    cs3 = Centro_de_salud("Fundacion Favaloro", "Av. Belgrano 1746", "Comuna 2", "Ciudad Autónoma de Buenos Aires", "011-4378-1200")
    cs4 = Centro_de_salud("Hospital General de Niños Dr. R. Gutierrez", "Gallo 1330", "Comuna 10", "Ciudad Autónoma de Buenos Aires", "011 4962-9247")
    cs5 = Centro_de_salud("Hospital Italiano de La Plata", "Av. 51", "Gambier", "Buenos Aires", "022-15129500")
    cs6 = Centro_de_salud("Hospital Universitario Austral", "Mariano Acosta 1611", "Pilar", "Buenos Aires", "023-04388888")
    cs7 = Centro_de_salud("CETRAMOR", "Rioja 1529", "Barrio Centro", "Rosario, Santa Fe", "0341-4488962")
    cs8 = Centro_de_salud("Hospital Alejandro Posadas", "Av. Presidente Arturo U. Ilia 386", "El Palomar", "Buenos Aires", "011 4469-9300")
    cs9 = Centro_de_salud("Hospital Gral. de Agudos Carlos G. Durand", "Av. Diaz Velez 5044", "Caballito", "Ciudad Autónoma de Buenos Aires", "011 4982-5555")
    cs10 = Centro_de_salud("Sanatorio Pasteur", "Chacabuco 675", "San Fernando del Valle de Catamarca", "Catamarca", "038 3443-2000")
    cs11 = Centro_de_salud("Hospital Dr. Julio Cecilio Perrando", "Av. 9 de Julio 1110", "Don Rafael, Resistencia", "Chaco", "036 2442-7233")
    cs12= Centro_de_salud ("Hospital Alvear Comodoro Rivadavia", "Juan Ramon Balcarce", "Barrio 25 de mayo, Comodoro Rivadavia", "Chubut", "029 7455-9952")
    cs13= Centro_de_salud ("Hospital de Urgencias", "Catamarca 441", "Barrio Centro, Cordoba Capital" , "Cordoba", "0351 427-6200")
    cs14= Centro_de_salud ("Hospital Privado de Cordoba", "Naciones Unidas 346","Colinas de Velez Sarfield, Cordoba Capital","Cordoba","0351 468-8200")
    cs15= Centro_de_salud ("Hospital Gral. San Martin", "Av. 3 de Abril 1224", "Barrio Centro, Ciudad de Corrientes", "Corrientes", "---") 
    cs16= Centro_de_salud ("Hospital Justo Jose de Urquiza", "Av. Hipólito Irigoyen 3180", "Barrio Centro", "Entre Ríos", "034 5442-1791" ) 
    cs17= Centro_de_salud ("Central de Formosa", "Padre Patino 1163", "San Pio X, Formosa", "Formosa", "037 0442-6194")
    cs18= Centro_de_salud ("Hospital Central de Mendoza", "L.N. Alem 5502", "Barrio Santa Maria", "Mendoza", "026 1385-5509")
    cs19= Centro_de_salud ("Hospital El Carmen", "Godoy Cruz 5504", "Godoy Cruz", "Mendoza", "081 0810-1033" ) #mendoza
    cs20= Centro_de_salud ("Autogestion SAMIC El Dorado", "Junin 3380", "El Dorado", "Misiones", "037 6415-6950")#misiones
    cs21 = Centro_de_salud ("Castro Rendon", "Buenos Aires 450", "Barrio Central", "Neuquen", "0299 4490-800")
    cs22 = Centro_de_salud ("Hospital Area Programa Cipoletti Dr. Pedro Moguillansky", "Naciones Unidas 1450", "Cipolletti", "Río Negro" , "0299 4775-469")#rio negro
    cs23 = Centro_de_salud ("Hospital Papa Francisco", "Calle 120", "Juan Manuelde Rosas", "Salta", "0387 438-5022" )#salta
    cs24 = Centro_de_salud ("Hospital Dr. Guillermo Rawson", "Av. Guillermo Rawson Sur 494", "Barrio Autopista", "San Juan", "026 4422-4005")#san juan
    cs25 = Centro_de_salud ("Hospital Dr. Clemente Alvarez", "Av. Pellegrini 3205", "Rosario Centro", "Santa Fe", "034 1480-8111") #santa fe
    cs26 = Centro_de_salud ("Hospital Regional Dr. Ramon Carrillo", "", "", "", ""  )
    cs27 = Centro_de_salud ("Hospital Regional Rio Grande", "Florentino Ameghino 709", "Rio Grande", "Tierra del Fuego", "029 6442-2042")#tierra del fuego
    cs28 = Centro_de_salud ("Clinica Mayo SRL", "9 de Julio 279", "San Miguel de Tucumán", "Tucuman", "038 1450-2600") #tucuman
    

    #Lista de centros habilitados por el INCUCAI:
    centros = [cs1, cs2, cs3, cs4, cs5, cs6, cs7, cs8, cs9, cs10, cs11, cs12, cs13, cs14, cs15, cs16, cs17, cs18, cs19, cs20, cs21, cs22, cs23, cs24, cs25, cs26, cs27, cs28] 

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
        print(f"\n📏 Distancia entre {cs1.nombre_cs} y {cs2.nombre_cs}: {distancia_km:.2f} km")
    except ValueError as e:
        print(f"⚠️ Error al calcular distancia: {e}")

if __name__ == "__main__":
    main()