def study_schedule(permanence_period, target_time):
    if type(target_time) != int:
        return None

    students  = 0

    for entry, exit in permanence_period:
        if type(entry) != int or type(exit) != int:
            return None

        if entry <= target_time <= exit:
            students += 1

    return students
