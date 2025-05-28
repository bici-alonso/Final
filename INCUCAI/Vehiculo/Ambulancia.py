from Vehiculo.Vehiculo import Vehiculo

class Ambulancia(Vehiculo):
    
    def calculo_tiempo(self, dist, trafico=None):
        if dist < 0:
            raise ValueError("La distancia no puede ser negativa")
        if trafico is None:
            trafico = self.nivel_trafico()
        if trafico < 0:
            raise ValueError("El tráfico no puede ser negativo")
        
        tiempo_basico = dist / self.velocidad
        tiempo_total = tiempo_basico + trafico
        
        self.agregar_viaje(dist, tiempo_total, trafico)
        
        return tiempo_total
    
    