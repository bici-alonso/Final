'''
Los órganos que se pueden donar son los siguientes: corazón, hígado, páncreas, huesos, riñón, pulmones,
intestino, piel y córneas. 
Además, los órganos almacenan la fecha y hora de ablación (si todavía no
corresponde simplemente no recuerda ninguna fecha en particular).




'''



from datetime import datetime, date, time


class Organo ():
    def __init__ (self, tipo, fecha_ablacion=None, hora_ablacion=None):
        self.tipo = tipo
        self.fecha_ablacion = fecha_ablacion
        self.hora_ablacion = hora_ablacion
        
    def ingresar_datos_ablacion(self):
        fecha_str = input("Ingrese la fecha de ablación (YYYY-MM-DD): ")
        hora_str = input("Ingrese la hora de ablación (HH:MM:SS): ")

        try:
            self.fecha_ablacion = datetime.strptime(fecha_str, "%Y-%m-%d").date()
            self.hora_ablacion = datetime.strptime(hora_str, "%H:%M:%S").time()
            print("Datos de ablación guardados correctamente.")
        except ValueError:
            print("Formato de fecha u hora incorrecto.")
        
        
    def mostrar_datos(self):
        if self.fecha_ablacion and self.hora_ablacion:
            print(f"\nÓrgano: {self.tipo}")
            print(f"Fecha de ablación: {self.fecha_ablacion}")
            print(f"Hora de ablación: {self.hora_ablacion}")
        else:
            print("No se ha registrado aún una fecha y hora de ablación.")
        
        
        
        
        '''
        now = datetime.now()
        # convert to string
        date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
        print('DateTime String:', date_time_str)

        '''

        
    def calcular_tiempo_transcurrido(self):
        if not self.fecha_ablacion or not self.hora_ablacion:
            print("No hay fecha y hora registrada para calcular el tiempo.")
            return

        ablacion_datetime = datetime.combine(self.fecha_ablacion, self.hora_ablacion)
        ahora = datetime.now()
        diferencia = ahora - ablacion_datetime

        if diferencia.total_seconds() >= 0:
            print(f"Tiempo transcurrido desde la ablación: {diferencia}")
        else:
            print("La fecha de ablación está en el futuro.")
    
    
        '''
    
        
# Obtener la fecha y hora actual
hora_actual = datetime.datetime.now()

# Crear un objeto datetime para una fecha específica
fecha_deseada = datetime.datetime(2025, 5, 20, 10, 0, 0)  # Año, Mes, Día, Hora, Minuto, Segundo

# Comparar
if fecha_deseada > hora_actual:
    print("La fecha deseada es en el futuro.")
elif fecha_deseada < hora_actual:
    print("La fecha deseada ya ha pasado.")
else:
    print("La fecha deseada es la misma que la fecha actual.")
        
        '''
        
organo = Organo("corazón")
organo.ingresar_datos_ablacion()
organo.mostrar_datos()
organo.calcular_tiempo_transcurrido() 