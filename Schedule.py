from course_data import Section
from time_data import TimeRange


class Schedule:
    def __init__(self):
        self.sections: [Section] = []
        self.used_times: [TimeRange] = []

    def add_section(self, section: Section):
        self.sections.append(section)
        self.used_times.append(section.time_range)

    def clear(self):
        self.sections = []
        self.used_times = []

    def display(self, indent: str = ""):
        if not self.sections:
            print("Schedule is currently empty.")
        for section in self.sections:
            print(indent + section.describe())
