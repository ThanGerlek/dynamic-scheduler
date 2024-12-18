from course_data import Course
from fake_data import get_fake_course_data


def get_course_data(course_id: str) -> Course:
    return get_fake_course_data(course_id)
