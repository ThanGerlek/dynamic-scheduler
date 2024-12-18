from time_data import DaysOfWeek, TimeRange


class ParticipationType:
    def __init__(self, value: str):
        value = value.strip().upper()
        if value not in ["IN PERSON", "REMOTE", "PARTIAL"]:
            raise Exception(f"Invalid ParticipationType: '{value}'")


class Section:
    def __init__(self, course_id: str, section_id: str, time_range: TimeRange, days_of_week: DaysOfWeek, professor: str,
                 participation_type: ParticipationType):
        self.section_id = section_id
        self.course_id = course_id
        self.time_range = time_range
        self.daysOfWeek = days_of_week
        self.professor = professor
        self.participation_type = participation_type

    def describe(self):
        return f"{self.course_id} {self.section_id}, {self.daysOfWeek.describe()} {self.time_range.describe()}, {self.professor}"


class Course:
    def __init__(self, course_id: str, sections: [Section]):
        self.course_id = course_id
        self.sections = sections

    def describe(self):
        out = self.course_id + "  [ "
        for section in self.sections:
            out += section.section_id + " "
        return out + "]"
