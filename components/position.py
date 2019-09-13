class Position:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    
    def displace(self, dx, dy):
        self.x+=dx
        self.y+=dy

    def swap(self, target_entity):
        x_temp=self.x
        y_temp=self.y
        self.x=target_entity.components[Position].x
        self.y=target_entity.components[Position].y
        target_entity.components[Position].x=x_temp
        target_entity.components[Position].y=y_temp