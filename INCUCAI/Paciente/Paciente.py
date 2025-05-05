from abc import ABC
from INCUCAI import Incucai 



class Paciente (ABC):

    def __init__(self, nombre, DNI, fecha_nac, sexo, telefono, contacto, tipo_sangre, centro_salud, que_es):
        
        self.nombre = nombre
        self.DNI = DNI
        self.fecha_nac = fecha_nac
        self.sexo = sexo
        self.telefono = telefono 
        self.contacto=contacto
        self.tipo_sangre = tipo_sangre
        self.centro_salud = centro_salud
        self.que_es = incucai.asignar_pac()
        #que_es #para ver si es receptor o donante 
        self.lista_pacientes=[]

    def agregar(self): #Falta validacion de carga de datos
        print("Ingrese datos del paciente:") #el nombre no puede tener nros o caracteres especiales
        self.nombre = input("Ingrese nombre:")
        self.DNI = int(input("Ingrese DNI:")) #el dni debe tener cierta cantidad de cifras 
        self.fecha_nac = input("Ingrese fecha de nacimiento:") #la fecha debe venir en cierto formato
        #agregar telefono --> verificacion solo nros
        #agregar contacto de emerg --> verificacion solo nros
        #agregar sexo --> verificacion m/f
        #agregar centro de salud asociado
        #agregar tipo de sangre --> verificacion que sea un tipo de sangre valido
        
        if super().asignar_lista() == 1: #la asignacion de la lista quiero hacerla en base a la palabra donante o receptor (revisar en metodo asignar_lista)
            
    def datos_pacientes(self): #funciona a modo de getter 
        #completar la impresion de este getter
        print(f"El paciente es {self.nombre}\nDNI:{self.DNI}\nfecha de nacimiento:{self.fecha_nac}")


