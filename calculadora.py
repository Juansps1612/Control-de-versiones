def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero")
    return a / b


def menu():
    while True:
        print("\n===== CALCULADORA =====")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "5":
            print("¡Hasta luego! 👋")
            break

        try:
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))

            if opcion == "1":
                print(f"Resultado: {sumar(a, b)}")
            elif opcion == "2":
                print(f"Resultado: {restar(a, b)}")
            elif opcion == "3":
                print(f"Resultado: {multiplicar(a, b)}")
            elif opcion == "4":
                try:
                    print(f"Resultado: {dividir(a, b)}")
                except ZeroDivisionError as e:
                    print(f"Error: {e}")
            else:
                print("Opción no válida. Intenta de nuevo.")

        except ValueError:
            print("⚠️ Error: Debes ingresar solo números.")


if __name__ == "__main__":
    menu()

