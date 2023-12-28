from Person import Person
from Resource import Resource

class Event:
    def __init__(self, name, responsible:Person, resources:list[Resource], requested_hours, start_day:int = 0) -> None:
        self.name = name
        self.responsible = responsible
        self.resources = resources
    
    def add_resource(self, resource):
        self.resources.append(resource)
    
    def __repr__(self) -> str:
        f"Event{{responsible : {self.responsible}, name : {self.name} }}"


    