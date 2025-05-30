from INCUCAI.Vehiculo.Vehiculo import Vehiculo

class Avion(Vehiculo):
    def __init__(self, velocidad, patente, centro_vehiculo):
        super().__init__(velocidad, patente, centro_vehiculo)
        
    def calculo_tiempo(self, dist, trafico=None):
        if dist < 0:
            raise ValueError("La distancia no puede ser negativa")
        
        tiempo=dist/self.velocidad
        self.agregar_viaje(dist, tiempo, trafico=0)
        return tiempo
    
    
    
    
    
