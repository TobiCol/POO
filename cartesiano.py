class Punto:
    def __init__(self, punto_x, punto_y):
        self.x: float = punto_x
        self.y: float = punto_y

    def mostrar_Puntos(self):
        print((self.x, self.y))

point = Punto(7,8)
point.mostrar_Puntos()
