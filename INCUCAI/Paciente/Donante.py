from .Paciente import *
from datetime import datetime, date
from INCUCAI.Paciente.Receptor import Receptor
from INCUCAI.Organos.Organo import Organo

class Donante(Paciente):
    lista_donantes = []  
    def __init__(self, nombre, DNI, fecha_nac, sexo, telefono, contacto, tipo_sangre, centro, que_es, hla_a1, hla_a2, hla_b1, hla_b2, hla_dr1, hla_dr2, fecha_fall, hora_fall, hora_ablacion, fecha_ablacion, lista_organos, estado_donante):
        super().__init__(nombre, DNI, fecha_nac, sexo, telefono, contacto, tipo_sangre, centro, que_es, hla_a1, hla_a2, hla_b1, hla_b2, hla_dr1, hla_dr2)
        
        self.fecha_fall = fecha_fall
        self.hora_fall=hora_fall
        
        self.fecha_ablacion = fecha_ablacion
        self.hora_ablacion = hora_ablacion
        self.lista_organos = [
            Organo(o.strip().lower()) if not isinstance(o, Organo) else o
            for o in lista_organos
        ]
        
        self.hora_fall = hora_fall
        self.fecha_creacion = date.today()
        self.hora_creacion = datetime.now().time()
        
        self.estado_donante=estado_donante

    def compatibilidad_hla(self, otro_paciente: Receptor) -> tuple [int, int]:
        """
        Calcula la cantidad de coincidencias HLA entre este paciente (donante) y otro paciente (receptor).
        Se comparan los siguientes loci genéticos:
        - HLA-A (2 alelos)
        - HLA-B (2 alelos)
        - HLA-DR (2 alelos)
        Para cada uno de los tres loci, se compara cada alelo del donante con ambos alelos del receptor.
        Se suma un punto por cada coincidencia, sin contar duplicados por alelos idénticos en el mismo locus.
        Argumentos:
            -otro_paciente:Receptor
        Returns:
            tuple[int, int]: Una tupla con:
                - El número de coincidencias (máximo 6)
                - El total posible de coincidencias (siempre 6)
        """
        matchs = 0, total=6
        #compara genoma A:
        if self.hla_a1 in [otro_paciente.hla_a1, otro_paciente.hla_a2]:
            matchs += 1
        if self.hla_a2 in [otro_paciente.hla_a1, otro_paciente.hla_a2] and self.hla_a2 != self.hla_a1:
            matchs += 1
        #compara genoma B:
        if self.hla_b1 in [otro_paciente.hla_b1, otro_paciente.hla_b2]:
            matchs += 1
        if self.hla_b2 in [otro_paciente.hla_b1, otro_paciente.hla_b2] and self.hla_b2 != self.hla_b1:
            matchs += 1
        #compara genoma dr:
        if self.hla_dr1 in [otro_paciente.hla_dr1, otro_paciente.hla_dr2]:
            matchs += 1 
        if self.hla_dr2 in [otro_paciente.hla_dr1, otro_paciente.hla_dr2] and self.hla_dr2 != self.hla_dr1:
            matchs += 1 
        return matchs, total
    
    def es_compatible_sangre(self, otro_paciente: Receptor) -> bool:
        """
        Evalua la compatibilidad sanguinea entre donante y receptor
        Argumentos:
            - Receptor
        return:
            - Bool con True si son compatibles y False si no lo son
        """
        compatibilidades = {
                "O-": ["O-", "O+", "A-", "A+", "B-", "B+", "AB-", "AB+"],  #0- dona a todos
                "O+": ["O+", "A+", "B+", "AB+"],
                "A-": ["A-", "A+", "AB-", "AB+"],
                "A+": ["A+", "AB+"],
                "B-": ["B-", "B+", "AB-", "AB+"],
                "B+": ["B+", "AB+"],
                "AB-": ["AB-", "AB+"],
                "AB+": ["AB+"] 
            }
        tipo_donante = self.tipo_sangre
        if tipo_donante not in compatibilidades.keys():
            raise ValueError("Tipo de sangre de donante no válido")
        tipo_receptor = otro_paciente.tipo_sangre
        if tipo_receptor not in compatibilidades.keys():
            raise ValueError("Tipo de sangre del receptor no válido")
        
        return tipo_receptor in compatibilidades.get(tipo_donante, [])
    
    def __str__(self):
        organos = [organo.tipo for organo in self.lista_organos]
        return f"Donante: {self.nombre}, DNI: {self.DNI}, Órganos: {','.join(organos)}, Sangre: {self.tipo_sangre}"
    
    @classmethod
    def agregar(cls, donante):
        cls.lista_donantes.append(donante)
    
    