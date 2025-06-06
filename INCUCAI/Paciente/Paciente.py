'''
Los Pacientes poseen nombre, DNI (el cual es único), fecha de nacimiento, sexo, teléfono de contacto, tipo de
sangre, y centro de salud asociado. Los pacientes se dividen entre receptores y donantes.
El donante posee la fecha y hora de fallecimiento, fecha y hora del comienzo de ablación y listado de órganos a donar. 
El receptor contiene órgano que va a recibir (uno solo) fecha que fue agregado a la lista de espera, prioridad, patología y
estado (Estable o Inestable).


'''

from abc import ABC
from datetime import date
from INCUCAI.Centros.Centro import *


class Paciente (ABC):

    pacientes_registrados = [] 
    
    def __init__(self, nombre, DNI, fecha_nac, sexo, telefono, contacto, tipo_sangre, centro, que_es, hla_a1, hla_a2, hla_b1, hla_b2, hla_dr1, hla_dr2):
        
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
        return self.calculo_edad() < 18
    
    def datos_pacientes_generico(self):
        
        print("\nINFORMACION DE PACIENTE:")
        print(f"\nDNI: {self.DNI}. Paciente: {self.nombre}.") 
        print (f"\nTelefono: {self.telefono}. \nContacto de emergencia: {self.contacto}")
        print(f"\nFecha de nacimiento: {self.fecha_nac}. \nEdad: {self.calculo_edad()}")
        print(f"\nTipo de sangre: {self.tipo_sangre}")
        print(f"HLA: A({self.hla_a1}/{self.hla_a2}) B({self.hla_b1}/{self.hla_b2}) DR({self.hla_dr1}/{self.hla_dr2})")
        print (f"\nSexo: {self.sexo}")
        print(f"\nCentro de salud: {self.centro} \nTipo de paciente: {self.que_es}")
    
    def __eq__(self, other):
        return isinstance(other, Paciente) and self.DNI == other.DNI

