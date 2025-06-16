from INCUCAI.Vehiculo.Vehiculo import Vehiculo



class Helicoptero(Vehiculo):
    """
    Clase que representa un helicóptero utilizado en el sistema de transporte del INCUCAI.

    Hereda de:
        Vehiculo

    Los helicópteros se caracterizan por no verse afectados por el tráfico terrestre, por lo que
    su cálculo de tiempo de viaje ignora el nivel de tráfico.

    Métodos:
    --------
    __init__(velocidad, patente, centro_vehiculo)
        Inicializa un helicóptero con su velocidad, patente y centro asociado.
    calculo_tiempo(dist, trafico=None)
        Calcula el tiempo estimado de viaje en base a la distancia y velocidad del helicóptero,
        sin considerar tráfico. Registra el viaje.

    Excepciones:
    ------------
    ValueError:
        - Si la distancia es negativa.
    """

    def __init__(self, velocidad, patente, centro_vehiculo) -> None:
        """
        Constructor del helicóptero.

        Args:
            velocidad (float): Velocidad del helicóptero en km/h. Debe ser mayor a 0.
            patente (str): Patente identificatoria del helicóptero.
            centro_vehiculo (Centro): Centro médico al que pertenece el helicóptero.
        """
        super().__init__(velocidad, patente, centro_vehiculo)
        
    def calculo_tiempo(self, dist, trafico=None) -> float:
        """
        Calcula el tiempo estimado de viaje sin tener en cuenta el tráfico.

        Este método sobrescribe el método abstracto de la clase base `Vehiculo`.
        Registra el viaje en el historial.

        Args:
            dist (float): Distancia a recorrer en kilómetros.
            trafico (float, opcional): Se ignora, ya que el helicóptero no se ve afectado por tráfico.

        Returns:
            float: Tiempo estimado de viaje en horas.

        Raises:
            ValueError: Si la distancia es negativa.
        """
        if dist < 0:
            raise ValueError("La distancia no puede ser negativa")
        tiempo=dist/self.velocidad
        self.agregar_viaje(dist, tiempo, trafico=0)
        return tiempo
