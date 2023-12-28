class Project:
    def __init__(self, id:int, requested_slot:int) -> None:
        self.id = id
        self.requested_slots:int = requested_slot
    
    def __repr__(self) -> str:
        return f"Project{{id : {self.id}, requested_slot : {self.requested_slot} }}"


    