class Ambulancia(Vehiculo):
    def calculo_tiempo(self, dist, trafico):
        return dist / self.velocidad + trafico