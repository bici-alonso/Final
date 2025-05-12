from abc import ABC
from datetime import datetime
from INCUCAI import Incucai 



class Paciente (ABC):

    def __init__(self, nombre, DNI, fecha_nac, sexo, telefono, contacto, tipo_sangre, centro, que_es):
        
        self.nombre = nombre
        self.DNI = DNI
        self.fecha_nac = fecha_nac
        self.sexo = sexo
        self.telefono = telefono 
        self.contacto=contacto
        self.tipo_sangre = tipo_sangre
        self.centro = centro
        self.que_es = que_es #??
        #que_es #para ver si es receptor o donante 
        self.lista_pacientes=[]

    def agregar(self, que_es): #Falta validacion de carga de datos
        print("\nINGRESE DATOS DEL PACIENTE:") #el nombre no puede tener nros o caracteres especiales
        self.nombre = input("\nIngrese nombre:")
        self.DNI = int(input("\nIngrese DNI:")) #el dni debe tener cierta cantidad de cifras 
        self.fecha_nac = input("\nIngrese fecha de nacimiento:") #la fecha debe venir en cierto formato
        self.telefono = input ("\nIngrese telefono") # --> verificacion solo nros
        self.contacto = input ("\nIngrese telefono de emergencia") #--> verificacion solo nros
        self.sexo = input ("\nIngrese sexo del paciente") #--> verificar F/M
        self.centro = input ("\nIngrese el centro de salud del paciente") # no tiene restricciones ???
        self.tipo_sangre=input ("\nIngrese tipo de sangre") # --> verificacion que sea un tipo de sangre valido
        self.que_es = que_es
        
            
    '''def datos_pacientes(self): #funciona a modo de getter 
        #completar la impresion de este getter
        print(f"El paciente es {self.nombre}\nDNI:{self.DNI}\nfecha de nacimiento:{self.fecha_nac}")'''


