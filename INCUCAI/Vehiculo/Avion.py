from Vehiculo.Vehiculo import Vehiculo

class Avion(Vehiculo):
    def calculo_tiempo(self, dist, trafico):
        return dist / self.velocidad