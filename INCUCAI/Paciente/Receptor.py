from .Paciente import *

class Receptor(Paciente):

    lista_receptor = []
    def __init__(self, orga_recib, fecha_list_esp, patologia, estado):
        #falta heredar los datos de paciente
        self.org_recib = orga_recib #solo puede recibir un organo --> como valido esto?
        self.fecha_list_esp = fecha_list_esp
        self.patologia = patologia
        self.estado = estado
        #self.lista_receptor = []
        #Falta determinar de que otros atributos dependeria su prioridad

    
        
    def agregar(self, cls, datos):
        cls.lista_receptor.append(datos)
        print("Donante agregado correctamente. \n")

    def listar(self, cls):
        return cls.lista_receptor
    #def metodo_prioridad --> un metodo que en base a consideraciones
    # de los atributos, defina el estado de prioridad
    
    #metodo que determine que frente a dos pacientes con la misma prioridad, va antes el que esta
    #hace mas tiempo esperando 
    
    
