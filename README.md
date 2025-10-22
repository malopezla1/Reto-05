# Reto-05
1. Crea un paquete con todo el código de la clase Shape , este ejercicio debe realizarse de dos maneras:
- Un módulo único dentro del paquete Shape
- Los módulos individuales que importan Shape heredan de él.

# Desarrollo
Devidi mi codigo para el ejercicio en clase sobre figuras y sus angulos, lo dividi en los siguientes modulos: __init__.py, Base.py, Line.py, Point.py, Rectangles.py, Triangles.py.

# Ejemplo de uso de main.py
```Python
from shape import Rectangle, Square, Isosceles, Equilateral, Scalene, Trirectangle

if __name__ == "__main__":
    figures = [
        Rectangle(4, 5),
        Square(4),
        Isosceles(5, 6),
        Equilateral(4),
        Scalene(4, 5, 6),
        Trirectangle(3, 4)
    ]

    for figure in figures:
        print(figure)
        print("-" * 40)
```
