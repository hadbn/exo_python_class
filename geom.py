import numpy as np

class Point:
    def __init__(self, x=None, y=None):
        if x is not None:
            self.x = float(x)
        else:
            self.x = None
        if y is not None:
            self.y = float(y)
        else:
            self.y=None

    def translate(self, Vect):
        if Vect is not None and Vect != Point():
            self += Vect

    def __eq__(self, Vect):
        return (self.x == Vect.x) and (self.y == Vect.y)

    def __iadd__(self, Vect):
        if isinstance(Vect, Point):
            self.x += Vect.x
            self.y += Vect.y
        else:
            raise NotImplementedError

    def dist(self, pt):
        if isinstance(pt, Point):
            return np.sqrt(np.pow(pt.x - self.x, 2)**2 + np.pow(pt.y - self.y, 2)**2)
        else:
            raise NotImplementedError

class Polygon:
    def __init__(self, list_pts=None):
        if list_pts is not None:
            self.list_pts = [Point(item[0], item[1]) for item in list_pts]
        else:
            self.list = []
    def __repr__(self):
        if self.list_pts is not None:
            return f"Polygone contenant {len(self.list_pts)} points"
        else:
            return "Polygone vide"
    def translate(self, Vect):
        for point in self.list_pts:
            point.translate(Vect)


class Circle(Polygon):
    def __init__(self, radius = None, center = None, nb = 100):
        self.center = center
        self.radius = radius
        if radius is None and center is None:
            super().__init__()
        else:
            if radius is None or center is None:
                raise ValueError
            Xs = np.cos(np.linspace(0, 2*np.pi, nb)) * radius
            Ys = np.sin(np.linspace(0, 2*np.pi, nb)) * radius
            super().__init__(list_pts=np.vstack((Xs,Ys)).T)
            self.translate(center)
    def __call__(self, pt):
        if self.center is not None :
            return bool(self.center.dist(pt) <= self.radius)