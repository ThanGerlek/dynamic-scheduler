class TimeRange:
    def __init__(self, start_time: int, end_time: int):
        self.start_time = start_time
        self.end_time = end_time

    def overlaps(self, other) -> bool:
        if not isinstance(other, TimeRange):
            raise Exception("Invalid TimeRange.overlaps() call")
        # xxx  |  xxx | xxxx |  xx
        #  xxx | xxx  |  xx  | xxxx
        return self.start_time < other.start_time < self.end_time or other.start_time < self.start_time < other.end_time

    def duration(self) -> int:
        return self.end_time - self.start_time

    def describe(self):
        return f"{self.start_time}-{self.end_time}"


class DaysOfWeek:
    def __init__(self, string_value: str):
        string_value = string_value.strip().upper()
        self.days = []
        for day in ["M", "T", "W", "Th", "F", "Sa", "Su"]:
            if day in string_value:
                self.days.append(day)
        if not self.days:
            raise Exception(f"Invalid DaysOfWeek value: '{string_value}'")

        self.days = string_value

    def overlaps(self, other):
        if not isinstance(other, DaysOfWeek):
            raise Exception("Invalid DaysOfWeek.overlaps() call")
        for day in self.days:
            if day in other.days:
                return True
        return False

    def describe(self):
        out = ""
        for day in self.days:
            out += day
        return out


class TimeComparator:
    def __init__(self, value: str):
        value = value.strip().upper()
        if value not in ["BEFORE", "AFTER", "EQUALS"]:
            raise Exception(f"Invalid TimeComparator value: '{value}'")
        self.value = value

    def compare(self, time1, time2):
        if self.value == "BEFORE":
            return time1 < time2
        elif self.value == "AFTER":
            return time1 > time2
        else:
            return time1 == time2
