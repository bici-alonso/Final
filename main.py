#from INCUCAI.Centros.Centro import Centro
from INCUCAI.Incucai import Incucai
from INCUCAI.Paciente.Donante import Donante
#from INCUCAI.Organos.Organo import Organo
from INCUCAI.Paciente.Paciente import Paciente
from INCUCAI.Paciente.Receptor import Receptor
#from INCUCAI.Vehiculo.Vehiculo import Vehiculo

def main():
    #a fines de testeo usamos estos objetos que no los hago por carga de datos
    #paciente= Paciente("Zoe", 46821489, "6/11/2005", "F", 1126485713, "0+", "Favaloro", "Donante") #esta carga deberia resolverse con la funcion agregar
    #paciente2=Paciente("Vicky", 46583726, "25/03/2005", "F", 1135857168, "0+", "Favaloro", "Donante" )
    #paciente.datos_pacientes() #metodo tipo getter
    #paciente2.datos_paciente()
    incucai = Incucai()
    incucai.clasificar_pac()

    for d in Donante.listar():
        print("--------------------lista donantes---------------")
        print(d)
    
    for r in Receptor.listar():
        print("---------------------lista receptores------------------")
        print(r)


if __name__ == "__main__":
    main()

