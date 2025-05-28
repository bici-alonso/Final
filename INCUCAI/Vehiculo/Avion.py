from Vehiculo.Vehiculo import Vehiculo

class Avion(Vehiculo):
    def calculo_tiempo(self, dist):
        if dist < 0:
            raise ValueError("La distancia no puede ser negativa")
        
        tiempo=dist/self.velocidad
        self.agregar_viaje(dist, tiempo, trafico=0)
        return tiempo
    
    
    
    
    
