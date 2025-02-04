# Reto_06

## Resumen de Excepciones en el Código

El Reto #01 maneja las siguientes excepciones:

### 1. **`ZeroDivisionError`**

   - En la operación de división (`/`), se utiliza un bloque `try-except` para capturar esta excepción.
   - Si ocurre, se lanza un mensaje de error personalizado: `"No se puede dividir por cero"`.

### 2. **`ValueError`**
   - En el bloque `match`, si la operación no coincide con ninguna de las opciones válidas, se lanza un `ValueError` con el mensaje: `"Operación no válida"`.
    
### 3. **`Exception`**
  - En el bloque principal `try-except`, se captura cualquier excepción que ocurra durante la ejecución del programa (por ejemplo, errores de entrada del usuario).
    - Se muestra un mensaje de error genérico con el contenido de la excepción.
   
   ```python

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




   ```

---

El Reto #02 maneja las siguientes excepciones: 
## 1. **Exception**

- Se usa un `try-except` general para capturar cualquier error inesperado en la ejecución del código.  
- Si ocurre una excepción en la entrada o en la función `palindromo()`, se imprime el mensaje de error correspondiente.  

   
```python
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
   ```
---
El Reto #03 maneja las siguientes excepciones: 
 
## 1. **`ValueError`**  
   - Se lanza manualmente con `raise ValueError("La lista debe contener solo números enteros")`.    

## 2. **`Exception`**  
   - Se usa un `try-except` general para capturar cualquier error inesperado en la ejecución del código.  
   - Si ocurre una excepción en la ejecución, se imprime el mensaje de error correspondiente.  


```python
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
   ```
---

El Reto #04 maneja las siguientes excepciones: 

## 1. **`ValueError`**  
   - Se lanza manualmente con `raise ValueError("La lista debe contener solo números enteros")`.  

## 2. **`IndexError`**  
   - Puede ocurrir si la lista `numeros` tiene un solo elemento o está vacía, ya que `numeros[i + 1]` intentaría acceder a un índice fuera del rango válido.  

## 3. **`Exception`**  
   - Se usa un `try-except` general para capturar cualquier error inesperado en la ejecución del código.  
   - Si ocurre una excepción, se imprime el mensaje de error correspondiente.  


```python

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



```
---
El Reto #05 maneja las siguientes excepciones:   

## 1. **`ValueError`**  
   - Se lanza manualmente con `raise ValueError("La lista debe contener solo palabras")`.  
   - También se lanza `ValueError` si la lista tiene menos de dos elementos, con el mensaje `"La lista debe contener al menos dos palabras"`.  

## 2. **`Exception`**  
   - Se usa un `try-except` general para capturar cualquier error inesperado en la ejecución del código.  
   - Si ocurre una excepción, se imprime el mensaje de error correspondiente.  


```python

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

```


 # Manejo de Excepciones en el Paquete `shape`


## Excepciones en el Módulo `main.py`

### 1. **Excepción: `ValueError` en `set_vertices`**
  - En el método `set_vertices`, se verifica que todos los argumentos sean objetos de tipo `Point`.
  - Si no lo son, se lanza un `ValueError` con el mensaje: `"Todos los vértices deben ser objetos de tipo Point."`.
  ```python
class Rectangle(Shape):
    def __init__(self, vertices: list, edges: list) -> None:
        """Inicializa un rectángulo con cuatro vértices y cuatro aristas."""
        super().__init__(is_regular=True)
        if len(vertices) == 4 and len(edges) == 4:
            self.set_vertices(*vertices)
            self.set_edges(*edges)
        else:
            raise ValueError("Un rectángulo debe tener 4 vértices y 4 aristas.")
  ```

### 2. **Excepción: `ValueError` en `set_edges`**

  - En el método `set_edges`, se verifica que todos los argumentos sean objetos de tipo `Line`.
  - Si no lo son, se lanza un `ValueError` con el mensaje: `"Todas las aristas deben ser objetos de tipo Line."`.

     ```python
    def set_edges(self, *args: Line) -> None:
        """Establece las aristas de la figura, verificando que sean válidas."""
        if all(isinstance(line, Line) for line in args):
            self._edges = list(args)
        else:
            raise ValueError("Todas las aristas deben ser objetos de tipo Line.")
     ```

### 3. **Excepción: `NotImplementedError` en `compute_area`**
- El método `compute_area` en la clase `Shape` está diseñado para ser implementado en subclases.
- Si no se implementa, se lanza un `NotImplementedError` con el mensaje: `"El método para calcular el área debe implementarse en las subclases."`.
     ```python
         def compute_area(self) -> float:
        """Calcula el área de la figura (debe ser implementado en subclases)."""
        raise NotImplementedError(
            "El método para calcular el área debe implementarse en las subclases.")
     ```



## Excepciones en la Clase `Line`

### 1. **Excepción: `ValueError` en `get_length`**
  - En el método `get_length`, se verifica que la longitud de la línea sea un valor positivo.
   - Si no lo es, se lanza un `ValueError` con el mensaje: `"La longitud de la línea no puede ser negativa."`.
     ```python
         def get_length(self) -> float:
        """Obtiene la longitud de la línea."""
        if self._length <= 0:
            raise ValueError("La longitud de la línea no puede ser negativa.")
        return self._length
     ```

---

## Ejemplo de Uso en `main.py`

El siguiente código en `main.py` muestra como se utiliza `try` y `except` para manejar los errores en el paquete `Shape`:

```python

try:
    # Create Point objects
    p1 = Point(0, 0)
    p2 = Point(4, 0)
    p3 = Point(4, 3)
    p4 = Point(0, 3)
    p5 = Point(0, 0)
    p6 = Point(4, 0)
    p7 = Point(2, 3)

    # Create Line objects
    l1 = Line(p1, p2)
    l2 = Line(p2, p3)
    l3 = Line(p3, p4)
    l4 = Line(p4, p1)
    l5 = Line(p5, p6)
    l6 = Line(p6, p7)
    l7 = Line(p7, p5)

    # Create Rectangle object
    rectangle = Rectangle(vertices=[p1, p2, p3, p4], edges=[l1, l2, l3, l4])
    print(f"Área del rectángulo: {rectangle.compute_area()}")
    print(f"Perímetro del rectángulo: {rectangle.compute_perimeter()}")

    # Create Square object
    square = Square(vertices=[p1, p2, p3, p4], edges=[l1, l2, l3, l4])
    print(f"Área del cuadrado: {square.compute_area()}")
    print(f"Perímetro del cuadrado: {square.compute_perimeter()}")

    # Create Triangle object
    triangle = Triangle(vertices=[p5, p6, p7], edges=[l5, l6, l7])
    print(f"Área del triángulo: {triangle.compute_area():.2f}") 
    print(f"Perímetro del triángulo: {triangle.compute_perimeter():.2f}")
except Exception as e:
    print(f"Error: {e}")
