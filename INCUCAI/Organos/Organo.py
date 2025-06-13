''' 
Los órganos que se pueden donar son los siguientes: 
corazón, hígado, páncreas, huesos, riñón, pulmones, intestino, piel y córneas. 
Los órganos almacenan la fecha y hora de ablación (si todavía no corresponde, no recuerda ninguna fecha en particular).
'''

import unicodedata
from datetime import datetime, timedelta

class Organo:
    #organos válidos (sin acentos)
    
    
    organos_validos = {
        "corazon": "corazón",
        "higado": "hígado",
        "pancreas": "páncreas",
        "huesos": "huesos",
        "riñon": "riñón",
        "rinon": "riñón",
        "rinion": "riñón",
        "pulmones": "pulmones",
        "pulmon": "pilmones",
        "intestino": "intestino",
        "piel": "piel",
        "corneas": "córneas"
    }
    
    
    #vida util de cada organo post ablacion
    
    tiempos_conservacion = {
        "corazon": 6, "higado": 12, "pancreas": 12, "huesos": 20, "riñon": 24, "rinon":24, "rinion":24,
        "pulmones": 6, "intestino": 12, "piel": 60, "corneas": 90
    }

    def __init__(self, tipo, fecha_ablacion=None, hora_ablacion=None):
        self.tipo = self.sacar_acentos(tipo.strip().lower())
        self.fecha_ablacion = fecha_ablacion
        self.hora_ablacion = hora_ablacion

        if self.tipo not in self.organos_validos:
            print(f"❌ '{tipo}' no es un órgano válido.")
            print(f"Órganos válidos: {', '.join(self.organos_validos)}")
            raise ValueError(f"'{tipo}' no es un órgano válido.")
        
        '''else:
            print(f"Órgano registrado: 🫀  {self.tipo.capitalize()} ")
            print(f"Tiempo máximo de conservación: {self.get_tiempo_conservacion()} horas")
        '''

    def sacar_acentos(self, texto):
        return ''.join(
            c for c in unicodedata.normalize('NFD', texto)
            if unicodedata.category(c) != 'Mn'
        )
    
    def get_tiempo_conservacion(self):
        #tiempo de conservación del organo en horas
        return self.tiempos_conservacion.get(self.tipo, 0)
    
    def set_ablacion_auto(self, fecha_ablacion, hora_ablacion):
        #establece la fecha y hora de ablación en automatico
        self.fecha_ablacion = fecha_ablacion
        self.hora_ablacion = hora_ablacion
        print(f"Ablación establecida a las {self.hora_ablacion}")
        
    def calcular_tiempo_transcurrido(self):
        #calcula el tiempo transcurrido desde la ablación en horas
        if not self.fecha_ablacion or not self.hora_ablacion:
            return None

        ablacion_datetime = datetime.combine(self.fecha_ablacion, self.hora_ablacion)
        diferencia = datetime.now() - ablacion_datetime
        
        if diferencia.total_seconds() >= 0:
            return diferencia.total_seconds() / 3600  # en horas
        else:
            return 0  # Si está en el futuro, retornar 0
    
    def calcular_tiempo_restante(self):
        """Calcula el tiempo restante antes de que el órgano se venza"""
        tiempo_transcurrido = self.calcular_tiempo_transcurrido()
        if tiempo_transcurrido is None:
            return None
            
        tiempo_maximo = self.get_tiempo_conservacion()
        tiempo_restante = tiempo_maximo - tiempo_transcurrido
        
        return max(0, tiempo_restante)  # No devolver valores negativos
    
    def es_viable_para_trasplante(self):
        if not self.fecha_ablacion or not self.hora_ablacion:
            return False
        tiempo_restante = self.calcular_tiempo_restante()
        return tiempo_restante is not None and tiempo_restante > 0

    def get_fecha_vencimiento(self):
        """retorna la fecha y hora límite para el trasplante"""
        if not self.fecha_ablacion or not self.hora_ablacion:
            return None
            
        ablacion_datetime = datetime.combine(self.fecha_ablacion, self.hora_ablacion)
        vencimiento = ablacion_datetime + timedelta(hours=self.get_tiempo_conservacion())
        return vencimiento

    def calcular_tiempo_transcurrido_hoy_ablacion(self):
        tiempo_transcurrido = self.calcular_tiempo_transcurrido()
        if tiempo_transcurrido is not None:
            print(f"Tiempo transcurrido desde la ablación: {tiempo_transcurrido:.2f} horas")
        else:
            print("No hay fecha y hora registrada para calcular el tiempo.")

    def mostrar_datos(self):
        """
        Muestra toda la información del órgano
        """
        
        print(f"\n----------------------------------------------------INFORMACIÓN DEL ÓRGANO----------------------------------------------------")
        print(f"Tipo: {self.tipo.capitalize()}")
        print(f"Tiempo máximo de conservación: {self.get_tiempo_conservacion()} horas")
        
        if self.fecha_ablacion and self.hora_ablacion:
            print(f"Fecha de ablación: {self.fecha_ablacion}")
            print(f"Hora de ablación: {self.hora_ablacion}")
            tiempo_transcurrido = self.calcular_tiempo_transcurrido()
            tiempo_restante = self.calcular_tiempo_restante()
            
            if tiempo_transcurrido is not None:
                print(f"\nTiempo transcurrido desde ablación: {tiempo_transcurrido:.0f} horas")
                if tiempo_restante is not None:
                    if tiempo_restante > 0:
                        print(f"⏳ Tiempo restante para trasplante: {tiempo_restante:.1f} horas")
                        print(f"Estado: VIABLE para trasplante")
                    else:
                        print("⚠️  ÓRGANO VENCIDO - Tiempo límite superado")
                        print("Estado: NO VIABLE para trasplante")
        else:
            print("No se ha registrado aún una fecha y hora de ablación.")

    def __str__(self):
        return self.organos_validos.get(self.tipo, self.tipo).capitalize()
