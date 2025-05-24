from Vehiculo.Vehiculo import Vehiculo

class Ambulancia(Vehiculo):
    
    def calculo_tiempo(self, dist, trafico):
        if dist < 0:
            raise ValueError("La distancia no puede ser negativa")
        if trafico < 0:
            raise ValueError("El tráfico no puede ser negativo")
        
        return dist / self.velocidad + trafico
    
    