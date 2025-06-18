from INCUCAI.Paciente.Donante import Donante
from INCUCAI.Paciente.Receptor import Receptor
from INCUCAI.Vehiculo.Helicoptero import Helicoptero
from INCUCAI.Vehiculo.Avion import Avion
from INCUCAI.Vehiculo.Ambulancia import Ambulancia
from datetime import time, date
from INCUCAI.Centros.Cirujanos.General import General
from INCUCAI.Centros.Cirujanos.Especialista import Especialista


class Testing:
        def creacion_pacientes (self) -> list:
                '''
                Crea una lista de instancias de pacientes predefinidos (donantes y receptores).

                Esta función genera un conjunto de objetos Donante y Receptor con datos simulados,
                que pueden ser usados para pruebas, carga inicial del sistema o demostraciones.

                Returns:
                        list: Lista que contiene instancias de Donante y Receptor.
                '''
                #Donantes:
                dpaciente1 = Donante("Ana López", 45012345, date(1990, 5, 15), "F", "1123456789", "1198765432", "A+", "Hospital Italiano de La Plata", "Donante", "02", "24", "07", "35", "11", "04", None, None, time(16, 0), date(2025, 5, 21), ["rinon"], "vivo")
                dpaciente2 = Donante("Carlos Pérez", 43123456, date(1985, 7, 10), "M", "1134567890", "1191234567", "O-", "Fundacion Favaloro", "Donante", "03", "30", "08", "15", "13", "07", date(2025, 5, 18), time(13, 0), time(15, 0), date(2025, 5, 19), ["rinon", "corazon"], "muerto")
                dpaciente3=Donante("Juan Perez Rojo", 46583722,date (1999, 6, 21), "M", "011234566", "012345678", "A+", "Fundacion Favaloro", "Donante", "33", "23", "21", "10", "11", "33" , date(2024, 10, 10), time (5, 55), time (7, 21), date(2024, 10, 7), ["pulmones"], "muerto")
                dpaciente4 = Donante("Lucía Torres", 46098765, date(2000, 11, 5), "F", "1156789012", "1192345678", "A-", "Hospital Garrahan", "Donante", "23", "31", "35", "44", "13", "17", date(2025, 5, 24), time(10, 0), time(12, 0), date(2025, 5, 25), ["hígado", "riñón"], "muerto")
                dpaciente5 = Donante("Sofía Díaz", 47000001, date(1999, 8, 13), "F", "1167890123", "1193456789", "O+", "Hospital Zonal Alvear", "Donante", "24", "32", "07", "44", "11", "17", date(2025, 5, 23), time(9, 30), time(11, 30), date(2025, 5, 24), ["corneas", "corazón"], "muerto")
                dpaciente6 = Donante("Matías Herrera", 42234567, date(1988, 3, 30), "M", "1178901234", "1194567890", "A-", "Hospital de Urgencias", "Donante", "22", "30", "31", "54", "13", "17", None, None, time(13, 0), date(2025, 5, 22), ["hígado"], "vivo")
                dpaciente7 = Donante("Elena Ríos", 41023456, date(1978, 12, 19), "F", "1189012345", "1195678901", "AB-", "Hospital Papa Francisco", "Donante", "23", "33", "25", "40", "12", "17", None, None, time(17, 0), date(2025, 5, 20), ["corneas", "piel"], "vivo")
                dpaciente8 = Donante("Diego Suarez", 46543210, date(1996, 4, 8), "M", "1190123456", "1196789012", "B-", "Hospital Clemente Alvarez", "Donante", "23", "30", "32", "42", "10", "17", date(2025, 5, 27), time(13, 30), time(15, 30), date(2025, 5, 28), ["corazón", "riñón"], "vivo")
                dpaciente9 = Donante("Micaela Suárez", 45987654, date(2001, 6, 17), "F", "1191234567", "1197890123", "A+", "Clinica Mayo SRL", "Donante", "23", "30", "35", "44", "13", "17", date(2025, 5, 26), time(14, 15), time(16, 15), date(2025, 5, 27), ["riñón"], "muerto")
                dpaciente10 = Donante("Federico Blanco", 44098765, date(1995, 1, 11), "M", "1192345678", "1198901234", "O-", "Hospital Samic Alem", "Donante", "23", "31", "35", "44", "19", "10",date(2025, 5, 22), time(12, 45), time(14, 45), date(2025, 5, 23), ["corazón", "hígado", "pulmones", "huesos"], "muerto")
                dpaciente11 = Donante("Johnny Bravo", 20498885, date(1970, 9, 12), "M", "34567643", "23456788", "O+", "Clinica Mayo SRL", "Donante", "09", "21", "07", "12", "10", "11", None, None, time(21, 20), date(2025,6, 8), ["huesos"], "vivo")
                dpaciente12= Donante ("Juliana Rios", 45583733, date(2000, 8, 10), "F", "01135857767", "11456737829", "A+", "Clinica Mayo SRL", "Donante", "02", "24", "07", "35", "10", "06", None, None, time (21, 00), date(2025, 6, 10), ["riñón"], "vivo")
                
                #Receptores:
                rpaciente11 = Receptor("Valentina Rossi", 48012345, date(2002, 5, 10), "F", "1112345678", "1123456789", "A+", "Fundacion Favaloro", "Receptor", "02", "24", "07", "35", "11", "04", ["riñón"], date(2024, 6, 1), "insuficiencia renal", "inestable")
                rpaciente12 = Receptor("Julián Navarro", 47876543, date(1998, 4, 22), "M", "1123456789", "1134567890", "O-", "Fundacion Favaloro", "Receptor", "03", "30", "08", "15", "13", "07", ["riñón"], date(2023, 11, 3), "cirrosis", "estable")
                rpaciente13 = Receptor("Martina Silva", 47765432, date(2004, 8, 5), "F", "1134567890", "1145678901", "A-", "Fundacion Favaloro", "Receptor", "24", "32", "07", "44", "11", "17", ["corazón"], date(2023, 9, 12), "miocardiopatía", "estable")
                rpaciente14 = Receptor("Bruno Castro", 47654321, date(2001, 10, 19), "M", "1145678901", "1156789012", "AB+", "Hospital Garrahan", "Receptor", "23", "30", "35", "44", "13", "17", ["riñón"], date(2024, 2, 18), "glomerulonefritis", "inestable")
                rpaciente15 = Receptor("Agustina Paz", 47543210, date(1995, 12, 1), "F", "1156789012", "1167890123", "O+", "Hospital Zonal Alvear", "Receptor", "24", "32", "07", "44", "13", "17", ["corneas"], date(2024, 4, 25), "queratocono", "estable")
                rpaciente16 = Receptor("Lucas Molina", 47432109, date(1993, 7, 7), "M", "1167890123", "1178901234", "A-", "Hospital de Urgencias", "Receptor", "22", "30", "31", "54", "17", "17", ["hígado"], date(2024, 1, 6), "hepatitis", "inestable")
                rpaciente17 = Receptor("Camila Sosa", 47321098, date(2000, 3, 9), "F", "1178901234", "1189012345", "AB-", "Hospital Papa Francisco", "Receptor", "23", "33", "25", "40", "12", "17", ["piel"], date(2023, 10, 20), "quemaduras", "inestable")
                rpaciente18 = Receptor("Tomás Aguirre", 47210987, date(1999, 11, 30), "M", "1189012345", "1190123456", "B-", "Hospital Clemente Alvarez", "Receptor", "23", "30", "32", "42", "10", "17", ["corazón"], date(2024, 3, 3), "cardiopatía", "inestable")
                rpaciente19 = Receptor("Luciana Medina", 47109876, date(1996, 6, 14), "F", "1190123456", "1191234567", "A+", "Clinica Mayo SRL", "Receptor", "23", "30", "35", "44", "13", "17", ["riñón"], date(2023, 12, 11), "nefropatía", "estable")
                rpaciente20 = Receptor("Nicolás Vera", 47098765, date(1997, 2, 4), "M", "1191234567", "1192345678", "O-", "Hospital Samic Alem", "Receptor", "23", "31", "35", "44", "19", "10", ["hígado"], date(2024, 5, 9), "insuficiencia hepática", "estable")   
                return [dpaciente1, dpaciente2, dpaciente3, dpaciente4, dpaciente5, dpaciente6, dpaciente7, dpaciente8, dpaciente9, dpaciente10, dpaciente11, dpaciente12, rpaciente11, rpaciente12, rpaciente13, rpaciente14, rpaciente15, rpaciente16, rpaciente17, rpaciente18, rpaciente19, rpaciente20]

        def creacion_cirujanos_especialistas(self):
                        #Hospital Garrahan
                        especialista_garra_1 = Especialista("Juan Rios", "Hospital Garrahan", "gastroenterologo")
                        especialista_garra_2=Especialista("Camila Rios", "Hospital Garrahan", "pulmonar")
                        especialista_garra_3=Especialista("Manuela Alonso", "Hospital Garrahan", "pulmonar")
                        
                        #Hospital Italiano de La Plata
                        especialista_ita_1 = Especialista("Juan Rios", "Hospital Italiano de La Plata", "gastroenterologo")
                        especialista_ita_2 = Especialista("Matias Escobar ", "Hospital Italiano de La Plata", "cardiovascular")
                        especialista_ita_3 = Especialista ("Victoria Palacios", "Hospital Italiano de La Plata", "pulmonar")
                        especialista_ita_4 = Especialista ("Jose Ayala", "Hospital Italiano de La Plata", "traumatologo")
                        
                        #Hospital General de Niños Dr. R. Gutierrez
                        especialista_guti_1 = Especialista("Juan Nevada", "Hospital General de Niños Dr. R. Gutierrez", "gastroenterologo")
                        especialista_guti_2 = Especialista("Matias Mio", "Hospital General de Niños Dr. R. Gutierrez", "cardiovascular")
                        especialista_gut_3= Especialista ("Angeles Esperanza", "Hospital General de Niños Dr. R. Gutierrez", "pulmonar")
                        especialista_gut_4 = Especialista ("Josefina Clara", "Hospital General de Niños Dr. R. Gutierrez", "traumatologo")
                        
                        #Fundacion Favaloro
                        especialista_fava_1 = Especialista("Marcos Blanco", "Fundacion Favaloro", "gastroenterologo")
                        especialista_fava_2 = Especialista("Matias Sivan", "Fundacion Favaloro", "cardiovascular")
                        especialista_fava_3 = Especialista ("Angeles Ayala", "Fundacion Favaloro", "pulmonar")
                        especialista_fava_4 = Especialista ("Agustina Palacios", "Fundacion Favaloro", "traumatologo")
                        especialista_fava_5 = Especialista ("Pablo Agustin", "Fundacion Favaloro", "plastico")
                        
                        #Hospital Regional Rio Grande
                        especialista_rio_1 = Especialista("Marcos Rojo", "Hospital Regional Rio Grande", "gastroenterologo")
                        especialista_rio_2 = Especialista("Juan Lopez", "Hospital Regional Rio Grande", "cardiovascular")
                        especialista_rio_4 = Especialista ("Marcos Martinez", "Hospital Regional Rio Grande", "pulmonar")
                        especialista_rio_3 = Especialista ("Ramon Suar", "Hospital Regional Rio Grande", "traumatologo")
                        especialista_rio_5= Especialista ("Camila Agustin", "Hospital Regional Rio Grande", "plastico")
                        
                        #Hospital Dr. Clemente Alvarez
                        especialista_alvarez_2 = Especialista("Juan Alonso", "Hospital Dr. Clemente Alvarez", "cardiovascular")
                        especialista_alvarez_1 = Especialista ("Marcos Martinez", "Hospital Dr. Clemente Alvarez", "plastico")
                        
                        #Clinica Mayo SRL
                        especialista_mayo_1 = Especialista("Luciana Martino", "Hospital Regional Rio Grande", "gastroenterologo")
                        especialista_mayo_2 = Especialista("Francisca Suarez", "Hospital Regional Rio Grande", "cardiovascular")
                        especialista_mayo_3 = Especialista ("JUstina Apud", "Hospital Regional Rio Grande", "traumatologo")
                        
                        #Hospital Dr. Guillermo Rawson
                        especialista_rawson_1= Especialista("Juan Baron", "Hospital Dr. Guillermo Rawson", "traumatologo")
                        especialista_rawson_2= Especialista("Leon Blanco", "Hospital Dr. Guillermo Rawson", "traumatologo")
                        
                        #Hospital Papa Francisco
                        especialista_papa_1= Especialista("Geronimo Alias", "Hospital Papa Francisco", "plastico")
                        especialista_papa_2= Especialista("Azul Dinamarca", "Hospital Papa Francisco", "cardiovascular")
                        
                        #Hospital Samic Alem
                        especialista_alem_1= Especialista("Matias Juarez", "Hospital Samic Alem de autogestión nivel II", "pulmonar")
                        
                        #Hospital El Carmen
                        especialista_carmen_1=Especialista("Camila Amieva", "Hospital El Carmen", "plastico")
                        especialista_carmen_2=Especialista("Andres Alonso", "Hospital El Carmen", "plastico")
                        
                        #Hospital de Urgencias
                        especialista_urgencias= Especialista("Sebastian Juan", "Hospital de Urgencias", "cardiovascular")
                        especialista_urgencias_2= Especialista("Belen Esperanza", "Hospital de Urgencias", "traumatologo")
                        especialista_urgencias_3= Especialista("Martina Esperanza", "Hospital de Urgencias", "traumatologo")
                        especialista_urgencias_4= Especialista("Juliana Maricic", "Hospital de Urgencias", "pulmonar")
                        
                        #Hospital Zonal Alvear
                        especialista_alvear_1= Especialista("Tomas Cerada", "Hospital Zonal Alvear", "cardiovascular")
                        especialista_alvear_2= Especialista("Matias Nardio", "Hospital Zonal Alvear", "plastico")
                        
                        #Sanatorio Pasteur
                        especialista_pasteur_1=Especialista("Jazmin Rios", "Sanatorio Pasteur", "gastroenterologo")
                        especialista_pasteur_2=Especialista("Tomas Codega", "Sanatorio Pasteur", "gastroenterologo")
                        especialista_pasteur_3=Especialista("Tomas Niro", "Sanatorio Pasteur", "traumatologo")
                        
                        #Hospital Gral. de Agudos Carlos G. Durand
                        especialista_durand_1=Especialista("Francisco Perez", "Hospital Gral. de Agudos Carlos G. Durand", "gastroenterologo")
                        especialista_durand_2=Especialista("Marcos Cerasa", "Hospital Gral. de Agudos Carlos G. Durand", "traumatologo")
                        
                        #Hospital Universitario Austral
                        especialista_austral_1=Especialista("Pilar Magliano", "Hospital Universitario Austral", "cardiovascular")
                        especialista_austral_2=Especialista("Felipe Jurda", "Hospital Universitario Austral", "plastico")
                        
                        #Hospital El Cruce
                        especialista_cruce_1=Especialista("Adrián Lucero", "Hospital El Cruce", "traumatologo")
                        especialista_cruce_2=Especialista("Celeste Barrios", "Hospital El Cruce", "pulmonar")
                        especialista_cruce_3=Especialista("Francisco Magliano", "Hospital El Cruce", "pulmonar")
                        
                        
                        return [ especialista_garra_1,  especialista_garra_2,  especialista_garra_3,
                                especialista_ita_1, especialista_ita_2, especialista_ita_3, especialista_ita_4,
                                especialista_fava_1, especialista_fava_2, especialista_fava_3, especialista_fava_4, especialista_fava_5,
                                especialista_guti_1, especialista_guti_2, especialista_gut_3, especialista_gut_4, 
                                especialista_rio_1, especialista_rio_2, especialista_rio_3, especialista_rio_4, especialista_rio_5,
                                especialista_alvarez_2, especialista_alvarez_1,
                                especialista_mayo_1, especialista_mayo_2, especialista_mayo_3,
                                especialista_rawson_1, especialista_rawson_2,
                                especialista_papa_1, especialista_papa_2,
                                especialista_alem_1, especialista_carmen_1, especialista_carmen_2, 
                                especialista_austral_1, especialista_austral_2, especialista_alvear_2, especialista_alvear_1,
                                especialista_durand_1, especialista_durand_2, especialista_cruce_1, especialista_cruce_2, especialista_cruce_3, 
                                especialista_pasteur_1, especialista_pasteur_2, especialista_pasteur_3, especialista_urgencias, especialista_urgencias_2, especialista_urgencias_3, especialista_urgencias_4
                                ]

        def creacion_cirujanos_generales(self):
                #Hospital Regional Rio Grande
                general_rio_1=General("Maximo Priotti", "Hospital Regional Rio Grande")
                general_rio_2=General("Maximo Priotti", "Hospital Regional Rio Grande")

                #Hospital Dr. Clemente Alvarez
                general_alvarez_1=General("Fernando Kurd", "Hospital Dr. Clemente Alvarez")
                general_alvarez_2=General("Francisca Irlion", "Hospital Dr. Clemente Alvarez")

                #Hospital Dr. Guillermo Rawson
                general_rawson_1=General("Juan Martin Hugo", "Hospital Dr. Guillermo Rawson")
                general_rawson_2=General("Joaquin Zabala", "Hospital Dr. Guillermo Rawson")

                #Hospital Papa Francisco
                general_papa_1=General("Geronimo Alias", "Hospital Papa Francisco")
                general_papa_2=General("Azul Dinamarca", "Hospital Papa Francisco")

                #Hospital Samic Alem
                general_alem_1=General("Matias Suarez", "Hospital Samic Alem de autogestión nivel II")
                general_alem_2=General("Josefina Virgala", "Hospital Samic Alem de autogestión nivel II")

                #Hospital El Carmen
                general_carmen_1=General("Juana Perez", "Hospital El Carmen")
                general_carmen_2=General("Andres Fava", "Hospital El Carmen")

                #Hospital de Urgencias
                general_urgencias=General("Matias Rebord", "Hospital de Urgencias")
                general_urgencias_2=General("Matias Zabala", "Hospital de Urgencias")

                #Hospital Zonal Alvear
                general_alvear_1=General("Franco Cera", "Hospital Zonal Alvear")
                general_alvear_2=General("Matias Nardio", "Hospital Zonal Alvear")

                #Sanatorio Pasteur
                general_pasteur_1=General("Tomas Martinez", "Sanatorio Pasteur")
                general_pasteur_2=General("Pablo Codega", "Sanatorio Pasteur")

                #Hospital Gral. de Agudos Carlos G. Durand
                general_durand_1=General("Francisco Perez", "Hospital Gral. de Agudos Carlos G. Durand")
                general_durand_2=General("Marcos Cerasa", "Hospital Gral. de Agudos Carlos G. Durand")

                #Hospital Universitario Austral
                general_austral_1=General("Victoria Dimarco", "Hospital Universitario Austral")
                general_austral_2=General("Belen Jurda", "Hospital Universitario Austral")

                #Hospital El Cruce
                general_cruce_1=General("Franco Suarez", "Hospital El Cruce")
                general_cruce_2=General("Matias Juan Domingo", "Hospital El Cruce")

                #Hosipital Italiano de La Plata 
                general_italiano_1 = General("Juana Lara", "Hospital Italiano de La Plata")
                general_italiano_2 = General("Mateo Fava", "Hospital Italiano de La Plata")

                #Hospital General de Niños Dr. R. Gutierrez
                general3 = General("Juana", "Hospital General de Niños Dr. R. Gutierrez")
                general4= General("Mateo", "Hospital General de Niños Dr. R. Gutierrez")

                #Fundacion Favaloro
                general_favaloro_1 = General("Julia Lauro", "Fundacion Favaloro")
                general_favaloro2= General("Mateo Alonso", "Fundacion Favaloro")

                #Hospital Garrahan
                general_garrahan_1 = General("Juana Martinez", "Hospital Garrahan")
                general_garrahan_2=General("Martin Suarez", "Hospital Garrahan")

                #Clinica Mayo SRL
                general_mayo_1 = General("Juan Perez", "Clinica Mayo SRL")
                general_mayo_2=General("Zoe Fernandez", "Clinica Mayo SRL")

                return [general_rawson_1, general_rawson_2, general_alem_1, general_alem_2, general_carmen_1, general_carmen_2, general_urgencias, 
                        general_urgencias_2, general_alvear_1, general_alvear_2, general_pasteur_1, general_pasteur_2, 
                        general_durand_1, general_durand_2, general_austral_1, general_austral_2, general_cruce_1, general_cruce_2, 
                        general_italiano_1, general_italiano_2, general3, general4, general_favaloro_1, general_favaloro2, general_alvarez_1, general_alvarez_2,
                        general_garrahan_2, general_garrahan_1, general_mayo_1, general_mayo_2, general_papa_1, general_papa_2, general_rio_1, general_rio_2]

        def creacion_helicoptero(self):
                
                #Hospital Garrahan
                helicoptero_garr_1 = Helicoptero(150, "AA150AA", "Hospital Garrahan")
                helicoptero_garr_2 = Helicoptero(150, "AA151AA", "Hospital Garrahan")
                helicoptero_garr_3 = Helicoptero(180, "AA152AA", "Hospital Garrahan")
                helicoptero_garr_4 = Helicoptero(170, "AA153AA", "Hospital Garrahan")
                helicoptero_garr_5 = Helicoptero(150, "AA154AA", "Hospital Garrahan")
                
                #Hospital Italiano La Plata
                helicoptero_ita_1 = Helicoptero(130, "AA190AA", "Hospital Italiano de La Plata")

                #Hospital Gral. de Agudos Carlos G. Durand
                helicoptero_durand_1 = Helicoptero(150, "AA200AA", "Hospital Gral. de Agudos Carlos G. Durand")
                helicoptero_durand_2 = Helicoptero(150, "AA201AA", "Hospital Gral. de Agudos Carlos G. Durand")
                helicoptero_durand_3 = Helicoptero(150, "AA202AA", "Hospital Gral. de Agudos Carlos G. Durand")
                helicoptero_durand_4 = Helicoptero(150, "AA203AA", "Hospital Gral. de Agudos Carlos G. Durand")
                
                #Hospital de Urgencias
                helicoptero_urg_1 = Helicoptero(200, "AA300AA", "Hospital de Urgencias")
                helicoptero_urg_2 = Helicoptero(200, "AA301AA", "Hospital de Urgencias")
                helicoptero_urg_3 = Helicoptero(200, "AA302AA", "Hospital de Urgencias")
                helicoptero_urg_4 = Helicoptero(200, "AA303AA", "Hospital de Urgencias")
                helicoptero_urg_5 = Helicoptero(200, "AA304AA", "Hospital de Urgencias")
                helicoptero_urg_6 = Helicoptero(200, "AA305AA", "Hospital de Urgencias")
                helicoptero_urg_7 = Helicoptero(200, "AA306AA", "Hospital de Urgencias")
                helicoptero_urg_8 = Helicoptero(200, "AA307AA", "Hospital de Urgencias")
                
                return [helicoptero_garr_1, helicoptero_garr_2, helicoptero_garr_3, helicoptero_garr_4, helicoptero_garr_5, helicoptero_ita_1, 
                        helicoptero_durand_1, helicoptero_durand_2, helicoptero_durand_3, helicoptero_durand_4, 
                        helicoptero_urg_1, helicoptero_urg_2, helicoptero_urg_4, helicoptero_urg_5, helicoptero_urg_6, helicoptero_urg_7, helicoptero_urg_8, helicoptero_urg_3]

        def creacion_ambulancias(self):
                #Hospital Garrahan
                ambulancia_garr_1 = Ambulancia(80, "CPP189", "Hospital Garrahan")
                ambulancia_garr_2 = Ambulancia(90, "CPP190", "Hospital Garrahan")
                ambulancia_garr_3 = Ambulancia(105, "CPP191", "Hospital Garrahan")
                ambulancia_garr_4 = Ambulancia(80, "CPP192", "Hospital Garrahan")
                ambulancia_garr_5 = Ambulancia(120, "CPP193", "Hospital Garrahan")
                ambulancia_garr_6 = Ambulancia(150, "CPP194", "Hospital Garrahan")
                ambulancia_garr_7 = Ambulancia(130, "CPP195", "Hospital Garrahan")
                ambulancia_garr_8 = Ambulancia(99, "CPP196", "Hospital Garrahan")
                ambulancia_garr_9 = Ambulancia(140, "CPP197", "Hospital Garrahan")
                ambulancia_garr_10 = Ambulancia(110, "CPP198", "Hospital Garrahan")
                
                #Clinica Mayo SRL
                ambulancia_mayo_1 = Ambulancia(90, "CPP199", "Clinica Mayo SRL")
                ambulancia_mayo_2 = Ambulancia(115, "CPP200", "Clinica Mayo SRL")
                ambulancia_mayo_3 = Ambulancia(130, "CPP201", "Clinica Mayo SRL")
                ambulancia_mayo_4 = Ambulancia(85, "CPP202", "Clinica Mayo SRL")
                ambulancia_mayo_5 = Ambulancia(145, "CPP203", "Clinica Mayo SRL")
                
                #Fundacion Favaloro
                ambulancia_favaloro_1 = Ambulancia(100, "CPP204", "Fundacion Favaloro")
                ambulancia_favaloro_2 = Ambulancia(125, "CPP205", "Fundacion Favaloro")
                ambulancia_favaloro_3 = Ambulancia(90, "CPP206", "Fundacion Favaloro")
                ambulancia_favaloro_4 = Ambulancia(140, "CPP207", "Fundacion Favaloro")
                ambulancia_favaloro_5 = Ambulancia(110, "CPP208", "Fundacion Favaloro")
                
                #Hospital El Cruce
                ambulancia_elcruce_1 = Ambulancia(105, "CPP209", "Hospital El Cruce")
                ambulancia_elcruce_2 = Ambulancia(130, "CPP210", "Hospital El Cruce")
                ambulancia_elcruce_3 = Ambulancia(85, "CPP211", "Hospital El Cruce")
                ambulancia_elcruce_4 = Ambulancia(145, "CPP212", "Hospital El Cruce")
                ambulancia_elcruce_5 = Ambulancia(90, "CPP213", "Hospital El Cruce")
                
                #Sanatorio Pasteur
                ambulancia_pasteur_1 = Ambulancia(120, "CPP214", "Sanatorio Pasteur")
                ambulancia_pasteur_2 = Ambulancia(80, "CPP215", "Sanatorio Pasteur")
                ambulancia_pasteur_3 = Ambulancia(135, "CPP216", "Sanatorio Pasteur")
                ambulancia_pasteur_4 = Ambulancia(100, "CPP217", "Sanatorio Pasteur")
                ambulancia_pasteur_5 = Ambulancia(150, "CPP218", "Sanatorio Pasteur")
                
                #Hospital Zonal Alvear
                ambulancia_alvear_1 = Ambulancia(100, "CPP224", "Hospital Zonal Alvear")
                ambulancia_alvear_2 = Ambulancia(80, "CPP225", "Hospital Zonal Alvear")
                
                #Hospital Italiano La Plata
                ambulancia_ita_1 = Ambulancia(120, "CPP219", "Hospital Italiano de La Plata")
                ambulancia_ita_2 = Ambulancia(80, "CPP220", "Hospital Italiano de La Plata")
                ambulancia_ita_3 = Ambulancia(140, "CPP221", "Hospital Italiano de La Plata")
                
                #Hospital Universitario Austral
                ambulancia_austral_1=Ambulancia(120, "CPP200", "Hospital Universitario Austral")
                
                #Hospital General de Niños Dr. R. Gutierrez
                ambulancia_guti_1 = Ambulancia(80, "CPP230", "Hospital General de Niños Dr. R. Gutierrez")
                ambulancia_guti_2 = Ambulancia(80, "CPP231", "Hospital General de Niños Dr. R. Gutierrez")
                ambulancia_guti_3 = Ambulancia(80, "CPP232", "Hospital General de Niños Dr. R. Gutierrez")
                ambulancia_guti_4 = Ambulancia(80, "CPP233", "Hospital General de Niños Dr. R. Gutierrez")
                
                #Hospital Gral. de Agudos Carlos G. Durand
                ambulancia_durand_1 = Ambulancia(80, "CPP250", "Hospital Gral. de Agudos Carlos G. Durand")
                ambulancia_durand_2 = Ambulancia(80, "CPP251", "Hospital Gral. de Agudos Carlos G. Durand")
                ambulancia_durand_3 = Ambulancia(80, "CPP252", "Hospital Gral. de Agudos Carlos G. Durand")
                
                #Hospital Papa Francisco
                ambulancia_papa_1 = Ambulancia(95, "CPP229", "Hospital Papa Francisco")
                ambulancia_papa_2 = Ambulancia(120, "CPP238", "Hospital Papa Francisco")
                ambulancia_papa_3 = Ambulancia(140, "CPP237", "Hospital Papa Francisco")

                #Hospital Dr. Clemente Alvarez
                ambulancia_clemente_1 = Ambulancia(110, "CPP240", "Hospital Dr. Clemente Alvarez")
                ambulancia_clemente_2 = Ambulancia(85, "CPP241", "Hospital Dr. Clemente Alvarez")
                
                #Hospital Regional Rio Grande
                ambulancia_rio_1 = Ambulancia(105, "CPP260", "Hospital Regional Rio Grande")
                ambulancia_rio_2 = Ambulancia(130, "CPP261", "Hospital Regional Rio Grande")
                ambulancia_rio_3 = Ambulancia(89, "CPP262", "Hospital Regional Rio Grande")
                ambulancia_rio_4 = Ambulancia(150, "CPP263", "Hospital Regional Rio Grande")
                ambulancia_rio_5 = Ambulancia(102, "CPP264", "Hospital Regional Rio Grande")

                #Hospital Dr. Guillermo Rawson
                ambulancia_rawson_1 = Ambulancia(110, "CPP80", "Hospital Dr. Guillermo Rawson")
                ambulancia_rawson_2 = Ambulancia(90, "CPP281", "Hospital Dr. Guillermo Rawson")

                #Hospital Samic Alem
                ambulancia_alem_1 = Ambulancia(108, "CPP290", "Hospital Samic Alem de autogestión nivel II")
                
                #Hospital de Urgencias
                ambulancia_urgencias_1 = Ambulancia(150, "CPP291", "Hospital de Urgencias")
                ambulancia_urgencias_2 = Ambulancia(130, "CPP292", "Hospital de Urgencias")
                ambulancia_urgencias_3 = Ambulancia(90, "CPP293", "Hospital de Urgencias")
                ambulancia_urgencias_4 = Ambulancia(145, "CPP294", "Hospital de Urgencias")
                ambulancia_urgencias_5 = Ambulancia(100, "CPP295", "Hospital de Urgencias")
                ambulancia_urgencias_6 = Ambulancia(120, "CPP296", "Hospital de Urgencias")
                ambulancia_urgencias_7 = Ambulancia(130, "CPP297", "Hospital de Urgencias")
                ambulancia_urgencias_8 = Ambulancia(90, "CPP298", "Hospital de Urgencias")
                ambulancia_urgencias_9 = Ambulancia(145, "CPP299", "Hospital de Urgencias")
                
                return [ambulancia_garr_1, ambulancia_garr_2, ambulancia_garr_3, ambulancia_garr_4, ambulancia_garr_5, ambulancia_garr_6, ambulancia_garr_7, ambulancia_garr_8, ambulancia_garr_9, ambulancia_garr_10, 
                        ambulancia_mayo_1, ambulancia_mayo_2, ambulancia_mayo_3, ambulancia_mayo_4, ambulancia_mayo_5, ambulancia_rawson_1, ambulancia_rawson_2,
                        ambulancia_rio_1, ambulancia_rio_2, ambulancia_rio_3, ambulancia_rio_4, ambulancia_rio_5,
                        ambulancia_favaloro_1 , ambulancia_favaloro_2, ambulancia_favaloro_3, ambulancia_favaloro_4, ambulancia_favaloro_5,
                        ambulancia_elcruce_1, ambulancia_elcruce_2, ambulancia_elcruce_3, ambulancia_elcruce_4, ambulancia_elcruce_5,
                        ambulancia_papa_1, ambulancia_papa_2, ambulancia_papa_3, ambulancia_clemente_1, ambulancia_clemente_2, ambulancia_alem_1,
                        ambulancia_pasteur_1, ambulancia_pasteur_2, ambulancia_pasteur_3, ambulancia_pasteur_4, ambulancia_pasteur_5, 
                        ambulancia_alvear_1, ambulancia_alvear_2, ambulancia_austral_1, ambulancia_ita_1, ambulancia_ita_2, ambulancia_ita_3,
                        ambulancia_guti_1, ambulancia_guti_2, ambulancia_guti_3, ambulancia_guti_4, ambulancia_durand_1, ambulancia_durand_2, ambulancia_durand_3,
                        ambulancia_urgencias_1, ambulancia_urgencias_2, ambulancia_urgencias_3, ambulancia_urgencias_4, ambulancia_urgencias_5, ambulancia_urgencias_6,
                        ambulancia_urgencias_7, ambulancia_urgencias_8, ambulancia_urgencias_9]
                
        def creacion_aviones(self):

                #Hospital Garrahan
                avion_garr_1 = Avion(280, "AB466AP", "Hospital Garrahan")
                avion_garr_2 = Avion(290, "AB467AP", "Hospital Garrahan")
                avion_garr_3 = Avion(310, "AB468AP", "Hospital Garrahan")
                avion_garr_4 = Avion(250, "AB469AP", "Hospital Garrahan")
                
                #Clinica Mayo
                avion_mayo_1 = Avion(280, "AB450AP", "Clinica Mayo SRL") 
                
                #Fundacion Favaloro
                avion_fava_1 = Avion(250, "AB459AP", "Fundacion Favaloro")
                avion_fava_2 = Avion(290, "AB460AP", "Fundacion Favaloro")
                avion_fava_3 = Avion(285, "AB462AP", "Fundacion Favaloro")
                
                #Hospital General de Niños Dr. R. Gutierrez
                avion_guti_1 = Avion(280, "AB443AP", "Hospital General de Niños Dr. R. Gutierrez")
                avion_guti_2 = Avion(350, "AB442AP", "Hospital General de Niños Dr. R. Gutierrez")
                avion_guti_3 = Avion(240, "AB441AP", "Hospital General de Niños Dr. R. Gutierrez")
                avion_guti_4 = Avion(320, "AB440AP", "Hospital General de Niños Dr. R. Gutierrez")
                avion_guti_5 = Avion(295, "AB444AP", "Hospital General de Niños Dr. R. Gutierrez")
                
                #Hospital Italiano La Plata
                avion_ita_1 = Avion(310, "AB432AP", "Hospital Italiano de La Plata")



                #Hospital Gral. de Agudos Carlos G. Durand
                avion_durand_1 = Avion(290, "AB400AP", "Hospital Gral. de Agudos Carlos G. Durand")
                avion_durand_2 = Avion(270, "AB401AP", "Hospital Gral. de Agudos Carlos G. Durand")
                
                #Sanatorio Pasteur
                avion_pasteur = Avion(270, "AB478AP", "Sanatorio Pasteur")
                
                #Hospital Zonal Alvear
                avion_alvear = Avion(285, "AB416AP", "Hospital Zonal Alvear")
                
                return [avion_garr_1, avion_garr_2, avion_garr_3, avion_garr_4 , 
                        avion_mayo_1, avion_fava_1, avion_fava_2, avion_fava_3, 
                        avion_guti_1, avion_guti_2, avion_guti_3, avion_guti_4, avion_guti_5, 
                        avion_ita_1, avion_durand_1, avion_durand_2, avion_pasteur, avion_alvear]