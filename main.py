import local_storage
from DbDao import DbDao
from Schedule import Schedule
from course_data import Course
from preference_data import PreferenceSet, ProfessorPreference, Rank, SectionStartPreference
from schedule_generator import generate_schedule
from time_data import TimeComparator

dao = DbDao()


help_string = """Available Commands
help - Display this message.
quit - Exit the program.
generate - Generate a schedule using current preferences.
add pref - Add an additional preference.
clear prefs - Remove all preferences.
save prefs - Save the current preference list.
show prefs - Show the current preferences list.
add course - Add an additional course.
clear courses - Remove all courses from the course list.
show courses - Show the current course list.
show schedule - Show the currently saved schedule.
"""


def main():
    username = input("What's your username? ").strip()
    user_data = dao.get_user_data(username)
    if not user_data:
        dao.create_user(username)
        print(f"Welcome, {username}! You're all set up.")
    else:
        print(f"Welcome back, {username}!")

    prefs = PreferenceSet()
    courses: list[Course] = []
    schedule: Schedule or None = None

    while True:
        cmd = input(">>> ").strip().lower()
        if cmd == "help":
            print(help_string)
        elif cmd == "quit":
            print("Goodbye!")
            break
        elif cmd == "generate":
            new_sch = generate(courses, prefs)
            schedule = new_sch if new_sch else schedule
        elif cmd == "add pref":
            add_pref(prefs)
        elif cmd == "clear prefs":
            clear_prefs(prefs)
        elif cmd == "save prefs":
            save_prefs(prefs)
        elif cmd == "show prefs":
            show_prefs(prefs)
        elif cmd == "add course":
            add_course(courses)
        elif cmd == "clear courses":
            clear_courses(courses)
        elif cmd == "show courses":
            show_courses(courses)
        elif cmd == "show schedule":
            show_schedule(schedule)
        elif cmd == "test":
            test(courses, prefs)
        else:
            print('Unrecognized command. Enter "help" to see available commands.')


def parse_rank():
    raw_input = input("Score: ").strip().lower()
    if raw_input == "":
        return Rank()
    return Rank(raw_input)


def generate(courses: list[Course], prefs: PreferenceSet) -> Schedule or None:
    if not courses:
        print("Please add a course first.")
        return None

    print("Generating schedule...")
    schedules: list[Schedule] = generate_schedule(courses, prefs)
    if not schedules:
        print("Unable to resolve conflicts. Try relaxing constraints or removing courses.")
    print(f"Found {len(schedules)} possible schedules.")
    count = int(input("How many would you like to see? "))
    count = min(count, len(schedules))
    for i in range(count):
        rank, schedule = schedules[i]
        print(f"Schedule {i + 1}.    Score: {rank.value}")
        schedule.display("    ")
    save_index = int(input("Which would you like to save? Enter 0 for none. "))
    if save_index > 0:
        _, sch = schedules[save_index - 1]
        print("Saved.")
        return sch
    return None


def add_pref(prefs: PreferenceSet):
    cmd = input("What type: prof, start, or end? ").strip().lower()
    rank = parse_rank()
    if cmd == "prof":
        professor = input("Prof's name: ").strip().lower()
        pref = ProfessorPreference(rank, professor)
    elif cmd == "start":
        time = int(input("Start time boundary: ").strip())
        comparator = TimeComparator(input("Comparison: "))
        pref = SectionStartPreference(rank, time, comparator)
    elif cmd == "end":
        time = int(input("End time boundary: ").strip())
        comparator = TimeComparator(input("Comparison: "))
        pref = SectionStartPreference(rank, time, comparator)
    else:
        print("Unrecognized command. Please try again.")
        return
    prefs.add(pref)
    print(f"Added preference: {pref.describe()}")


def clear_prefs(prefs: PreferenceSet):
    prefs.clear()
    print("Cleared all preferences.")


def save_prefs(prefs: PreferenceSet):
    print("save_prefs() is unimplemented")


def show_prefs(prefs: PreferenceSet):
    if not prefs.preferences:
        print("There are no preferences currently defined.")
    else:
        print("Preferences")
        for pref in prefs.preferences:
            print(f"    {pref.describe()}")


def add_course(courses: list[Course]):
    course_id = input("Course ID: ")
    course: Course = local_storage.get_course_data(course_id)
    courses.append(course)
    print(f"Added course {course_id} to the selected courses list.")


def clear_courses(courses: list[Course]):
    courses.clear()
    print("Cleared currently selected courses.")


def show_courses(courses: [Course]):
    if not courses:
        print("There are no courses currently selected.")
    else:
        print("Courses")
        for course in courses:
            print(f"    {course.describe()}")


def show_schedule(schedule: Schedule):
    if schedule:
        schedule.display()
    else:
        print("No schedule is selected currently.")


def test(sch, prefs):
    pass


if __name__ == '__main__':
    main()
