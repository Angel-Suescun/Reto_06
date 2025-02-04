
def anagrama(palabras: list) -> list:

    hay_anagrama = False
    lista_minuscula = [palabra.lower() for palabra in palabras]

    for i in range(len(lista_minuscula)):
        for j in range(i + 1, len(lista_minuscula)):
            if sorted(lista_minuscula[i]) == sorted(lista_minuscula[j]):
                print(f"{palabras[i]} y {palabras[j]} son anagramas")
                hay_anagrama = True

    if not hay_anagrama:
        print("No hay anagramas")
try:
    lista_palabras = ["amor", "roma", "perro"] 
    if all(isinstance(i, str) for i in lista_palabras):
        raise ValueError("La lista debe contener solo palabras")
    elif len(lista_palabras) < 2:
        raise ValueError("La lista debe contener al menos dos palabras")
    anagrama(lista_palabras)
except Exception as e:
    print(f"Error: {e}")
