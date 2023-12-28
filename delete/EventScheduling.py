from delete.Event import Event
import pandas as pd

class EventScheduling:
    def __init__(self, event:Event, days:int) -> None:
        self.event = event
        self.days = days
        self.schedule = []
        for resource in self.event.resources:
            self.schedule.append(resource.get_calendar())

    
    def print(self) -> None:
        for resource in self.event.resources:
            resource.get_calendar().print_calendar()
        