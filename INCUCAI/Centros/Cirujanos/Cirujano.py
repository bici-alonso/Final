''' Los cirujanos pueden ser generales o tener especialidades. 
Si la operación la realiza un cirujano general entonces el exito de la operación depende de un valor aleatorio entre 1 y 10,
si sale mas de 5 la operación es exitosa, 5 o menos falla. 
Si en cambio tiene especialidades depende del organo a operar. 
Si el organo influye en su especialidad entonces en el valor de entre 1 y 10, basta con que sea un 3 o mayor. 
Los cirujanos solo pueden hacer una operación al día, por lo que, si ya fueron asignados a una operación antes, 
no pueden ser asignados a una nueva.

Las especialidades que hay son:
    Cirujano cardiovascular: Tiene especialidad si la operación es de corazón.
    Cirujano pulmonar: Tiene especialidad si la operación es de pulmones.
    Cirujano plastico: Tiene especialidad si la operación es de piel y córneas. 
    Cirujano traumatologo: Tiene especialidad si la operación es de huesos.
    Cirujano gastroenterologo: Tiene especialidad si la operación es de intestinos, riñón, hígado y páncreas.
'''

from abc import ABC, abstractmethod
from datetime import date, datetime


class Cirujano(ABC):
    '''
    Clase abstracta que representa un cirujano dentro del sistema de trasplantes. Esta clase debe ser heredada por clases concretas
    como `General` o `Especialista`.
    '''


    def __init__(self, nombre, centro):
        '''
        Inicializa un cirujano con nombre y centro de salud.

        Args:
            nombre (str): Nombre del cirujano.
            centro (CentroSalud): Objeto que representa el centro de salud donde trabaja.
        '''
        self.nombre=nombre
        self.centro = centro
        self.operaciones_del_dia=[]
        self.ult_operacion= None #date
    
    def cirujano_disponible(self) -> bool: 
        '''
        Verifica si el cirujano está disponible para operar en el día actual.

        Returns:
            bool: True si el cirujano no operó aún hoy. False si ya realizó una operación hoy.
        '''
        hoy=date.today()
        return self.ult_operacion != hoy
    
    def dar_operacion (self):
        '''
        Registra que el cirujano realiza una operación en el momento actual.

        Raises:
            Exception: Si el cirujano ya realizó una operación hoy y no está disponible.
        '''
        if not self.cirujano_disponible():
            raise Exception (f"\nCirujano/a {self.nombre} no disponible")
        self.ult_operacion=date.today()
        self.operaciones_del_dia.append(datetime.now())
        print(f"{self.nombre} asignado a operación")
            
    def __len__(self):
        '''
        Retorna la cantidad total de operaciones registradas por el cirujano.

        Returns:
            int: Número de operaciones registradas.
        '''
        return len(self.operaciones_del_dia)
    
    @abstractmethod
    def exito_operacion(self, organo):
        '''
        Método abstracto que debe ser implementado por las subclases para determinar
        el resultado de una operación de trasplante.

        Args:
            organo (str): Nombre del órgano sobre el que se realiza la operación.

        Returns:
            bool: Resultado de la operación (True si fue exitosa, False si no).
        '''
        pass 