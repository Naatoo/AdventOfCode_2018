import re
import operator
from datetime import datetime
from collections import defaultdict, Counter


def parse_input_file():
    with open('input.txt') as file:
        parsed_data = {}
        for line in file.readlines():
            timestamp, text = re.search('\[(.+)] (.+)', line.strip()).groups()
            parsed_data[datetime.strptime(timestamp, '%Y-%m-%d %H:%M')] = text
    return parsed_data


def get_sleep_intervals_and_days_to_guards_mapping(parsed_data: dict) -> (dict, dict):
    days_data = defaultdict(list)
    guards_days_mapping = {}
    index = None
    for timestamp, text in dict(sorted(parsed_data.items())).items():
        if "begins shift" in text or timestamp.hour == 23:
            index = text.split(" ")[1][1:]
        elif 'falls asleep' in text:
            day = timestamp.date()
            asleep_timestamp = timestamp
        elif 'wakes up' in text:
            guards_days_mapping[timestamp.date()] = index
            days_data[day].append((asleep_timestamp.minute, timestamp.minute - 1))
    return days_data, guards_days_mapping


def get_sleepy_guard_index(days_data: dict, guards_days_mapping: dict) -> int:
    guards_sleep = defaultdict(int)
    for date, sleep_data in days_data.items():
        for time_delta in sleep_data:
            minutes = time_delta[1] - time_delta[0]
            guards_sleep[guards_days_mapping[date]] += minutes
    return max(guards_sleep.items(), key=operator.itemgetter(1))[0]


def get_minutes_asleep_and_all_guards_sleep_data(days_data: dict, guards_days_mapping: dict) -> (int, dict):
    minutes = []
    all_guards_data = defaultdict(list)
    for date, sleep_data in days_data.items():
        for time_delta in sleep_data:
            for minute in range(time_delta[0], time_delta[1] + 1):
                all_guards_data[guards_days_mapping[date]].append(minute)
                if guards_days_mapping[date] == index:
                    minutes.append(minute)
    return Counter(minutes).most_common(1)[0][0] * int(index), all_guards_data


def get_result_2():
    final_data = {index: Counter(minutes) for index, minutes in all_guards_sleep_data.items()}
    final_occurrences = 0
    result = 0
    for index, (minute, occurrences) in {index: counter.most_common(1)[0]
                                         for index, counter in final_data.items()}.items():
        if occurrences > final_occurrences:
            result = int(index) * minute
    return result


parsed_data = parse_input_file()
days_sleep_intervals, guards_day_mapping = get_sleep_intervals_and_days_to_guards_mapping(parsed_data)
index = get_sleepy_guard_index(days_sleep_intervals, guards_day_mapping)
result1, all_guards_sleep_data = get_minutes_asleep_and_all_guards_sleep_data(days_sleep_intervals, guards_day_mapping)

print("PART 1:", result1)
print("PART 2:", get_result_2())
