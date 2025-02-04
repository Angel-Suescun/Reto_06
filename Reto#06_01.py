
def calculator(number1: int, number2: int, operation: str) -> float:
    match operation:
        case '+':
            return number1 + number2
        case '-':
            return number1 - number2
        case '*':
            return number1 * number2
        case '/':
            try:
                return number1 / number2
            except ZeroDivisionError:
                raise ZeroDivisionError("No se puede dividir por cero")
        case _:
            raise ValueError("Operación no válida")

try:
    number1 = int(input("Ingrese el primer número: "))
    number2 = int(input("Ingrese el segundo número: "))
    operation = input(
        "Ingrese la operación (Suma: +, Resta: -, Multiplicación: *, División: /): "
    )
    print(
            f"La operación {number1}{operation}{number2} da como resultado: "
            f"{calculator(number1, number2, operation)}"
        )
except Exception as e:
    print(f"Error: {e}")



