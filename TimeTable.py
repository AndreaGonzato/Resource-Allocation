import pandas as pd

class TimeTable:
    def __init__(self, days:int, slots:list) -> None:
        self.days = days
        self.slots = slots
        self.slots_per_day = len(slots)
        self.time_slots = [[0 for j in range(days)] for i in range(self.slots_per_day)]
    
    def print_calendar(self) -> None:        
        df = pd.DataFrame(self.time_slots, index=self.slots)
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
    
    def __getitem__(self, indices):
        # Assuming indices is a tuple (i, j) for a 2D object
        i, j = indices
        # Define how to access elements using two indices
        return self.time_slots[i][j]

    
if __name__ == "__main__":
    t = TimeTable(5, [8, 9, 10, 11, 12, 13, 14, 15, 16, 17])
    #print(t)

    t.set_value(3, 1, 2)

    t.print_calendar()

    print(t[2, 1])