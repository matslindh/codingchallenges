def most_asleep(f):
    current_guard = None
    fell_asleep = None
    sleep_time = {}

    for line in f.readlines():
        date, time, action, guard, *_ = line.strip().split(' ')
        time = int(time[3:5])

        if action == 'falls':
            fell_asleep = time
        elif action == 'wakes':
            if current_guard not in sleep_time:
                sleep_time[current_guard] = {
                    'total': 0,
                    'at': [0]*60
                }

            sleep_time[current_guard]['total'] += time - fell_asleep

            for t in range(fell_asleep, time):
                sleep_time[current_guard]['at'][t] += 1
        elif action == 'Guard':
            current_guard = int(guard[1:])

    max_guard_id = max(sleep_time, key=(lambda key: sleep_time[key]['total']))
    most_asleep_value = 0
    most_asleep_at = None
    most_asleep_at_guard_id = None

    for guard_id in sleep_time:
        my_max = max(sleep_time[guard_id]['at'])

        if my_max > most_asleep_value:
            most_asleep_value = my_max
            most_asleep_at = sleep_time[guard_id]['at'].index(most_asleep_value)
            most_asleep_at_guard_id = guard_id

    return max_guard_id * sleep_time[max_guard_id]['at'].index(max(sleep_time[max_guard_id]['at'])), \
        most_asleep_at_guard_id * most_asleep_at


def test_most_asleep():
    assert most_asleep(open('input/04.test')) == (240, 4455)


if __name__ == '__main__':
    print(most_asleep(open('input/04.sorted')))
