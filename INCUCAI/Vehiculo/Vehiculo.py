from abc import ABC, abstractmethod
from datetime import datetime
import random



class Vehiculo(ABC):
    """
    Clase abstracta que representa un vehículo del sistema de transporte del INCUCAI.

    Esta clase modela los atributos y comportamientos comunes de todos los vehículos que participan
    en los traslados relacionados con donaciones y trasplantes (como ambulancias, helicópteros, aviones, etc.).

    Atributos:
    ----------
    velocidad : float
        Velocidad máxima del vehículo (en km/h). Debe ser mayor a 0.
    patente : str
        Identificador único del vehículo (no puede estar vacío).
    centro_vehiculo : Centro
        Centro médico o base al que pertenece el vehículo.
    viajes : list[dict]
        Lista de viajes realizados por el vehículo. Cada viaje contiene distancia, tiempo estimado, tráfico y fecha.
    disponible : bool
        Indica si el vehículo está disponible para un nuevo viaje (por defecto, True).

    Métodos:
    --------
    __init__(velocidad, patente, centro_vehiculo)
        Constructor que inicializa los atributos del vehículo. Valida velocidad y patente.
    nivel_trafico()
        Simula un nivel de tráfico aleatorio entre 0.1 y 2.0.
    calculo_tiempo(dist, trafico)
        Método abstracto que debe ser implementado por cada subclase. Calcula el tiempo estimado de viaje.
    agregar_viaje(dist, tiempo, trafico)
        Registra un viaje en el historial del vehículo.
    historial_viajes()
        Devuelve una copia de la lista de viajes realizados por el vehículo.
    __str__()
        Retorna una representación legible del vehículo (tipo, patente y velocidad).
    __eq__(other)
        Compara dos vehículos por su patente.

    Excepciones:
    ------------
    ValueError:
        - Si la velocidad es menor o igual a 0.
        - Si la patente es una cadena vacía o solo espacios.
    """
    
    def __init__(self, velocidad, patente, centro_vehiculo):
        """
        Inicializa un vehículo con su velocidad, patente y centro asignado.

        Args:
            velocidad (float): Velocidad en km/h. Debe ser > 0.
            patente (str): Identificador del vehículo.
            centro_vehiculo (Centro): Centro o base del vehículo.

        Raises:
            ValueError: Si la velocidad es <= 0 o la patente está vacía.
        """
        if velocidad <= 0:
            raise ValueError("La velocidad debe ser mayor a 0")
        if not patente or not patente.strip():
            raise ValueError("La patente no puede estar vacía")
            
        self.velocidad = velocidad
        self.patente = patente.strip().upper()
        self.viajes = []
        self.disponible=True
        self.centro_vehiculo = centro_vehiculo

    def nivel_trafico(self) -> float:
        """
        Simula y retorna un nivel de tráfico aleatorio entre 0.1 y 2.0.

        Returns:
            float: Nivel de tráfico (1.0 = tráfico normal, >1.0 = tráfico lento).
        """
        return round(random.uniform(0.1, 2.0), 2)

    @abstractmethod
    def calculo_tiempo (self, dist, trafico=None) -> float:
        """
        Método abstracto para calcular el tiempo estimado de viaje.

        Debe ser implementado por las subclases. Puede tener en cuenta el tráfico.

        Args:
            dist (float): Distancia a recorrer (en km).
            trafico (float, opcional): Factor de tráfico (por defecto, None).

        Returns:
            float: Tiempo estimado de viaje (en horas).
        """
        pass 

    def agregar_viaje(self, dist, tiempo, trafico=0) -> None:
        """
        Registra un nuevo viaje en el historial del vehículo.

        Args:
            dist (float): Distancia del viaje.
            tiempo (float): Tiempo estimado de duración.
            trafico (float): Nivel de tráfico durante el viaje.
        """
        self.viajes.append({
            'fecha': datetime.now(), # ??
            'distancia': dist,
            'tiempo estimado': tiempo,
            'trafico': trafico
        })

    def historial_viajes(self) -> list[dict]:
        """
        Retorna una copia del historial de viajes del vehículo.

        Returns:
            list[dict]: Lista de viajes registrados.
        """
        return self.viajes.copy()

    def __str__(self):
        """
        Representación en cadena del vehículo.

        Returns:
            str: Información básica del vehículo (tipo, patente y velocidad).
        """
        #define cómo se representa un objeto de una clase como una cadena de texto.
        return f"{self.__class__.__name__} - Patente: {self.patente}, Velocidad: {self.velocidad} km/h"

    def __eq__(self, other):
        """
        Compara dos vehículos por su patente.

        Args:
            other (Vehiculo): Otro vehículo para comparar.

        Returns:
            bool: True si las patentes son iguales, False en caso contrario.
        """
        if not isinstance(other, Vehiculo):
            return False
        return self.patente == other.patente


