class TimeTable:
    def __init__(self, days, slots_per_day) -> None:
        self.days = days
        self.slots_per_day = slots_per_day

    def get_total_slots(self):
        return self.days * self.slots_per_day
  
    
    def __repr__(self) -> str:
        return f"TimeTable[day :{self.days}, slot_per_day : {self.slots_per_day}]"