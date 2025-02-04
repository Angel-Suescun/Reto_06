def palindromo(palabra: str) -> bool:
    palabra = palabra.lower()
    for i in range(len(palabra) // 2):
        if palabra[i] != palabra[-i - 1]:
            return False
    return True

try:
    palabra = input("Ingrese una palabra: ")
    if palindromo(palabra):
        print(f"{palabra} es un palíndromo")
    else:
        print(f"{palabra} no es un palíndromo")
except Exception as e:
    print(f"Error: {e}")



