from .Paciente import *
from datetime import datetime

class Receptor(Paciente):

    lista_receptor = []
    def __init__(self, nombre, DNI, fecha_nac, sexo, telefono, contacto, tipo_sangre, centro, que_es, org_recib, fecha_list_esp, patologia, estado):
        super().__init__(nombre, DNI, fecha_nac, sexo, telefono, contacto, tipo_sangre, centro, que_es)
        self.org_recib = org_recib #solo puede recibir un organo --> como valido esto?
        self.fecha_list_esp = datetime.strptime(fecha_list_esp, "%d/%m/%Y")
        self.patologia = patologia
        self.estado = estado
        #self.lista_receptor = []
        #Falta determinar de que otros atributos dependeria su prioridad

    
    @classmethod
    def agregar(cls, receptor):
        cls.lista_receptor.append(receptor)
        print("Receptor agregado correctamente. \n")

    @classmethod
    def listar(cls):
        return cls.lista_receptor
    
    def __str__(self):
        return f"Receptor: {self.nombre}, DNI: {self.DNI}, Órganos a recibir: {self.org_recib}, Sangre: {self.tipo_sangre}"
    
    @classmethod
    def lista_espera_ordenada(cls):
        '''para ordenar la loista de pacientes y que me los de por orden de agregado a la lista, mas cerca a mas lejos'''
        return sorted(cls.lista_receptor, key=lambda r: r.fecha_list_esp)
    #def metodo_prioridad --> un metodo que en base a consideraciones
    # de los atributos, defina el estado de prioridad
    
    #metodo que determine que frente a dos pacientes con la misma prioridad, va antes el que esta
    #hace mas tiempo esperando 
    
    
