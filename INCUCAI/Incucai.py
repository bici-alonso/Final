class Incucai:


    def __init__(self):
        self.receptores = []
        self.donantes = []
        self.Centros_de_salud = []
        

    def asignar_lista(self): #esta asignacion deberia estar en la clase paciente y deberia directamente leer el atributo que se hace por carga con la palabra ?
        numero=int(input("A que lista quiere agregar?\n1- Lista Receptores\n2-Lista donantes"))
        if numero == 1:
            for i in self.receptores:
                return
    
    #incucai debe tener una validacion que ningun paciente se repite
    #debo sacar de la lista a pacientes que no tiene mas organos para donar
    #debo sacar a los receptores que tuvieron un transplante exitoso


