class Point:
    def __init__(self, x: float, y: float):
        self._x = float(x)
        self._y = float(y)

    def compute_distance(self) -> float:
        return (self._x**2 + self._y**2) ** 0.5

    def get_x(self) -> float:
        return self._x

    def set_x(self, x: float) -> None:
        self._x = float(x)

    def get_y(self) -> float:
        return self._y

    def set_y(self, y: float) -> None:
        self._y = float(y)