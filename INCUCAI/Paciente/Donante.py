from .Paciente import *
from datetime import datetime, date
from INCUCAI.Paciente.Paciente import Paciente

class Donante(Paciente):

    lista_donantes = []
    def __init__(self, nombre, DNI, fecha_nac, sexo, telefono, contacto, tipo_sangre, centro, que_es, hla_a1, hla_a2, hla_b1, hla_b2, hla_dr1, hla_dr2, fecha_fall, hora_fall, hora_ablacion, fecha_ablacion, lista_organos):
        super().__init__(nombre, DNI, fecha_nac, sexo, telefono, contacto, tipo_sangre, centro, que_es, hla_a1, hla_a2, hla_b1, hla_b2, hla_dr1, hla_dr2)
        self.fecha_fall = fecha_fall
        self.fecha_ablacion = fecha_ablacion
        self.hora_ablacion = hora_ablacion
        self.hora_fall = hora_fall
        self.lista_organos = lista_organos
        self.fecha_creacion = date.today()
        self.hora_creacion = datetime.now().time()
        # Lista de todos los donantes (atributo de clase)
        #Donante.lista_donantes.append(self) 
        
    
    def __str__ (self):
        return f"Donante: {self.nombre}, DNI: {self.DNI}, Órganos: {self.lista_organos}, Sangre: {self.tipo_sangre}"
    
    