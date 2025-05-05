'''Considerar distancia de centro de salud mas cercano

Los centros de salud asignan un vehiculo para el transporte del órgano. 
Esta selección de vehículos se realiza en base a la distancia. 
Si se encuentra en la misma provincia y partido, se debe hacer uso del vehiculo disponible de mayor velocidad pero que no se use
para distancias mayores. 
Si se encuentra en la misma provincia, pero en un partido distinto, se utiliza el helicóptero. 
Si discierne la provincia se utiliza el avión.
Una vez que el INCUCAI encontró un match, inicia el protocolo de transporte y trasplante. Este le pide al
centro de salud del donante que asigne un vehículo y un cirujano. Una vez que se asignó el vehículo, el centro
procede a realizar la ablación del órgano que necesita el receptor.
Ese vehículo realiza el transporte (el cual demora un tiempo dependiendo de la distancia). 
Finalmente, el centro de salud del receptor realiza el trasplante. 
Para realizar el trasplante se verifica que no hayan transcurrido más de 20 horas desde la ablación del órgano y procede a realizar el trasplante. 
'''


#Hago a vehiculo mi clase abstracta:

from abc import ABC, abstractmethod
from datetime import datetime




class Vehiculo(ABC):


    def __init__(self, velocidad, patente):
        self.velocidad = velocidad
        self.patente = patente
        self.viajes = []
        
    @abstractmethod
        def calculo_tiempo (self, dist, trafico):
            #????
            
    def agregar_viaje(self, dist, tiempo):
        self.viajes.append({
            'fecha': datetime.now(), # ??
            'distancia': dist,
            'tiempo estimado': tiempo
        })