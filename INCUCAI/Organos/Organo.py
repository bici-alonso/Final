'''
Los órganos que se pueden donar son los siguientes: 
corazón, hígado, páncreas, huesos, riñón, pulmones, intestino, piel y córneas. 
Los órganos almacenan la fecha y hora de ablación (si todavía no corresponde, no recuerda ninguna fecha en particular).
'''

import unicodedata
from datetime import datetime, date, time

class Organo:
    # Lista base de órganos válidos (sin acentos)
    organos_validos = [
        "corazon", "higado", "pancreas", "huesos", "riñon",
        "pulmones", "intestino", "piel", "corneas"
    ]

    def __init__(self, tipo, fecha_ablacion=None, hora_ablacion=None):
        self.tipo = self.quitar_acentos(tipo.strip().lower())
        self.fecha_ablacion = fecha_ablacion
        self.hora_ablacion = hora_ablacion

        if self.tipo not in self.organos_validos:
            print(f" '{tipo}' no es un órgano válido.")
            print(f"Órganos válidos: {', '.join(self.organos_validos)}")
        else:
            print(f"✅ Órgano registrado:  🫀 🫁  {self.tipo.capitalize()} 🫀 🫁 ")

    def quitar_acentos(self, texto):
        return ''.join(
            c for c in unicodedata.normalize('NFD', texto)
            if unicodedata.category(c) != 'Mn'
        )

    def ingresar_datos_ablacion(self):
        fecha_str = input("Ingrese la fecha de ablación (YYYY-MM-DD): ")
        hora_str = input("Ingrese la hora de ablación (HH:MM:SS): ")

        try:
            fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()
            hora = datetime.strptime(hora_str, "%H:%M:%S").time()
            if datetime.combine(fecha, hora) > datetime.now():
                print("La fecha y hora no pueden estar en el futuro.")
                return
            self.fecha_ablacion = fecha
            self.hora_ablacion = hora
            print("Datos de ablación guardados correctamente.")
        except ValueError:
            print("Formato de fecha u hora incorrecto.")

    def mostrar_datos(self):
        print(f"\nÓrgano: {self.tipo.capitalize()}")
        if self.fecha_ablacion and self.hora_ablacion:
            print(f"Fecha de ablación: {self.fecha_ablacion}")
            print(f"Hora de ablación: {self.hora_ablacion}")
        else:
            print("No se ha registrado aún una fecha y hora de ablación.")

    def calcular_tiempo_transcurrido_hoy_ablacion(self):
        hora_actual=datetime.now()
        if not self.fecha_ablacion or not self.hora_ablacion:
            print("No hay fecha y hora registrada para calcular el tiempo.")
            return

        ablacion_datetime = datetime.combine(self.fecha_ablacion, self.hora_ablacion)
        diferencia = hora_actual - ablacion_datetime
        if diferencia.total_seconds() >= 0:
            print(f"Tiempo transcurrido desde la ablación: {diferencia} horas")
        else:
            print("La fecha de ablación está en el futuro.")



tipo = input("Ingrese el tipo de órgano: ")
organo = Organo(tipo)
if organo.tipo in Organo.organos_validos:
    organo.ingresar_datos_ablacion()
    organo.mostrar_datos()
    organo.calcular_tiempo_transcurrido_hoy_ablacion()
