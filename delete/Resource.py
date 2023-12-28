from TimeTable import TimeTable

class Resource:
    def __init__(self, name:str) -> None:
        self.name = name
    
    def init_calendar(self, days:int, slots:list) -> TimeTable:
        self.calendar = TimeTable(days=days, slots=slots)
        return self.calendar
    
    def get_calendar(self) -> TimeTable:
        return self.calendar

    
    def set_unavailability(self, day:int, slot_index:int)  -> None:
        self.calendar.set_unavailability(day, slot_index)


    def __repr__(self) -> str:
        return self.name
