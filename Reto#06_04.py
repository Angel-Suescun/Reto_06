def sumatoria_mayor(numeros: list) -> list:

    suma_mayor = 0
    numeros_mayor = []

    for i in range(len(numeros) - 1):
        suma = numeros[i] + numeros[i + 1]
        if suma > suma_mayor:
            suma_mayor = suma
            numeros_mayor = [numeros[i], numeros[i + 1], suma_mayor]

    return numeros_mayor

try:
    lista_numeros = [11, 22, 35, 39, 5, 5600, 71, 81, 99, 105, 110, 1]
    if all(isinstance(i, int) for i in lista_numeros):
        raise ValueError("La lista debe contener solo números enteros")
    if len(lista_numeros) < 2:
        raise IndexError("La lista debe contener al menos dos números")
    lista_mayor = sumatoria_mayor(lista_numeros)
    print(
        f"La suma entre dos números consecutivos de {lista_numeros} es: "
        f"{lista_mayor[0]} + {lista_mayor[1]} = {lista_mayor[2]}"
    )
except Exception as e:
    print(f"Error: {e}")


