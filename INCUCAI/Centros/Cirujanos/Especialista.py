import random
from INCUCAI.Centros.Cirujanos.Cirujano import *
from INCUCAI.Organos.Organo import *

class Especialista (Cirujano):
    def __init__(self, nombre, centro, especialidad):
        super().__init__(nombre, centro)
        self.especialidad=especialidad.lower()
        self.organos={
            "cardiovascular": ["corazon"],
            "gastroenterologo": ["intestino", "higado", "pancreas", "riñon", "rinion", "rinon"],
            "plastico": ["corneas", "piel"],
            "traumatologo": ["huesos"],
            "pulmonar": ["pulmones"]
        }
        
    def exito_operacion(self, organo):
        self.dar_operacion()
        tipo = organo.tipo.lower() if isinstance(organo, Organo) else organo.lower()
        #organo = organo.lower()
        resultado = random.randint(1, 10)
        
        if tipo in self.organos.get(self.especialidad, []):
            return resultado >= 3
        else:
            return resultado > 5
    
    def tiene_especialidad_para(self, organo):
        """
        Verifica si el cirujano tiene especialidad para un órgano específico.
        
        Args:
            organo: Órgano a verificar (objeto Organo o string)
            
        Returns:
            bool: True si tiene especialidad para este órgano
        """
        tipo = organo.tipo.lower() if isinstance(organo, Organo) else organo.lower()
        return tipo in self.organos.get(self.especialidad, [])
    
    
    def __str__(self):
        return f"Cirujano especialista {self.nombre} ({self.especialidad.capitalize()})"