import random
from Cirujanos.Cirujano import *

class Especialista (Cirujano):
    def __init__(self, nombre, especialidad):
        super().__init__(nombre)
        self.especialidad=especialidad.lower()
        self.organos={
            "cardiovascular": ["corazon"],
            "gastroenterologo": ["intestino", "higado", "pancreas", "riñon"],
            "plastico": ["corneas", "piel"],
            "traumatologo": ["huesos"],
            "pulmonar": ["pulmones"]
        }
        
    def exito_operacion(self):
        self.dar_operacion(self, organo)
        organo = organo.lower()
        resultado = random.randint(1, 10)
        if organo in self.organos_especialidad.get(self.especialidad, []):
            return resultado >= 3
        else:
            return resultado > 5