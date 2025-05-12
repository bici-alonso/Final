

from Paciente import *
from datetime import datetime, date

class Donante(Paciente):

    lista_donantes = []  # Lista de todos los donantes (atributo de clase)

    def __init__(self, nombre, DNI, fecha_nac, sexo, telefono, contacto, tipo_sangre, centro, que_es,  fecha_hora_fall, fecha_hora_ablacion, lista_organos):
        super().__init__(nombre, DNI, fecha_nac, sexo, telefono, contacto, tipo_sangre, centro, que_es)
        self.fecha_hora_fall = fecha_hora_fall
        self.fecha_hora_ablacion = fecha_hora_ablacion
        self.lista_organos = lista_organos
        self.fecha_creacion = date.today()
        self.hora_creacion = datetime.now().time()
        Donante.lista_donantes.append(self) 

    

    def agregar(cls, datos): #uso este cls porque estoy usando una lista, un atributo de la CLASE, no una sola variable
        cls.lista_donantes.append(datos)
        print("Donante agregado correctamente. \n")

    def listar(self, cls):
        return cls.lista_donantes