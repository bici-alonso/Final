from INCUCAI.Vehiculo.Vehiculo import Vehiculo

class Ambulancia(Vehiculo):
    """
    Clase que representa una ambulancia utilizada en el sistema de transporte del INCUCAI.

    Hereda de:
        Vehiculo

    Las ambulancias se ven afectadas por el tráfico urbano, por lo que el tiempo total de viaje
    incluye un valor adicional que representa el nivel de tráfico.

    Métodos:
    --------
    __init__(velocidad, patente, centro_vehiculo)
        Inicializa una ambulancia con su velocidad, patente y centro asociado.
    
    calculo_tiempo(dist, trafico=None)
        Calcula el tiempo estimado de viaje considerando la distancia y el nivel de tráfico.
        Registra el viaje.

    Excepciones:
    ------------
    ValueError:
        - Si la distancia es negativa.
        - Si el tráfico es negativo.
    """
    def __init__(self, velocidad, patente, centro_vehiculo) -> None:
        """
        Constructor de la ambulancia.

        Args:
            velocidad (float): Velocidad de la ambulancia en km/h. Debe ser mayor a 0.
            patente (str): Patente identificatoria de la ambulancia.
            centro_vehiculo (Centro): Centro médico al que pertenece la ambulancia.
        """
        super().__init__(velocidad, patente, centro_vehiculo)
    
    def calculo_tiempo(self, dist, trafico=None) -> float:
        """
        Calcula el tiempo estimado de viaje teniendo en cuenta el tráfico.

        Si no se proporciona un valor de tráfico, se genera aleatoriamente mediante
        el método `nivel_trafico`.

        Args:
            dist (float): Distancia a recorrer en kilómetros.
            trafico (float, opcional): Nivel de tráfico a considerar. Si es None, se calcula automáticamente.

        Returns:
            float: Tiempo estimado total de viaje en horas.

        Raises:
            ValueError: Si la distancia o el tráfico son negativos.
        """
        if dist < 0:
            raise ValueError("La distancia no puede ser negativa")
        if trafico is None:
            trafico = self.nivel_trafico()
        if trafico < 0:
            raise ValueError("El tráfico no puede ser negativo")
        
        tiempo_basico = dist / self.velocidad
        tiempo_total = tiempo_basico + trafico
        
        self.agregar_viaje(dist, tiempo_total, trafico)
        
        return tiempo_total