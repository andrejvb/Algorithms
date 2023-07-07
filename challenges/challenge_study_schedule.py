def study_schedule(permanence_period, target_time):
    best_time = 0

    if type(target_time) != int:
        return None
    
    for period in permanence_period:
        if type(period[0]) | type(period[1]) != int:
            return None
        if period[0] <= target_time <= period[1]:
            best_time += 1

    return best_time


    raise NotImplementedError

permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]

print(study_schedule(permanence_period, 5))
