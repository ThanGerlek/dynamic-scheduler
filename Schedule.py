from course_data import Section
from time_data import TimeRange


class Schedule:
    def __init__(self):
        self.sections: [Section] = []
        self.used_times: [TimeRange] = []

    def add_section(self, section: Section):
        self.sections.append(section)
        self.used_times.append(section.time_range)
