'''
TRABAJO PRACTICO FINAL - LABO DE PROGRAMACION I. 
SIMULACION SIST. DONACION DE ORGANOS

Alonso Victoria
Pfeifer Zoe

El INCUCAI se encarga de la coordinación y logística de la donación de tejidos y órganos. 
Debido a que su sistema quedó desactualizado por el paso del tiempo, le solicitaron realizar una nueva versión dónde tendrá que mejorar la automatización y
la logística para optimizar la llegada de órganos a los pacientes que se encuentran en la lista de espera. 
Este consta de una lista de receptores, una lista de donantes y una lista de centros de salud habilitados.

El Sistema tiene que permitir:
    -Registrar pacientes nuevos (Validando que no se encuentre en otra lista ni se repita).
    -Quitar de la lista de donantes a aquellos cuyos organos ya han sido utilizados en su totalidad.
    -Quitar de la lista a un receptor una vez que ha recibido su organo exitosamente.
    -Buscar por centro de salud los pacientes de la lista de espera.
    -Buscar un receptor e informar qué prioridad tiene en la lista de espera.
    -Imprimir listado de pacientes donantes y receptores.
    -Realizar correctamente todo el proceso de asignación y derivación de un organo a un receptor,
    contemplando el viaje, la disponibilidad en ese horario de los vehiculos de un centro medico y el tiempo de viaje.


para subir los archivos al git:

git add .

git commit -m "Descripción de lo que hiciste"

git push



'''

#La clase INCUCAI la uso como manager de mis demas clases --> Permite manejar/linkear mis clases y listas

from INCUCAI.Paciente.Paciente import Paciente
from INCUCAI.Paciente.Donante import Donante #no me esta dejando importar, como esta en carpetas chat me dijo q le ponga ese punto pero tampoco funciona
from INCUCAI.Paciente.Receptor import Receptor #lo dejo asi con todo hecho pero nose si esta funcionando bien porque no puedo correrlo
#from INCUCAI.Centros.Centro import Centro_de_salud 

