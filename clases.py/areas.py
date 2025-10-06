import math

class Areas:
    def calcular_area_triangulo(self, base, altura):
        return (base * altura) / 2

    def calcular_area_rectangulo(self, base, altura):
        return base * altura

    def calcular_area_circulo(self, radio):
        return math.pi * (radio ** 2)

    def leer_datos_triangulo(self):
        base = float(input("Introduce la base del triángulo: "))
        altura = float(input("Introduce la altura del triángulo: "))
        return base, altura

    def leer_datos_rectangulo(self):
        base = float(input("Introduce la base del rectángulo: "))
        altura = float(input("Introduce la altura del rectángulo: "))
        return base, altura

    def leer_datos_circulo(self):
        radio = float(input("Introduce el radio del círculo: "))
        return radio
