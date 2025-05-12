

from .Paciente import *
from datetime import datetime, date

class Donante(Paciente):


    def __init__(self, nombre, DNI, fecha_nac, sexo, telefono, contacto, tipo_sangre, centro, que_es,  fecha_fall, hora_fall, hora_ablacion, fecha_ablacion, lista_organos):
        super().__init__(nombre, DNI, fecha_nac, sexo, telefono, contacto, tipo_sangre, centro, que_es)
        self.fecha_fall = fecha_fall
        self.fecha_ablacion = fecha_ablacion
        self.hora_ablacion = hora_ablacion
        self.hora_fall = hora_fall
        self.lista_organos = lista_organos
        self.fecha_creacion = date.today()
        self.hora_creacion = datetime.now().time()
        self.lista_donantes = []  # Lista de todos los donantes (atributo de clase)
        Donante.lista_donantes.append(self) 

    

    def agregar(cls, datos): #uso este cls porque estoy usando una lista, un atributo de la CLASE, no una sola variable
        cls.lista_donantes.append(datos)
        print("Donante agregado correctamente. \n")

    def listar(self, cls):
        return cls.lista_donantes