class Incucai:
    
    '''
    El INCUCAI sabe recibir un paciente. Cuando lo hace recibe al Paciente, y lo ingresa.
    
    Si el paciente es donante, al ser ingresado se lo agrega a la lista de pacientes donantes.
    Luego se busca los posibles receptores para
    cada órgano que el donante puede donar, para esto se busca en su lista de pacientes receptores todos los
    pacientes que necesitan ese órgano y tienen el mismo tipo de sangre. Finalmente, se elige el receptor, en
    función a la prioridad del paciente (si tienen la misma prioridad elige al que tiene una fecha anterior de
    ingreso a la lista de espera). En tal caso, se envia el organo correspondiente a la ubicación del paciente
    receptor y se quita de la lista de donantes la disponibilidad de ese organo para ese donante en particular. Si el
    paciente es receptor, se lo agrega a la lista de pacientes receptores, y se busca si hay alguna coincidencia en
    la lista de donantes. De haberlo se despacha el organo para el receptor, actualizando de igual manera la lista
    de donantes.

    '''
    

    def __init__(self):
        #Constructor de INCUCAI
        self.receptores = []
        self.donantes = []
        self.Centros_de_salud = []
        
    def clasificar_pac (self,que_es = None, paciente_exist = None):

        if paciente_exist:
            paciente_base = paciente_exist
            que_es = paciente_base.que_es.lower()
        '''else:
            opcion_don_rec=int(input("A que lista quiere agregar?\n1- Lista Receptores\n2-Lista donantes\n"))
            
            if opcion_don_rec == 1:
                que_es = 'receptor'
            elif opcion_don_rec == 2:
                que_es = 'donante' 
            else:
                print("\nOpcion no valida. El paciente DEBE SER DONANTE O RECEPTOR")
                return'''
            
        paciente_base = Paciente.agregar(que_es)

        dni_a_verificar = paciente_base.DNI

        if any(p.DNI == dni_a_verificar for p in self.donantes + self.receptores):
            print(f" Ya existe un paciente con DNI {dni_a_verificar} en el sistema. No se puede agregar.")
            return
        
        #datos = paciente_base.__dict__  #este dict toma los datos que se guardaron en pqciente y los pasa como uno solo, pata guardarlo en la lista

        if que_es == "donante":
        
            if not paciente_exist:
                fecha_fall = input("Ingrese fecha de fallecimiento (dd/mm/yyyy): ")
                hora_fall = input("Ingrese hora de fallecimiento (HH:MM): ")
                fecha_ablacion = input("Ingrese fecha de ablación (dd/mm/yyyy): ")
                hora_ablacion = input("Ingrese hora de ablación (HH:MM): ")
                lista_organos = input("Ingrese lista de órganos disponibles (separados por coma): ").split(',')

                donante = Donante(
                    paciente_base.nombre,
                    paciente_base.DNI,
                    paciente_base.fecha_nac,
                    paciente_base.sexo,
                    paciente_base.telefono,
                    paciente_base.contacto,
                    paciente_base.tipo_sangre,
                    paciente_base.centro,
                    que_es,
                    fecha_fall,
                    hora_fall,
                    hora_ablacion,
                    fecha_ablacion,
                    lista_organos)
            else:
                donante = paciente_exist
                fecha_fall = input("Ingrese fecha de fallecimiento (dd/mm/yyyy): ")
                hora_fall = input("Ingrese hora de fallecimiento (HH:MM): ")
                fecha_ablacion = input("Ingrese fecha de ablación (dd/mm/yyyy): ")
                hora_ablacion = input("Ingrese hora de ablación (HH:MM): ")
                lista_organos = input("Ingrese lista de órganos disponibles (separados por coma): ").split(',')

                donante = Donante(
                    paciente_base.nombre,
                    paciente_base.DNI,
                    paciente_base.fecha_nac,
                    paciente_base.sexo,
                    paciente_base.telefono,
                    paciente_base.contacto,
                    paciente_base.tipo_sangre,
                    paciente_base.centro,
                    que_es,
                    fecha_fall,
                    hora_fall,
                    hora_ablacion,
                    fecha_ablacion,
                    lista_organos)
                

            Donante.agregar(donante)
            self.donantes.append(donante)

        elif que_es == "receptor":
        
            if not paciente_exist:
                org_recib = input("Ingrese órgano que recibe: ")
                fecha_list_esp = input("Ingrese fecha en lista de espera (dd/mm/yyyy): ")
                patologia = input("Ingrese patología: ")
                estado = input("Ingrese estado: ")

                receptor = Receptor(
                    paciente_base.nombre,
                    paciente_base.DNI,
                    paciente_base.fecha_nac,
                    paciente_base.sexo,
                    paciente_base.telefono,
                    paciente_base.contacto,
                    paciente_base.tipo_sangre,
                    paciente_base.centro,
                    que_es,
                    org_recib,
                    fecha_list_esp,
                    patologia,
                    estado)
            else:
                org_recib = input("Ingrese órgano que recibe: ")
                fecha_list_esp = input("Ingrese fecha en lista de espera (dd/mm/yyyy): ")
                patologia = input("Ingrese patología: ")
                estado = input("Ingrese estado: ")

                receptor = Receptor(
                    paciente_base.nombre,
                    paciente_base.DNI,
                    paciente_base.fecha_nac,
                    paciente_base.sexo,
                    paciente_base.telefono,
                    paciente_base.contacto,
                    paciente_base.tipo_sangre,
                    paciente_base.centro,
                    que_es,
                    org_recib,
                    fecha_list_esp,
                    patologia,
                    estado)

            Receptor.agregar(receptor)
            self.receptores.append(receptor)

    
            

    
            
    #incucai debe tener una validacion que ningun paciente se repite
    #debo sacar de la lista a pacientes que no tiene mas organos para donar
    #debo sacar a los receptores que tuvieron un transplante exitoso