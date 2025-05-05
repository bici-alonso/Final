main.py
from Centros_de_salud import Centro_de_salud
from INCUCAI import INCUCAI
from Donante import Donante
from Organos import Organos
from Paciente import Paciente
from Receptor import Receptor
from Vehiculos import Vehiculos

def main():
    #a fines de testeo usamos estos objetos que no los hago por carga de datos
    paciente= Paciente("Zoe", 46821489, "6/11/2005", "F", 1126485713, "0+", "Favaloro", "Donante") #esta carga deberia resolverse con la funcion agregar
    paciente2=Paciente("Vicky", 46583726, "25/03/2005", "F", 1135857168, "0+", "Favaloro", "Donante" )
    paciente.datos_pacientes() #metodo tipo getter
    paciente2.datos_paciente()



main.py
if __name__ == "__main__":
    main()
    
