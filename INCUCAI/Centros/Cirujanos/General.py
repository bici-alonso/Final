import random
from INCUCAI.Centros.Cirujanos.Cirujano import *
from INCUCAI.Organos.Organo import Organo


class General (Cirujano):
    def __init__(self, nombre, centro):
        super().__init__(nombre, centro)

    def exito_operacion(self, organo):
        self.dar_operacion()
        resultado = random.randint(1, 10) > 5
        return resultado
    
    def __str__(self):
        return f"Cirujano general {self.nombre}"