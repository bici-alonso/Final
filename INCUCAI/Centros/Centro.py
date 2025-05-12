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


from geopy.geocoders import Nominatim

class Centro_de_salud():


    def __init__(self, nombre_cs, pais, direccion, partido, provincia, tel_contacto):
        self.pais = Argentina
        self.nombre_cs = nombre_cs
        self.direccion = direccion
        self.partido = partido
        self.provincia = provincia
        self.tel_contacto = tel_contacto
        self.cirujanos = []
        self.vehiculos = []
        
        #la carga de datos de a direccion debe hacerse como str separada o toda junta para el geopy?
        #tengo una lista de centros habilitados?
        
    def direccion_completa(self):
        return f"{self.direccion}, {self.partido}, {self.provincia}, Argentina"
        
#El incucai tiene centros de salud HABILITADOS PARA TRANSPLANTE, CREO UNA LISTA EN INCUCAI DEL TIPO CENTRO DE SALUD CON CIERTOS CENTROS CARGADOS

cs1 = Centro_de_salud("Hospital Garrahan", "Pichincha 1890", "Comuna 1", "Ciudad Autónoma de Buenos Aires", "011-12345678")
cs2 = Centro_de_salud("Hospital El Cruce", "Av. Calchaquí 5401", "Florencio Varela", "Buenos Aires", "011-98765432")

