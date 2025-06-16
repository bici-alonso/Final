from INCUCAI.Paciente.Paciente import Paciente
from datetime import datetime, date



class Receptor(Paciente):
    """
    Representa a un paciente receptor en el sistema de trasplantes del INCUCAI.

    Esta clase hereda de `Paciente` y añade atributos y métodos específicos para los pacientes que están
    en lista de espera para recibir un órgano.

    Atributos de clase:
    -------------------
    lista_receptor_temporal : list[Receptor]
        Lista temporal de todos los receptores registrados en el sistema.

    Atributos de instancia:
    -----------------------
    org_recib : str
        Órgano que el paciente necesita recibir.
    fecha_list_esp : datetime.date
        Fecha en la que el paciente fue incluido en la lista de espera.
    patologia : str
        Patología que justifica la necesidad del trasplante.
    estado : str
        Estado clínico del paciente. Debe ser "ESTABLE" o "INESTABLE".

    Métodos:
    --------
    __init__(...)
        Constructor. Inicializa todos los atributos específicos del receptor.
    prioridad_numerica()
        Devuelve un número que representa la prioridad clínica del receptor.
    agregar(receptor)
        Agrega un receptor a la lista temporal de receptores.
    listar()
        Retorna la lista completa de receptores temporales.
    lista_espera_ordenada()
        Devuelve la lista ordenada por fecha de ingreso a la lista de espera.
    __str__()
        Representación en cadena del receptor con los datos más relevantes.
    """
    
    lista_receptor_temporal = []
    
    def __init__(self, nombre, DNI, fecha_nac, sexo, telefono, contacto, tipo_sangre, centro, que_es, hla_a1, hla_a2, hla_b1, hla_b2, hla_dr1, hla_dr2, org_recib, fecha_list_esp, patologia, estado) -> None:
        """
        Constructor de la clase Receptor.

        Inicializa los datos generales del paciente receptor, incluyendo órgano a recibir,
        estado de salud, y fecha de ingreso a la lista de espera.

        Args:
            nombre (str): Nombre del paciente.
            DNI (int): Documento Nacional de Identidad.
            fecha_nac (datetime.date): Fecha de nacimiento.
            sexo (str): Sexo del paciente.
            telefono (str): Teléfono de contacto.
            contacto (str): Contacto de emergencia.
            tipo_sangre (str): Grupo sanguíneo del paciente.
            centro (Centro): Centro médico asignado.
            que_es (str): Tipo de paciente (se sobreescribe como "receptor").
            hla_a1, hla_a2, hla_b1, hla_b2, hla_dr1, hla_dr2 (str): Antígenos HLA.
            org_recib (str): Órgano que necesita el paciente.
            fecha_list_esp (datetime.date): Fecha de inclusión en la lista de espera.
            patologia (str): Patología que motiva el trasplante.
            estado (str): Estado clínico ("ESTABLE" o "INESTABLE").

        Raises:
            ValueError: Si el estado no es "ESTABLE" ni "INESTABLE".
        """
        super().__init__(nombre, DNI, fecha_nac, sexo, telefono, contacto, tipo_sangre, centro, que_es, hla_a1, hla_a2, hla_b1, hla_b2, hla_dr1, hla_dr2)
        self.que_es="receptor"
        self.org_recib = org_recib
        self.fecha_list_esp = fecha_list_esp
        self.patologia = patologia
        estado = estado.upper()
        if estado not in ["ESTABLE", "INESTABLE"]:
            raise ValueError("Estado debe ser 'ESTABLE' o 'INESTABLE'")
        else: 
            self.estado = estado
        
    
    def prioridad_numerica(self) -> int:
        """
        Retorna un valor numérico que representa la prioridad del receptor.

        - Receptores en estado INESTABLE tienen prioridad 1 (más urgente).
        - Receptores ESTABLE tienen prioridad 2 (menos urgente).

        Returns:
            int: Valor de prioridad, 1 o 2.
        """
        return 1 if self.estado == "INESTABLE" else 2
    
    @classmethod
    def agregar(cls, receptor) -> None:
        """
        Agrega un objeto Receptor a la lista temporal de receptores.

        Args:
            receptor (Receptor): Instancia de la clase Receptor a agregar.
        """
        cls.lista_receptor_temporal.append(receptor)
        print("Receptor agregado correctamente. \n")
    

    @classmethod
    def listar(cls) -> list:
        """
        Devuelve la lista completa de receptores temporales.

        Returns:
            list[Receptor]: Lista de receptores registrados temporalmente.
        """
        return cls.lista_receptor_temporal
    
    def __str__(self) -> str:
        """
        Representación simple del receptor para impresión.

        Returns:
            str: Cadena con nombre, DNI, órgano a recibir y tipo de sangre.
        """
        return f"Receptor: {self.nombre}, DNI: {self.DNI}, Órganos a recibir: {self.org_recib}, Sangre: {self.tipo_sangre}"
    
    @classmethod
    def lista_espera_ordenada(cls) -> list:
        """
        Retorna la lista de receptores ordenada por fecha de ingreso a la lista de espera.

        Cuanto más antigua sea la fecha, más arriba estará el paciente en la lista.

        Returns:
            list[Receptor]: Lista ordenada cronológicamente.
        """
        return sorted(cls.lista_receptor_temporal, key=lambda r: r.fecha_list_esp)