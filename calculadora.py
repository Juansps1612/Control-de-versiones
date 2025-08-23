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

if __name__ == "__main__":
    print("Suma de 5 + 3 =", sumar(5, 3))
    print("Resta de 5 - 3 =", restar(5, 3))
    print("Multiplicación de 5 * 3 =", multiplicar(5, 3))
    print("División de 5 / 3 =", dividir(5, 3))
