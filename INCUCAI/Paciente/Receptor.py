
from Paciente import *

class Receptor(Paciente):


    def __init__(self, orga_recib, fecha_list_esp, patologia, estado):
        #falta heredar los datos de paciente
        self.org_recib = orga_recib #solo puede recibir un organo --> como valido esto?
        self.fecha_list_esp = fecha_list_esp
        self.patologia = patologia
        self.estado = estado
        #Falta determinar de que otros atributos dependeria su prioridad
        
    #def metodo_prioridad --> un metodo que en base a consideraciones
    # de los atributos, defina el estado de prioridad
    
    #metodo que determine que frente a dos pacientes con la misma prioridad, va antes el que esta
    #hace mas tiempo esperando 
    
