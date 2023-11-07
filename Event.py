class Event:
    def __init__(self, name, resources) -> None:
        self.name = name
        self.resources = resources
    
    def add_resource(self, resource):
        self.resources.append(resource)


    