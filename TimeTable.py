import pandas as pd

class TimeTable:
    def __init__(self, days:int, slots_per_day:int) -> None:
        self.days = days
        self.slots_per_day = slots_per_day
        self.time_slots = [[0 for j in range(days)] for i in range(slots_per_day)]
    
    def print_calendar(self) -> None:
        left_headers = []
        for i in range(self.slots_per_day):
            left_headers.append("slot: "+ str(i))
        
        df = pd.DataFrame(self.time_slots, index=left_headers)
        top_header = []
        for i in range(self.days):
            top_header.append("day:"+str(i))
            
        df.columns = top_header
        print(df.to_string(header=True))
        

    def set_unavailability(self, day:int, slot_index:int) -> None:
        self.time_slots[slot_index][day] = -1

    def set_value(self, value,  day:int, slot_index:int) -> None:
        self.time_slots[slot_index][day] = value

    def get_total_time_slots(self) -> int:
        return self.days * self.slots_per_day
  
    
    def __repr__(self) -> str:
        header = f"TimeTable{{day : {self.days}, slot_per_day : {self.slots_per_day} }}"
        time_slots = ""
        for row in self.time_slots:
            time_slots += str(row) + "\n"

        return header + "\n" + time_slots 
    
if __name__ == "__main__":
    t = TimeTable(5, 24)
    #print(t)

    t.print_calendar()