import random
from Cirujanos.Cirujano import *
from Organos.Organo import *

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
        
    def exito_operacion(self, organo):
        self.dar_operacion()
        tipo = organo.tipo.lower() if isinstance(organo, Organo) else organo.lower()
        #organo = organo.lower()
        resultado = random.randint(1, 10)
        
        if tipo in self.organos_especialidad.get(self.especialidad, []):
            return resultado >= 3
        else:
            return resultado > 5
    
    def __str__(self):
        return f"Cirujano especialista {self.nombre} ({self.especialidad.capitalize()})"