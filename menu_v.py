from INCUCAI.Centros.Centro import Centro_de_salud
from INCUCAI.Incucai import Incucai
from INCUCAI.Paciente.Donante import Donante
from INCUCAI.Organos.Organo import *
from INCUCAI.Paciente.Paciente import Paciente
from INCUCAI.Paciente.Receptor import Receptor
from INCUCAI.Vehiculo.Vehiculo import Vehiculo
from datetime import date



incucai = Incucai()
    
print("==== SIMULACIÓN DE SISTEMA INCUCAI ====\n")
donante_vivo = Donante("Juan Perez", 12345678, date(1980, 5, 12),"M", "123456789","Maria Perez", "A+", "Favaloro", que_es="donante", hla_a1="01", hla_a2="02", hla_b1="07", hla_b2="08", hla_dr1="15", hla_dr2="16", fecha_fall=None, hora_fall=None, hora_ablacion=None, fecha_ablacion=None, lista_organos=["corazon"])
receptor = Receptor("Ana Gomez", 87654321, date(1995, 10, 20), "F", "987654321", "Carlos Gomez", "A+", "Favaloro", que_es="receptor", hla_a1="01", hla_a2="02", hla_b1="07", hla_b2="08", hla_dr1="15", hla_dr2="16", org_recib=["corazon"], fecha_list_esp="01/01/2024", patologia="Insuficiencia renal", estado="Estable")


print("\n--- Registro de Donante ---")
incucai.clasificar_paciente_ya_existente(paciente_existente=donante_vivo)

print("\n--- Registro de Receptor ---")
incucai.clasificar_paciente_ya_existente(paciente_existente=receptor)

print("\n--- Estado Final del Sistema ---")
print("\nDonantes registrados:")
incucai.listar_donantes()
    
print("\nReceptores en espera:")
incucai.listar_receptores()

print("\nCentros de salud registrados:")
incucai.mostrar_centros_salud()