'''
Los centros de salud asignan un vehiculo para el transporte del órgano. 
Esta selección de vehículos se realiza en base a la distancia. 
Si se encuentra en la misma provincia y partido, se debe hacer uso del vehiculo disponible de mayor velocidad pero que no se use
para distancias mayores. 
Si se encuentra en la misma provincia, pero en un partido distinto, se utiliza el
helicóptero.
Si discierne la provincia se utiliza el avión.
Una vez que el INCUCAI encontró un match, inicia el protocolo de transporte y trasplante. Este le pide al
centro de salud del donante que asigne un vehículo y un cirujano. Una vez que se asignó el vehículo, el centro
procede a realizar la ablación del órgano que necesita el receptor. 
Ese vehículo realiza el transporte (el cual demora un tiempo dependiendo de la distancia). 

Para realizar el trasplante se verifica que no hayan transcurrido más de 20 horas desde la ablación del órgano y procede a realizar el trasplante con el cirujano elegido. 


Los vehículos que realizan el transporte tienen una velocidad y un registro de viajes realizados. Cuando se
despacha el organo se les indica la distancia y el nivel de trafico. Ambos datos los obtiene el centro de salud
consultando un servicio de terceros (pueden utilizar valores inventados a su discreción dentro de main
cuando se envian estos mensajes). Los vehiculos tardan en recorrer un trayecto en una cantidad igual a su
velocidad dividido la distancia mas el nivel de trafico. Tantos los helicopteros como los aviones, al ser
vehiculos aereos no se ven afectados por el nivel de trafico, por lo que ignoran ese valor. 
Considerar distancia de centro de salud mas cercano

Los centros de salud asignan un vehiculo para el transporte del órgano. 
Esta selección de vehículos se realiza en base a la distancia. 
Si se encuentra en la misma provincia y partido, se debe hacer uso del vehiculo disponible de mayor velocidad pero que no se use
para distancias mayores. 
Si se encuentra en la misma provincia, pero en un partido distinto, se utiliza el helicóptero. 
Si discierne la provincia se utiliza el avión.
Una vez que el INCUCAI encontró un match, inicia el protocolo de transporte y trasplante. 
Este le pide al centro de salud del donante que asigne un vehículo y un cirujano. 
Una vez que se asignó el vehículo, el centro procede a realizar la ablación del órgano que necesita el receptor.
Ese vehículo realiza el transporte (el cual demora un tiempo dependiendo de la distancia). 
Finalmente, el centro de salud del receptor realiza el trasplante. 
Para realizar el trasplante se verifica que no hayan transcurrido más de 20 horas desde la ablación del órgano y procede a realizar el trasplante. 
'''

from abc import ABC, abstractmethod
from datetime import datetime
import random

#vehiculo es clase abstracta:
class Vehiculo(ABC):

    def __init__(self, velocidad, patente, centro_vehiculo):
        if velocidad <= 0:
            raise ValueError("La velocidad debe ser mayor a 0")
        if not patente or not patente.strip():
            raise ValueError("La patente no puede estar vacía")
            
        self.velocidad = velocidad
        self.patente = patente.strip().upper()
        self.viajes = []
        self.disponible=True
        self.centro_vehiculo = centro_vehiculo

    def nivel_trafico(self):
        return round(random.uniform(0.1, 2.0), 2)
        
        
    @abstractmethod
    def calculo_tiempo (self, dist, trafico=None):
        pass 
            
    def agregar_viaje(self, dist, tiempo, trafico=0):
        self.viajes.append({
            'fecha': datetime.now(), # ??
            'distancia': dist,
            'tiempo estimado': tiempo,
            'trafico': trafico
        })
    
    def historial_viajes(self):
        return self.viajes.copy()
        
    def __str__(self):
        #define cómo se representa un objeto de una clase como una cadena de texto.
        return f"{self.__class__.__name__} - Patente: {self.patente}, Velocidad: {self.velocidad} km/h"
    
    def __eq__(self, other):
        if not isinstance(other, Vehiculo):
            return False
        return self.patente == other.patente
    

