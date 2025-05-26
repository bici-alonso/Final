import random
from Cirujanos.Cirujano import *

class General (Cirujano):
    def exito_operacion(self):
        self.dar_operacion()
        resultado = random.randint(1, 10)
        return resultado