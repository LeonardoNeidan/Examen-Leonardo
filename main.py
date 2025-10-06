from clases.areas import Areas

def main():
    obj = Areas()

    print("=== CÁLCULO DE ÁREAS ===")
    print("1. Triángulo")
    print("2. Rectángulo")
    print("3. Círculo")
    opcion = input("Selecciona una opción (1-3): ")

    if opcion == "1":
        base, altura = obj.leer_datos_triangulo()
        area = obj.calcular_area_triangulo(base, altura)
        print(f"El área del triángulo es: {area:.2f}")

    elif opcion == "2":
        base, altura = obj.leer_datos_rectangulo()
        area = obj.calcular_area_rectangulo(base, altura)
        print(f"El área del rectángulo es: {area:.2f}")

    elif opcion == "3":
        radio = obj.leer_datos_circulo()
        area = obj.calcular_area_circulo(radio)
        print(f"El área del círculo es: {area:.2f}")

    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()
