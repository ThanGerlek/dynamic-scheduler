from Schedule import Schedule
from course_data import Course, Section
from preference_data import PreferenceSet, Rank


def generate_schedule(courses: list[Course], prefs: PreferenceSet) -> [int, list[Section]]:
    all_schedules = get_all_schedules(courses)
    clean_schedules = remove_conflicts(all_schedules)

    scored_combos = []
    for schedule in clean_schedules:
        rank: Rank = prefs.rank_schedule(schedule)
        if not rank.is_rejected():
            scored_combos.append((rank, schedule))

    return sorted(scored_combos, key=ranked_schedule_sort_key, reverse=True)


def ranked_schedule_sort_key(ranked_schedule: tuple[Rank, Schedule]) -> int:
    rank, _ = ranked_schedule
    return rank.value


def get_all_schedules(courses: list[Course]) -> list[Schedule]:
    section_combos: list[list[Section]] = []
    for course in courses:
        section_combos = add_course_to_combos(section_combos, course)
    return list(map(lambda combo: Schedule(combo), section_combos))


def add_course_to_combos(section_combos: list[list[Section]], course: Course) -> list[list[Section]]:
    if not section_combos:
        return [[section] for section in course.sections]
    return [section_combo + [section] for section_combo in section_combos for section in course.sections]


# TODO Make conflict-removal more efficient. It's probably quite wasteful as-is.


def remove_conflicts(schedules: list[Schedule]) -> list[Schedule]:
    clean_schedules: list[Schedule] = []
    for schedule in schedules:
        if not schedule.has_conflict():
            clean_schedules.append(schedule)
    return clean_schedules
