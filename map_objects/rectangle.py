class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1=x1
        self.x2=x2
        self.y1=y1
        self.y2=y2

    def centre(self):
        return (int((self.x1+self.x2)/2), int((self.y1+self.y2)/2))

    def intersect(self, ref):
        return (self.x1<=ref.x2 and self.x2>=ref.x1 and self.y1<=ref.y2 and self.y2>=ref.y1)