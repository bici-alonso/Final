import random
from Cirujanos.Cirujano import *
from Organos.Organo import Organo


class General (Cirujano):

    def exito_operacion(self, organo):
        self.dar_operacion()
        resultado = random.randint(1, 10) > 5
        return resultado
    
    def __str__(self):
        return f"Cirujano general {self.nombre}"