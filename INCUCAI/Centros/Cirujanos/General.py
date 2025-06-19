import random
from INCUCAI.Centros.Cirujanos.Cirujano import *



class General (Cirujano):
    '''
    Representa a un cirujano general dentro del sistema de trasplantes.
    Esta clase hereda de `Cirujano` y representa un profesional médico con capacidad para realizar operaciones generales
    dentro del protocolo de trasplantes.
    '''

    def __init__(self, nombre, centro) -> None:
        '''
        Inicializa un cirujano general con su nombre y centro de salud.

        Args:
            nombre (str): Nombre del cirujano.
            centro (CentroSalud): Objeto que representa el centro de salud donde trabaja.
        '''
        super().__init__(nombre, centro)

    def exito_operacion(self) -> bool:
        '''
        Simula el resultado de una operación quirúrgica sobre un órgano.
        La operación se considera exitosa con una probabilidad del 50% (número aleatorio entre 1 y 10 > 5).

        Returns:
            bool: True si la operación fue exitosa, False en caso contrario.
        '''
        self.dar_operacion()
        resultado = random.randint(1, 10) > 5
        return resultado
    
    def __str__(self) -> str:
        '''
        Representación en forma de cadena del cirujano general.

        Returns:
            str: Descripción textual del cirujano general, su nombre.
        '''
        return f"Cirujano general {self.nombre}"