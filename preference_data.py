from Schedule import Schedule
from course_data import Section
from time_data import TimeComparator


class Rank:
    def __init__(self, value=None):
        self.value = value

    def compose(self, other):
        if not isinstance(other, Rank):
            raise Exception("Invalid Rank.compose() call")
        if self.is_rejected() or other.is_rejected():
            return Rank()
        else:
            return Rank(other.value + self.value)

    def is_rejected(self) -> bool:
        return self.value is None


class Preference:
    def __init__(self, rank: Rank):
        self.rank = rank

    def rank_section(self, section: Section) -> Rank:
        if self.applies(section):
            return self.rank
        return Rank(0)

    def applies(self, section: Section) -> bool:
        raise Exception("Tried to call Preference.applies() when it has not been implemented")

    def describe(self) -> str:
        raise Exception("Tried to call Preference.describe() when it has not been implemented")


class PreferenceSet:
    def __init__(self):
        self.preferences: [Preference] = []

    def rank_schedule(self, sch: Schedule) -> Rank:
        rank = Rank(0)
        for pref in self.preferences:
            for section in sch.sections:
                new_rank = pref.rank_section(section)
                rank = rank.compose(new_rank)
        return rank

    def add(self, pref: Preference):
        self.preferences.append(pref)

    def clear(self):
        self.preferences = []


# Preference subclasses

# To add:
# FreeTimePreference(timeRange, rank)
# DurationPreference(duration, rank)
# ProfessorPreference(profName, rank)

class ProfessorPreference(Preference):
    def __init__(self, rank: Rank, professor: str):
        super().__init__(rank)
        self.professor = professor

    def applies(self, section: Section) -> bool:
        return section.professor == self.professor

    def describe(self) -> str:
        return f"Professor: {self.professor}, rank: {self.rank.value}"


class SectionStartPreference(Preference):
    def __init__(self, rank: Rank, time: int, comparator: TimeComparator):
        super().__init__(rank)
        self.time = time
        self.comparator = comparator

    def applies(self, section: Section) -> bool:
        return self.comparator.compare(self.time, section.time_range.start_time)

    def describe(self) -> str:
        return f"Start time {self.comparator.value} {self.time}, rank: {self.rank.value}"


class SectionEndPreference(Preference):
    def __init__(self, rank: Rank, time: int, comparator: TimeComparator):
        super().__init__(rank)
        self.time = time
        self.comparator = comparator

    def applies(self, section: Section) -> bool:
        return self.comparator.compare(self.time, section.time_range.end_time)

    def describe(self) -> str:
        return f"End time {self.comparator.value} {self.time}, rank: {self.rank.value}"
