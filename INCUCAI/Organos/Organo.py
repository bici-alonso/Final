''' 
Los órganos que se pueden donar son los siguientes: 
corazón, hígado, páncreas, huesos, riñón, pulmones, intestino, piel y córneas. 
Los órganos almacenan la fecha y hora de ablación (si todavía no corresponde, no recuerda ninguna fecha en particular).
'''

import unicodedata
from datetime import datetime, date, timedelta

class Organo:
    # Lista base de órganos válidos (sin acentos)
    organos_validos = [
        "corazon", "higado", "pancreas", "huesos", "riñon",
        "pulmones", "intestino", "piel", "corneas"
    ]
    
    # CORREGIDO: Cambié el nombre de tiempos_maximo a tiempos_conservacion
    # Y corregí el tiempo del riñón de 20 a 24 horas según tu especificación original
    tiempos_conservacion = {
        "corazon": 6, "higado": 12, "pancreas": 12, "huesos": 20, "riñon": 24,
        "pulmones": 6, "intestino": 12, "piel": 60, "corneas": 90
    }

    def __init__(self, tipo, fecha_ablacion=None, hora_ablacion=None):
        self.tipo = self.sacar_acentos(tipo.strip().lower())
        self.fecha_ablacion = fecha_ablacion
        self.hora_ablacion = hora_ablacion

        if self.tipo not in self.organos_validos:
            print(f"❌ '{tipo}' no es un órgano válido.")
            print(f"Órganos válidos: {', '.join(self.organos_validos)}")
        else:
            print(f"Órgano registrado: 🫀  {self.tipo.capitalize()} ")
            print(f"Tiempo máximo de conservación: {self.get_tiempo_conservacion()} horas")

    def sacar_acentos(self, texto):
        return ''.join(
            c for c in unicodedata.normalize('NFD', texto)
            if unicodedata.category(c) != 'Mn'
        )
    
    def get_tiempo_conservacion(self):
        #tiempo máximo de conservación del organo en horas"""
        return self.tiempos_conservacion.get(self.tipo, 0)

   
    def ingresar_datos_ablacion(self):
        """Permite ingresar manualmente los datos de ablación con validación continua"""
        print("\n📅 INGRESO DE DATOS DE ABLACIÓN")
        print("Formato de fecha: YYYY-MM-DD (ejemplo: 2024-12-25)")
        print("Formato de hora: HH:MM:SS (ejemplo: 14:30:00)")
        
        while True:
            try:
                fecha_str = input("\nIngrese la fecha de ablación (YYYY-MM-DD): ").strip()
                if not fecha_str:
                    print("❌ La fecha no puede estar vacía. Intente nuevamente.")
                    continue
                    
                fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()
                break
            except ValueError:
                print("❌ Formato de fecha incorrecto. Use el formato YYYY-MM-DD (ejemplo: 2024-12-25)")
                print("   Intente nuevamente...")
        
        while True:
            try:
                hora_str = input("Ingrese la hora de ablación (HH:MM:SS): ").strip()
                if not hora_str:
                    print("❌ La hora no puede estar vacía. Intente nuevamente.")
                    continue
                    
                hora = datetime.strptime(hora_str, "%H:%M:%S").time()
                
                # Verificar que no esté en el futuro
                fecha_hora_completa = datetime.combine(fecha, hora)
                if fecha_hora_completa > datetime.now():
                    print("⚠️ La fecha y hora no pueden estar en el futuro.")
                    print("   Ingrese una hora válida...")
                    continue
                    
                break
            except ValueError:
                print("❌ Formato de hora incorrecto. Use el formato HH:MM:SS (ejemplo: 14:30:00)")
                print("   Intente nuevamente...")
        
        self.fecha_ablacion = fecha
        self.hora_ablacion = hora
        print("✅ Datos de ablación guardados correctamente.")
        return True
    
    def set_ablacion_auto(self, fecha_ablacion, hora_ablacion):
        #establece la fecha y hora de ablación en automatico
        self.fecha_ablacion = fecha_ablacion
        self.hora_ablacion = hora_ablacion
        print("Ablación establecida")
        
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
        """Verifica si el órgano aún es viable para trasplante"""
        if not self.fecha_ablacion or not self.hora_ablacion:
            return False
            
        tiempo_restante = self.calcular_tiempo_restante()
        return tiempo_restante is not None and tiempo_restante > 0

    def get_fecha_vencimiento(self):
        """Retorna la fecha y hora límite para el trasplante"""
        if not self.fecha_ablacion or not self.hora_ablacion:
            return None
            
        ablacion_datetime = datetime.combine(self.fecha_ablacion, self.hora_ablacion)
        vencimiento = ablacion_datetime + timedelta(hours=self.get_tiempo_conservacion())
        return vencimiento

    def calcular_tiempo_transcurrido_hoy_ablacion(self):
        """Método para mantener compatibilidad con tu código original"""
        tiempo_transcurrido = self.calcular_tiempo_transcurrido()
        if tiempo_transcurrido is not None:
            print(f"Tiempo transcurrido desde la ablación: {tiempo_transcurrido:.2f} horas")
        else:
            print("No hay fecha y hora registrada para calcular el tiempo.")

    def mostrar_datos(self):
        """Muestra toda la información del órgano"""
        print(f"📋 INFORMACIÓN DEL ÓRGANO")
        print(f"Tipo: {self.tipo.capitalize()}")
        print(f"Tiempo máximo de conservación: {self.get_tiempo_conservacion()} horas")
        
        if self.fecha_ablacion and self.hora_ablacion:
            print(f"Fecha de ablación: {self.fecha_ablacion}")
            print(f"Hora de ablación: {self.hora_ablacion}")

            # Mostrar tiempo transcurrido y tiempo restante
            tiempo_transcurrido = self.calcular_tiempo_transcurrido()
            tiempo_restante = self.calcular_tiempo_restante()
            
            if tiempo_transcurrido is not None:
                print(f"⏱️  Tiempo transcurrido desde ablación: {tiempo_transcurrido:.0f} horas")
                if tiempo_restante is not None:
                    if tiempo_restante > 0:
                        print(f"⏳ Tiempo restante para trasplante: {tiempo_restante:.1f} horas")
                        print(f"Estado: VIABLE para trasplante")
                    else:
                        print("⚠️  ÓRGANO VENCIDO - Tiempo límite superado")
                        print("Estado: NO VIABLE para trasplante")
        else:
            print("No se ha registrado aún una fecha y hora de ablación.")



print("------------------------GESTIÓN DE ÓRGANOS--------------------------")
tipo = input("Ingrese el tipo de órgano: ")
organo = Organo(tipo)    
if organo.tipo in Organo.organos_validos:
    exito_ablacion = organo.ingresar_datos_ablacion()    
    
    if exito_ablacion:
        organo.mostrar_datos()    
        print(f"\n🔍 ¿Es viable para trasplante? {'✅ Sí' if organo.es_viable_para_trasplante() else '❌ No'}")
            
        if organo.get_fecha_vencimiento():
            print(f"📅 Fecha límite para trasplante: {organo.get_fecha_vencimiento()}")
        else:
            print("No se pudieron establecer correctamente los datos de ablación.")
    else:
        print("No se puede proceder con un órgano inválido.")