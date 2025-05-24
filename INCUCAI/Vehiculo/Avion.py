from Vehiculo.Vehiculo import Vehiculo

class Avion(Vehiculo):
    def calculo_tiempo(self, dist):
        if dist < 0:
            raise ValueError("La distancia no puede ser negativa")
        return dist / self.velocidad
    
    
    
    
    
