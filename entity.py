class Entity:
    def __init__(self, *components):
        self.components={}
        # Please: Append to the list of entities:
        # Entity.all_entities.append(self)
        for component in components:
            self.components[type(component)]=component