from DbDao import DbDao
from course_data import Course, ParticipationType, Section
from time_data import DaysOfWeek, TimeRange

db_dao = DbDao()


def insert_test_user_data():
    db_dao.create_user("john")


def get_fake_course_data(course_id: str) -> Course:
    #   345 789
    #  234   890
    # 12 45 78
    if course_id == "TEST 101":
        return Course(course_id, [
            Section(
                    course_id=course_id,
                    section_id="001",
                    time_range=TimeRange(3, 6),
                    days_of_week=DaysOfWeek("MWF"),
                    professor="Bob Ross",
                    participation_type=ParticipationType("IN PERSON")
            ),
            Section(
                    course_id=course_id,
                    section_id="002",
                    time_range=TimeRange(7, 10),
                    days_of_week=DaysOfWeek("MWF"),
                    professor="Bob Ross",
                    participation_type=ParticipationType("IN PERSON")
            )
        ])
    elif course_id == "TEST 102":
        #  234   890
        # 12 45 78
        return Course(course_id, [
            Section(
                    course_id=course_id,
                    section_id="001",
                    time_range=TimeRange(2, 5),
                    days_of_week=DaysOfWeek("MWF"),
                    professor="Bob Ross",
                    participation_type=ParticipationType("IN PERSON")
            ),
            Section(
                    course_id=course_id,
                    section_id="002",
                    time_range=TimeRange(8, 11),
                    days_of_week=DaysOfWeek("MWF"),
                    professor="Bob Ross",
                    participation_type=ParticipationType("IN PERSON")
            )
        ])
    elif course_id == "TEST 103":
        # 12 45 78
        return Course(course_id, [
            Section(
                    course_id=course_id,
                    section_id="001",
                    time_range=TimeRange(1, 3),
                    days_of_week=DaysOfWeek("MWF"),
                    professor="Bob Ross",
                    participation_type=ParticipationType("IN PERSON")
            ),
            Section(
                    course_id=course_id,
                    section_id="002",
                    time_range=TimeRange(4, 6),
                    days_of_week=DaysOfWeek("MWF"),
                    professor="Bob Ross",
                    participation_type=ParticipationType("IN PERSON")
            ),
            Section(
                    course_id=course_id,
                    section_id="003",
                    time_range=TimeRange(7, 9),
                    days_of_week=DaysOfWeek("MWF"),
                    professor="Bob Ross",
                    participation_type=ParticipationType("IN PERSON")
            )
        ])
    elif course_id == "TEST 201":
        return Course(course_id, [
            Section(
                    course_id=course_id,
                    section_id="001",
                    time_range=TimeRange(11, 12),
                    days_of_week=DaysOfWeek("MWF"),
                    professor="Bob Ross",
                    participation_type=ParticipationType("IN PERSON")
            ),
            Section(
                    course_id=course_id,
                    section_id="002",
                    time_range=TimeRange(7, 8),
                    days_of_week=DaysOfWeek("MWF"),
                    professor="James Bond",
                    participation_type=ParticipationType("IN PERSON")
            ),
            Section(
                    course_id=course_id,
                    section_id="002",
                    time_range=TimeRange(7, 8),
                    days_of_week=DaysOfWeek("MWF"),
                    professor="Bob Ross",
                    participation_type=ParticipationType("IN PERSON")
            ),
            Section(
                    course_id=course_id,
                    section_id="002",
                    time_range=TimeRange(9, 10),
                    days_of_week=DaysOfWeek("MWF"),
                    professor="James Bond",
                    participation_type=ParticipationType("IN PERSON")
            )
        ])
    elif course_id == "TEST 202":
        return Course(course_id, [
            Section(
                    course_id=course_id,
                    section_id="001",
                    time_range=TimeRange(2, 5),
                    days_of_week=DaysOfWeek("MWF"),
                    professor="Bob Ross",
                    participation_type=ParticipationType("IN PERSON")
            ),
            Section(
                    course_id=course_id,
                    section_id="002",
                    time_range=TimeRange(8, 11),
                    days_of_week=DaysOfWeek("MWF"),
                    professor="Bob Ross",
                    participation_type=ParticipationType("IN PERSON")
            )
        ])
    elif course_id == "TEST 203":
        return Course(course_id, [
            Section(
                    course_id=course_id,
                    section_id="001",
                    time_range=TimeRange(1, 3),
                    days_of_week=DaysOfWeek("MWF"),
                    professor="Bob Ross",
                    participation_type=ParticipationType("IN PERSON")
            ),
            Section(
                    course_id=course_id,
                    section_id="002",
                    time_range=TimeRange(4, 6),
                    days_of_week=DaysOfWeek("MWF"),
                    professor="Bob Ross",
                    participation_type=ParticipationType("IN PERSON")
            ),
            Section(
                    course_id=course_id,
                    section_id="003",
                    time_range=TimeRange(7, 9),
                    days_of_week=DaysOfWeek("MWF"),
                    professor="Bob Ross",
                    participation_type=ParticipationType("IN PERSON")
            )
        ])
