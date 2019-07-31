class Rectangle:
    def __init__(self, x, y, w, h):
        self.x1=x
        self.x2=x+w
        self.y1=y
        self.y2=y+h

    def centre(self):
        return (int((self.x1+self.x2)/2), int((self.y1+self.y2)/2))

    def intersect(self, ref):
        return (self.x1<=ref.x2 and self.x2>=ref.x1 and self.y1<=ref.y2 and self.y2>=ref.y1)