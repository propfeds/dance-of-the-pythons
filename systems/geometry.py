import math

def distance_chebyshev(x1, y1, x2, y2):
    return max(abs(x2-x1), abs(y2-y1))

def distance_euclidian(x1, y1, x2, y2):
    return math.sqrt(float((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)))