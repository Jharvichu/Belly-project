# src/belly.py
from src.clock import get_current_time


class Belly:
    def __init__(self, clock_service=None):
        self.pepinos_comidos = 0
        self.tiempo_esperado = 0
        self.min_pepinos = 10
        self.time = 0
        self.registro_tiempos = []
        self.clock_service = clock_service

    def reset(self):
        self.pepinos_comidos = 0
        self.tiempo_esperado = 0

    def comer(self, pepinos):
        if pepinos < 0:
            raise ValueError("No se puede comer una cantidad negativa de pepinos")
        elif pepinos > 100 and pepinos < 1000:
            raise ValueError("No se puede comer mucha cantidad de pepinos")
        print(f"He comido {pepinos} pepinos.")
        self.pepinos_comidos += pepinos
        if self.clock_service:
            self.registro_tiempos.append(self.clock_service())
            self.time = get_current_time()

    def esperar(self, tiempo_en_horas):
        if tiempo_en_horas > 0:
            self.tiempo_esperado += tiempo_en_horas

    def esta_gruñendo(self):
        # Verificar que ambas condiciones se cumplan correctamente:
        # Se han esperado al menos 1.5 horas Y se han comido más de 10 pepinos
        if self.tiempo_esperado >= 1.5 and self.pepinos_comidos > 10:
            return True
        return False

    def pepinos_restantes(self):
        restante = self.min_pepinos - self.pepinos_comidos
        return restante

    def darme_tiempo_comio(self):
        return self.time
