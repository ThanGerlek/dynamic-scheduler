from course_data import Section
from time_data import TimeRange


class Schedule:
    def __init__(self, sections=None):
        self.sections: [Section] = sections if sections else []
        self.used_times: [TimeRange] = []

    def add_section(self, section: Section):
        self.sections.append(section)
        self.used_times.append(section.time_range)

    def clear(self):
        self.sections = []
        self.used_times = []

    def has_conflict(self) -> bool:
        for i in range(len(self.sections)):
            for j in range(i + 1, len(self.sections)):
                range1 = self.sections[i].time_range
                range2 = self.sections[j].time_range
                if range1.overlaps(range2):
                    return True
        return False

    def display(self, indent: str = ""):
        if not self.sections:
            print("Schedule is currently empty.")
        for section in self.sections:
            print(indent + section.describe())
