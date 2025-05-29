from INCUCAI.Paciente.Paciente import Paciente
from datetime import datetime, date


'''
El receptor contiene órgano que va a recibir, fecha que fue agregado a la lista de espera, 
prioridad, patología y estado (Estable o Inestable).


'''

class Receptor(Paciente):

    lista_receptor_temporal = []
    
    def __init__(self, nombre, DNI, fecha_nac, sexo, telefono, contacto, tipo_sangre, centro, que_es, hla_a1, hla_a2, hla_b1, hla_b2, hla_dr1, hla_dr2, org_recib, fecha_list_esp, patologia, estado):
        super().__init__(nombre, DNI, fecha_nac, sexo, telefono, contacto, tipo_sangre, centro, que_es, hla_a1, hla_a2, hla_b1, hla_b2, hla_dr1, hla_dr2)
        self.org_recib = [org.strip().lower() for org in org_recib] 
        self.fecha_list_esp = fecha_list_esp
        self.patologia = patologia
        estado = estado.upper()
        if estado not in ["ESTABLE", "INESTABLE"]:
            raise ValueError("Estado debe ser 'ESTABLE' o 'INESTABLE'")
        self.estado = estado
        

    
    def prioridad_numerica(self):
        return 1 if self.estado == "INESTABLE" else 2
    
    @classmethod
    def agregar(cls, receptor):
        cls.lista_receptor_temporal.append(receptor)
        print("Receptor agregado correctamente. \n")
    

    @classmethod
    def listar(cls):
        return cls.lista_receptor_temporal
    
    def __str__(self):
        orgs = ", ".join(self.org_recib)
        return f"Receptor: {self.nombre}, DNI: {self.DNI}, Órganos a recibir: {orgs}, Sangre: {self.tipo_sangre}"
    
    @classmethod
    def lista_espera_ordenada(cls):
        '''para ordenar la lista de pacientes y que me los de por orden de agregado a la lista, mas cerca a mas lejos'''
        return sorted(cls.lista_receptor_temporal, key=lambda r: r.fecha_list_esp)
    
