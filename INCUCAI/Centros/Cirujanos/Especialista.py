import random
from INCUCAI.Centros.Cirujanos.Cirujano import *
from INCUCAI.Organos.Organo import *

class Especialista (Cirujano):
    '''
    Representa a un cirujano especialista dentro del sistema de trasplantes.
    Hereda de la clase abstracta `Cirujano` e incorpora una especialidad médica que afecta 
    la probabilidad de éxito en una operación según el órgano a tratar.
    '''
    def __init__(self, nombre, centro, especialidad):
        '''
        Inicializa un cirujano especialista con su nombre, centro de salud y especialidad.

        Args:
            nombre (str): Nombre del cirujano.
            centro (CentroSalud): Objeto que representa el centro donde trabaja.
            especialidad (str): Especialidad médica del cirujano.
        '''
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
        '''
        Determina si una operación realizada por el cirujano especialista es exitosa.
        La probabilidad de éxito depende de si el órgano está dentro de la especialidad del cirujano:
            - Si el órgano pertenece a su especialidad, éxito con probabilidad >= 80% (resultado ≥ 3).
            - Si no pertenece, éxito solo con probabilidad > 50% (resultado > 5).

        Args:
            organo (Organo o str): Órgano sobre el que se realiza la operación.

        Returns:
            bool: True si la operación fue exitosa, False en caso contrario.
        '''
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
        '''
        Representación textual del cirujano especialista.

        Returns:
            str: Descripción con nombre y especialidad.
        '''
        return f"Cirujano especialista {self.nombre} ({self.especialidad.capitalize()})"