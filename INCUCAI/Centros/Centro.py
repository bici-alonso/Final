'''Acerca de los centros de salud estos tienen los siguientes datos: Nombre, Dirección, Partido, Provincia,
Teléfono, una lista de cirujanos y una lista de vehículos. Los centros de salud asignan un vehiculo para el
transporte del órgano. Esta selección de vehículos se realiza en base a la distancia. Si se encuentra en la
misma provincia y partido, se debe hacer uso del vehiculo disponible de mayor velocidad pero que no se use
para distancias mayores. Si se encuentra en la misma provincia, pero en un partido distinto, se utiliza el
helicóptero. Si discierne la provincia se utiliza el avión.

Una vez que el INCUCAI encontró un match, inicia el protocolo de transporte y trasplante. Este le pide al
centro de salud del donante que asigne un vehículo y un cirujano. Una vez que se asignó el vehículo, el centro
procede a realizar la ablación del órgano que necesita el receptor. En la ablación se setea la fecha y horario de
ablación del órgano y se quita el órgano removido de la lista de órganos del paciente donante. Ese vehículo
realiza el transporte (el cual demora un tiempo dependiendo de la distancia). Finalmente, el centro de salud
del receptor realiza el trasplante. Para realizar el trasplante se verifica que no hayan transcurrido más de 20
horas desde la ablación del órgano y procede a realizar el trasplante con el cirujano elegido. Si el trasplante es
exitoso, se remueve al paciente receptor de la lista de pacientes receptores. Si el trasplante falla, se cambia la
prioridad del paciente receptor a la de mayor prioridad y se setea su estado a inestable. Si el trasplante es
exitoso o no se define con un valor aleatorio que varia dependiendo de la especialidad del cirujano.
'''

'''
from geopy.geocoders import Nominatim
'''


from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import time


class Centro_de_salud():


    def __init__(self, nombre_cs, pais, direccion, partido, provincia, tel_contacto):
        self.pais = "Argentina"
        self.nombre_cs = nombre_cs
        self.direccion = direccion
        self.partido = partido
        self.provincia = provincia
        self.tel_contacto = tel_contacto
        self.cirujanos = []
        self.vehiculos = []
        self.coords = None
        
        #la carga de datos de a direccion debe hacerse como str separada o toda junta para el geopy?
        #tengo una lista de centros habilitados?
        
    def direccion_completa(self):
        return f"{self.direccion}, {self.partido}, {self.provincia}, Argentina"
        
#El incucai tiene centros de salud HABILITADOS PARA TRANSPLANTE, CREO UNA LISTA EN INCUCAI DEL TIPO CENTRO DE SALUD CON CIERTOS CENTROS CARGADOS

