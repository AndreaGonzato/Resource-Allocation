from TimeTable import TimeTable

class Resource:
    def __init__(self, name, timetable) -> None:
        self.name = name
        self.timetable = timetable
        self.calendar = [[0 for _ in range(timetable.slots_per_day)] for _ in range(timetable.days)]
    
    def set_unavailability(self, day, slot_index):
        self.calendar[day][slot_index] = -1

    def print_calendar(self):
        # Print the 2D array
        first_line= "day\slot:"
        for i in range(self.timetable.slots_per_day):
            first_line += "\t"+str(i)
        print(first_line)

        day = 0
        for row in self.calendar:
            line = "day: "+str(day)+"\t"
            for slot in row:
                line+= "\t"+str(slot)
            print(line)
            day+=1
    
    def __repr__(self) -> str:
        return self.name
