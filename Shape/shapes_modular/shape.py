from .line import Line
from .point import Point

class Shape:
    def __init__(self, is_regular: bool = True) -> None:
        """Inicializa una figura geométrica con regularidad opcional."""
        self._is_regular = is_regular
        self._vertices = []
        self._edges = []

    def set_vertices(self, *args: Point) -> None:
        """Establece los vértices de la figura, verificando que sean válidos."""
        if all(isinstance(vertex, Point) for vertex in args):
            self._vertices = list(args)
        else:
            raise ValueError("Todos los vértices deben ser objetos de tipo Point.")

    def get_vertices(self) -> list:
        """Obtiene los vértices de la figura."""
        return self._vertices

    def set_edges(self, *args: Line) -> None:
        """Establece las aristas de la figura, verificando que sean válidas."""
        if all(isinstance(line, Line) for line in args):
            self._edges = list(args)
        else:
            raise ValueError("Todas las aristas deben ser objetos de tipo Line.")

    def get_edges(self) -> list:
        """Obtiene las aristas de la figura."""
        return self._edges

    def set_inner_angles(self, inner_angles: list = None) -> None:
        """
        Establece los ángulos interiores de la figura. 
        Se calculan automáticamente si es regular.
        """
        if self._is_regular:
            n = len(self._vertices)
            self._inner_angles = [(180 * (n - 2)) / n] * n
        else:
            print("La figura no es regular, los triángulos tiene funcion especial")

    def get_inner_angles(self) -> list:
        """Obtiene los ángulos interiores de la figura."""
        return self._inner_angles

    def compute_area(self) -> float:
        """Calcula el área de la figura (debe ser implementado en subclases)."""
        raise NotImplementedError(
            "El método para calcular el área debe implementarse en las subclases.")

    def compute_perimeter(self) -> float:
        """Calcula el perímetro de la figura como la suma de sus aristas."""
        return sum(edge.get_length() for edge in self._edges)
    
if __name__ == '__main__':
    p1 = Point(0, 0)
    p2 = Point(3, 0)
    p3 = Point(3, 4)
    p4 = Point(0, 4)
    l1 = Line(p1, p2)
    l2 = Line(p2, p3)
    l3 = Line(p3, p4)
    l4 = Line(p4, p1)
    r = Shape(is_regular=True)
    r.set_vertices(p1, p2, p3, p4)
    r.set_edges(l1, l2, l3, l4)
    print(r.compute_perimeter())  # 14.0
    r.set_inner_angles()
    print(r.get_inner_angles())  # [90.0, 90.0, 90.0, 90.0]

