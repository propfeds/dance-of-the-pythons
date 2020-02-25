from math import sqrt
from typing import Tuple

class Rectangle:
    def __init__(self, x1: int, y1: int, x2: int, y2: int):
        self.x1=x1
        self.x2=x2
        self.y1=y1
        self.y2=y2
        self.w=x2-x1+1
        self.h=y2-y1+1

    def centre(self) -> Tuple[int, int]:
        return (int((self.x1+self.x2)/2), int((self.y1+self.y2)/2))

    def intersect(self, ref: Rectangle) -> bool:
        return (self.x1<=ref.x2 and self.x2>=ref.x1 and self.y1<=ref.y2 and self.y2>=ref.y1)

def dist_chebyshev(x1: int, y1: int, x2: int, y2: int) -> int:
    return max(abs(x2-x1), abs(y2-y1))

def dist_euclidian(x1: int, y1: int, x2: int, y2: int) -> float:
    return sqrt(float((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)))