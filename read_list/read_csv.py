#!/usr/bin/python3
"""
This files reads the .csv and puts the data into the dictionary
"""
from datetime import timedelta
import csv
import itertools

complete_mentors = []
uncomplete_mentors = []
mentorship_list = []

SESSION_GAP = 20
morning_start = timedelta(hours=8, minutes=00, seconds=00)
morning_end = timedelta(hours=12, minutes=00, seconds=00)
afternoon_start = timedelta(hours=13, minutes=00, seconds=00)
afternoon_end = timedelta(hours=18, minutes=00, seconds=00)


def read_csv_file(csv_name, complete_mentors, uncomplete_mentors):
    """
    This function reads the list of mentors and store the information into
    memory
    Args:
        @csv_name: path to the csv file
        @complete_mentors: list with the mentors with complete fields
        @uncomplete_mentors: list with the mentors with uncomplete fields

    Returns:
        Dictionary with the mentor name, time, and company values
    """
    with open(csv_name, encoding="utf-8") as csv_file:
        mentors = csv.reader(csv_file, delimiter=",")
        next(mentors)
        for mentor in mentors:
            mentorship = {}
            mentorship["name"] = mentor[0]
            mentorship["day"] = mentor[1].lower().strip()
            mentorship["time"] = mentor[2].lower().strip()
            mentorship["companies"] = [
                company for company in mentor[3:] if len(company) > 0]
            if (mentorship["day"].lower().strip(
            ) == "undefined" or mentorship["time"].lower().strip() == "undefined"):
                uncomplete_mentors.append(mentorship)
            else:
                complete_mentors.append(mentorship)


def generate_schedule(complete_mentors):
    """
    This generates the schedule having a predeterminated range
    Args:
        @complete_mentors: list with the mentors with complete fields

    Returns:
        Dictionary with all the dates
    """
    mentors = {}
    weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday"]
    time = ["am", "pm"]
    schedule = {}
    for x in itertools.product(weekdays, time):
        mentors["{}-{}".format(x[0], x[1])] = [
            mentor for mentor in complete_mentors if mentor["day"] == x[0] and mentor["time"] == x[1]]
        if x[1] == "pm":
            start = afternoon_start
            end = afternoon_end
        else:
            start = morning_start
            end = morning_end
        companies_placed = 0
        offset = 0
        counter = 1
        while (timedelta(minutes=offset) + start < end):
            if counter % 2 == 0:
                schedule["{}-{}-".format(x[0], x[1]) +
                         str(start +
                             timedelta(minutes=offset))] = ["BREAK TIME"]
            else:
                schedule["{}-{}-".format(x[0], x[1]) +
                         str(start +
                             timedelta(minutes=offset))] = []
            counter += 1
            offset += 20
    return schedule, mentors


def fill_schedule(schedule, mentors):
    """
    This fills the schedule taking in account all the mentors booked and
    companies
    Args:
        @mentors: list with the mentors with complete fields
        @schedule: schedule of the data

    Returns:
        Schedule without collapsing mentors or companies
    """
    weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday"]
    time = ["am", "pm"]
    for x in itertools.product(weekdays, time):
        for key, mentor in enumerate(mentors["{}-{}".format(x[0], x[1])]):
            if x[1] == "pm":
                start = afternoon_start
                end = afternoon_end
            else:
                start = morning_start
                end = morning_end
            companies_placed = 0
            next_iteration = 0
            companies_toplace = mentor["companies"][:]
            if (len(companies_toplace) >= 6):
                SESSION_GAP = 20
            else:
                SESSION_GAP = 40
            offset = 0
            while (companies_placed != len(mentor["companies"])):
                mentor_inschedule = [data for data in schedule["{}-{}-".format(x[0], x[1]) + str(
                    start + timedelta(minutes=offset))] if mentor["name"] in data]
                while (len(mentor_inschedule) > 0):
                    offset += SESSION_GAP
                    mentor_inschedule = [data for data in schedule["{}-{}-".format(x[0], x[1]) + str(
                        start + timedelta(minutes=offset))] if mentor["name"] in data]

                company_offset = 0
                company_inschedule = [data for data in schedule["{}-{}-".format(x[0], x[1]) + str(
                    start + timedelta(minutes=offset))] if companies_toplace[company_offset] in data]
                while (len(company_inschedule) > 0):
                    company_offset += 1
                    if company_offset < len(companies_toplace):
                        company_inschedule = [data for data in schedule["{}-{}-".format(x[0], x[1]) + str(
                            start + timedelta(minutes=offset))] if companies_toplace[company_offset] in data]
                    else:
                        offset += SESSION_GAP
                        next_iteration = 1
                        break
                if (next_iteration):
                    next_iteration = 0
                    continue
                schedule["{}-{}-".format(x[0], x[1]) + str(start + timedelta(minutes=offset))].append(
                    "Mentor: {} - Company: {}".format(mentor["name"], companies_toplace[company_offset]))
                companies_placed += 1
                companies_toplace.pop(company_offset)
    return schedule


def add_mentor(mentor, weekday, time, schedule):
    """
    This adds a new mentor into the schedule
    companies
    Args:
        @mentor: dictionary with the unbooked mentor data
        @weekday: day to book the mentor
        @time: time to book (PM or AM)
        @schedule: schedule of the data used

    Returns:
        Schedule with the new mentor
    """
    x = [weekday, time]
    if x[1] == "pm":
        start = afternoon_start
        end = afternoon_end
    else:
        start = morning_start
        end = morning_end
    companies_placed = 0
    next_iteration = 0
    companies_toplace = mentor["companies"][:]
    if (len(companies_toplace) >= 6):
        SESSION_GAP = 20
    else:
        SESSION_GAP = 40
    offset = 0
    while (companies_placed != len(mentor["companies"])):
        mentor_inschedule = [data for data in schedule["{}-{}-".format(x[0], x[1]) + str(
            start + timedelta(minutes=offset))] if mentor["name"] in data]
        while (len(mentor_inschedule) > 0):
            offset += SESSION_GAP
            mentor_inschedule = [data for data in schedule["{}-{}-".format(x[0], x[1]) + str(
                start + timedelta(minutes=offset))] if mentor["name"] in data]

        company_offset = 0
        company_inschedule = [data for data in schedule["{}-{}-".format(x[0], x[1]) + str(
            start + timedelta(minutes=offset))] if companies_toplace[company_offset] in data]
        while (len(company_inschedule) > 0):
            company_offset += 1
            if company_offset < len(companies_toplace):
                company_inschedule = [data for data in schedule["{}-{}-".format(x[0], x[1]) + str(
                    start + timedelta(minutes=offset))] if companies_toplace[company_offset] in data]
            else:
                offset += SESSION_GAP
                next_iteration = 1
                break
        if (next_iteration):
            next_iteration = 0
            continue
        schedule["{}-{}-".format(x[0], x[1]) + str(start + timedelta(minutes=offset))].append(
            "Mentor: {} - Company: {}".format(mentor["name"], companies_toplace[company_offset]))
        companies_placed += 1
        companies_toplace.pop(company_offset)
    return schedule


def main():
    complete_mentors = []
    uncomplete_mentors = []
    schedule = {}
    mentors = {}
    read_csv_file("techstar.csv", complete_mentors, uncomplete_mentors)
    schedule, mentors_bytime = generate_schedule(complete_mentors)
    schedule = fill_schedule(schedule, mentors_bytime)
    schedule = add_mentor(uncomplete_mentors[0], "monday", "am", schedule)
    print(schedule)


if __name__ == '__main__':
    main()
