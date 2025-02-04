


def primos(numero: list) -> list:
    primos = []

    for i in numero:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primos.append(i)

    if not primos:
        return "No hay números primos en la lista"

    if 1 in numero:
        primos.remove(1)  # El 1 no se considera primo

    return primos

try:
    lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    if all(isinstance(i, int) for i in lista_numeros):
        raise ValueError("La lista debe contener solo números enteros")
    primos_en_lista = primos(lista_numeros)
    print(f"Los números primos de la lista {lista_numeros} son: {primos_en_lista}")
except Exception as e:
    print(f"Error: {e}")

