'''
Los cirujanos pueden ser generales o tener especialidades. Si la operación la realiza un cirujano general
entonces el exito de la operación depende de un valor aleatorio entre 1 y 10, si sale mas de 5 la operación es
exitosa, 5 o menos falla. Si en cambio tiene especialidades depende del organo a operar. Si el organo influye
en su especialidad entonces en el valor de entre 1 y 10, basta con que sea un 3 o mayor. Los cirujanos solo
pueden hacer una operación al día, por lo que, si ya fueron asignados a una operación antes, no pueden ser
asignados a una nueva.

Las especialidades que hay son:
    Cirujano cardiovascular: Tiene especialidad si la operación es de corazón.
    Cirujano pulmonar: Tiene especialidad si la operación es de pulmones.
    Cirujano plastico: Tiene especialidad si la operación es de piel y córneas. 
    Cirujano traumatologo: Tiene especialidad si la operación es de huesos.
    Cirujano gastroenterologo: Tiene especialidad si la operación es de intestinos, riñón, hígado y páncreas.
'''

from abc import ABC, abstractmethod
from datetime import date, datetime

import random

class Cirujano(ABC):
    def __init__(self, nombre):
        self.nombre=nombre
        self.operaciones_del_dia=[]
        self.ult_operacion= None #date
    
    def cirujano_disponible(self) -> bool: 
        hoy=date.today()
        return self.ult_operacion != hoy
    
    def dar_operacion (self):
        if not self.cirujano_disponible():
            raise Exception (f"\nCirujano/a {self.nombre} no disponible para otra operacion en el dia.")
        self.ult_operacion=date.today()
        self.operaciones_del_dia.append(datetime.now())