def main():
    # Crear geolocalizador
    geolocator = Nominatim(user_agent="incucai_test")
    
    # Crear centros de salud
    cs1 = Centro_de_salud("Hospital Garrahan", "Argentina", "Pichincha 1890", "Comuna 1", "Ciudad Autónoma de Buenos Aires", "011-12345678")
    cs2 = Centro_de_salud("Hospital El Cruce", "Argentina", "Av. Calchaquí 5401", "Florencio Varela", "Buenos Aires", "011-98765432")
    cs3 = Centro_de_salud("Fundacion Favaloro", "Argentina", "Av. Belgrano 1746", "Comuna 2", "Ciudad Autónoma de Buenos Aires", "011-4378-1200")
    cs4 = Centro_de_salud("Hospital General de Niños Dr. R. Gutierrez", "Argentina", "Gallo 1330", "Comuna 10", "Ciudad Autónoma de Buenos Aires", "011 4962-9247")
    cs5 = Centro_de_salud("Hospital Italiano de La Plata", "Argentina", "Av. 51", "Gambier", "Buenos Aires", "022-15129500")
    cs6 = Centro_de_salud("Hospital Universitario Austral", "Argentina", "Mariano Acosta 1611", "Pilar", "Buenos Aires", "023-04388888")
    cs7 = Centro_de_salud("CETRAMOR", "Argentina", "Rioja 1529", "Barrio Centro", "Rosario", "Santa Fe", "0341-4488962")
    cs8 = Centro_de_salud("Hospital Alejandro Posadas", "Argentina", "Av. Presidente Arturo U. Ilia 386", "El Palomar", "Moron", "Buenos Aires", "01144699300")
    cs9 = Centro_de_salud("Hospital Gral. de Agudos Carlos G. Durand", "Argentina", "Av. Diaz Velez 5044", "Caballito", "Ciudad Autónoma de Buenos Aires", "01149825555")
    cs10 = Centro_de_salud("Sanatorio Pasteur", "Argentina", "Chacabuco 675", "El Jumeal", "San Fernando del Valle de Catamarca", "Catamarca", "03834432000")
    cs11 = Centro_de_salud("Hospital Dr. Julio Cecilio Perrando", "Argentina", "Av. 9 de Julio 1110", "Don Rafael", "Resistencia", "Chaco", "03624427233")

    # Lista de centros
    centros = [cs1, cs2, cs3, cs4, cs5, cs6, cs7, cs8, cs9, cs10, cs11]

    for centro in centros:
        print(f"\n📍 {centro.nombre_cs}")
        direccion = centro.direccion_completa()
        print(f"Dirección completa: {direccion}")
        location = geolocator.geocode(direccion)
        if location:
            print(f"🔢 Coordenadas: ({location.latitude}, {location.longitude})")
            centro.coords = (location.latitude, location.longitude)
        else:
            print("❌ No se pudo geolocalizar.")
        time.sleep(1)  # Para evitar bloqueo de Nominatim

    # Calcular distancia entre los dos centros si ambos fueron geolocalizados
    if hasattr(cs1, 'coords') and hasattr(cs2, 'coords'):
        distancia_km = geodesic(cs1.coords, cs2.coords).kilometers
        print(f"\n📏 Distancia entre {cs1.nombre_cs} y {cs2.nombre_cs}: {distancia_km:.2f} km")

if __name__ == "__main__":
    main()





''' terminar esta carga de datos que va en incucai
cs12= Centro_de_salud ("Hospital Alvear Comodoro Rivadavia", "Juan Ramon Balcarce", "Barrio 25 de mayo", "Comodor Rivadavia", "Chubut")
cs13= Centro_de_salud ("Hospital de Urgencias") #cordoba
cs14= Centro_de_salud ("Hospital Privado de Cordoba")#cordoba
cs15= Centro_de_salud ("Hospital Gral. San Martin") #corrientes
cs16= Centro_de_salud ("Hospital Justo Jose de Urquiza") #entre rios
cs17= Centro_de_salud ("Central de Formosa")#formosa
cs18= Centro_de_salud ("Hospital Central de Mendoza")#mendoza
cs19= Centro_de_salud ("Hospital El Carmen") #mendoz
cs20= Centro_de_salud ("Autogestion SAMIC El Dorado")#misiones
cs21 = Centro_de_salud ("Castro Rendon")
cs22 = Centro_de_salud ("Hospital Area Programa Cipoletti Dr. Pedro Moguillansky")#rio negro
cs23 = Centro_de_salud ("Hospital Papa Francisco")#salta
cs24 = Centro_de_salud ("Hospital Dr. Guillermo Rawson")#san juan
cs25 = Centro_de_salud ("Hospital Dr. Clemente Alvarez")#santa fe
cs26 = Centro_de_salud ("Hospital del Centenario")
cs27 = Centro_de_salud ("Hospital Regional Dr. Ramon Carrillo" )
cs28 = Centro_de_salud ("Rospital Rio Grande")#tierra del fuego
cs29 = Centro_de_salud ("Clinica Mayo SRL") #tucuman
'''

