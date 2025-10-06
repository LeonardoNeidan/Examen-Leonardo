# clases/areas.py

class Areas:
    def calcular_area_triangulo(self, base, altura):
        return (base * altura) / 2

    def calcular_area_rectangulo(self, base, altura):
        return base * altura

    def leer_datos_triangulo(self):
        base = float(input("Introduce la base del triángulo: "))
        altura = float(input("Introduce la altura del triángulo: "))
        return base, altura

    def leer_datos_rectangulo(self):
        base = float(input("Introduce la base del rectángulo: "))
        altura = float(input("Introduce la altura del rectángulo: "))
        return base, altura
