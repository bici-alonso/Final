from abc import ABC
from datetime import date
from INCUCAI.Centros.Centro import *



class Paciente (ABC):
    """
    Clase base abstracta que representa a un paciente dentro del sistema del INCUCAI.

    Atributos de clase:
    -------------------
    pacientes_registrados : list
        Lista que contiene los DNIs de todos los pacientes registrados.

    Atributos de instancia:
    -----------------------
    nombre : str
        Nombre completo del paciente.
    DNI : int
        Documento Nacional de Identidad del paciente.
    fecha_nac : datetime.date
        Fecha de nacimiento del paciente.
    sexo : str
        Sexo del paciente ('M', 'F', etc.).
    telefono : str
        Número de teléfono del paciente.
    contacto : str
        Información de contacto de emergencia.
    tipo_sangre : str
        Grupo sanguíneo del paciente (ej. "A+", "O-", etc.).
    centro : Centro
        Centro de salud asociado al paciente.
    que_es : str
        Tipo de paciente (por ejemplo, "donante", "receptor", etc.).
    hla_a1, hla_a2, hla_b1, hla_b2, hla_dr1, hla_dr2 : str
        Antígenos HLA del paciente utilizados para compatibilidad en trasplantes.

    Métodos:
    --------
    __init__(...)
        Constructor de la clase. Inicializa todos los atributos del paciente y lo registra.
    calculo_edad()
        Devuelve la edad del paciente en años.
    es_menor_de_edad()
        Retorna True si el paciente es menor de 18 años, False en caso contrario.
    datos_pacientes_generico()
        Imprime en consola los datos generales del paciente.
    __eq__(other)
        Compara dos pacientes por su DNI.
    """

    pacientes_registrados = [] 
    
    def __init__(self, nombre, DNI, fecha_nac, sexo, telefono, contacto, tipo_sangre, centro, que_es, hla_a1, hla_a2, hla_b1, hla_b2, hla_dr1, hla_dr2):
        """
        Constructor de la clase Paciente.
        Parámetros:
        -----------
        nombre : str
            Nombre del paciente.
        DNI : int
            Documento Nacional de Identidad.
        fecha_nac : datetime.date
            Fecha de nacimiento.
        sexo : str
            Sexo del paciente.
        telefono : str
            Número de teléfono.
        contacto : str
            Información de contacto de emergencia.
        tipo_sangre : str
            Tipo de sangre (ej: 'A+', 'O-', etc.).
        centro : Centro
            Centro médico asociado al paciente.
        que_es : str
            Tipo de paciente: "donante", "receptor", etc.
        hla_a1, hla_a2, hla_b1, hla_b2, hla_dr1, hla_dr2 : str
            Antígenos HLA del paciente para evaluar compatibilidad.
        """
        self.nombre = nombre
        self.DNI = DNI
        self.fecha_nac = fecha_nac
        self.sexo = sexo
        self.telefono = telefono 
        self.contacto=contacto
        self.tipo_sangre = tipo_sangre
        self.centro = centro
        self.que_es = que_es.lower()
        
        self.hla_a1=hla_a1
        self.hla_a2=hla_a2
        self.hla_b1=hla_b1
        self.hla_b2=hla_b2
        self.hla_dr1=hla_dr1
        self.hla_dr2=hla_dr2
        Paciente.pacientes_registrados.append(DNI)
        
    def calculo_edad(self):
        """
        Calcula la edad actual del paciente en años.
        returns:
            -int: Edad del paciente.
        """
        hoy=date.today()
        return hoy.year - self.fecha_nac.year - ((hoy.month, hoy.day) < (self.fecha_nac.month, self.fecha_nac.day))
    
    def es_menor_de_edad(self):
        """
        Indica si el paciente es menor de 18 años.

        Returns:
        --------
        bool
            True si es menor de edad, False si es mayor o igual a 18.
        """
        return self.calculo_edad() < 18
    
    def datos_pacientes_generico(self):
        """
        Muestra por consola los datos generales del paciente.
        """
        print("\nINFORMACION DE PACIENTE:")
        print(f"\nDNI: {self.DNI}. Paciente: {self.nombre}.") 
        print (f"\nTelefono: {self.telefono}. \nContacto de emergencia: {self.contacto}")
        print(f"\nFecha de nacimiento: {self.fecha_nac}. \nEdad: {self.calculo_edad()}")
        print(f"\nTipo de sangre: {self.tipo_sangre}")
        print(f"HLA: A({self.hla_a1}/{self.hla_a2}) B({self.hla_b1}/{self.hla_b2}) DR({self.hla_dr1}/{self.hla_dr2})")
        print (f"\nSexo: {self.sexo}")
        print(f"\nCentro de salud: {self.centro} \nTipo de paciente: {self.que_es}")
    
    def __eq__(self, other):
        """
        Compara dos pacientes por su DNI.

        Parameters:
        -----------
        other : Paciente
            Otro paciente a comparar.

        Returns:
        --------
        bool
            True si tienen el mismo DNI, False en caso contrario.
        """
        return isinstance(other, Paciente) and self.DNI == other.DNI

