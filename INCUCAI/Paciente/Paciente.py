from abc import ABC
from datetime import datetime
#from INCUCAI import Incucai 
import re



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
        self.que_es = que_es 
        self.lista_pacientes=[]

    @classmethod
    def agregar(cls, que_es): 
        print("\nINGRESE DATOS DEL PACIENTE:")
        
        while True:
            nombre = input("\nIngrese nombre: ")
            if re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñüÜ ]+", nombre):
                break
            print("❌El nombre solo debe contener letras y espacios")
        
        while True:
            DNI = int(input("\nIngrese DNI: ")) 
            if DNI.isdigit() and 7 <= len(DNI) <= 8:
                DNI = int(DNI)
                break
            print("❌ DNI inválido. Debe tener solo números (7 u 8 cifras).")

        while True:
            fecha_nac = input("\nIngrese fecha de nacimiento dd/mm/aaaa: ") 
            try: 
                datetime.strptime(fecha_nac, "%d/%m/%Y")
                break
            except ValueError:
                print("❌ Fecha inválida. Use el formato dd/mm/aaaa.")

        while True:
            telefono = int(input ("\nIngrese telefono: "))
            if telefono.isdigit() and len(telefono) >= 6:
                telefono = int(telefono)
                break
            print("❌ Teléfono inválido. Debe tener solo números (mín. 6 dígitos).")

        while True:
            contacto = int(input ("\nIngrese telefono de emergencia: "))
            if contacto.isdigit() and len(contacto) >= 6:
                contacto = int(contacto)
                break
            print("❌ Teléfono inválido. Debe tener solo números (mín. 6 dígitos).")
         
        while True:
            sexo = input ("\nIngrese sexo (F/M): ").upper() 
            if sexo in ["F", "M"]:
                break
            print("❌ Ingrese 'F' o 'M' solamente.")
        
        centro = input ("\nIngrese el centro de salud: ") #yo susnpingo q aca deberiamos dar las opciones de centro de salud que tenemos vargadas o nose q es lo q vamos a usar al final respecto a eso
        
        tipos_validos = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
        while True:
            tipo_sangre = input ("\nIngrese tipo de sangre: ").upper()
            if tipo_sangre in tipos_validos:
                break
            print("❌ Tipo de sangre inválido.")
        
        que_es = que_es
        return cls(nombre, DNI, fecha_nac, sexo, telefono, contacto, tipo_sangre, centro, que_es)
        
            
    '''def datos_pacientes(self): #funciona a modo de getter 
        #completar la impresion de este getter
        print(f"El paciente es {self.nombre}\nDNI:{self.DNI}\nfecha de nacimiento:{self.fecha_nac}")'''


