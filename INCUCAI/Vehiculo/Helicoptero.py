from Vehiculo.Vehiculo import Vehiculo


class Helicoptero(Vehiculo):
    def calculo_tiempo(self, dist, trafico):
        return dist / self.velocidad