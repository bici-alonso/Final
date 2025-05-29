from INCUCAI.Vehiculo.Vehiculo import Vehiculo

class Helicoptero(Vehiculo):
    def calculo_tiempo(self, dist, trafico=None):
        if dist < 0:
            raise ValueError("La distancia no puede ser negativa")

        tiempo=dist/self.velocidad
        self.agregar_viaje(dist, tiempo, trafico=0)
        return tiempo
    