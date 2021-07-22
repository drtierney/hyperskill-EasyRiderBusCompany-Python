import json
import re

all_keys = ['bus_id', 'stop_id', 'stop_name', 'next_stop', 'stop_type', 'a_time']
format_keys = ['stop_name', 'stop_type', 'a_time']
type_error_counter = dict.fromkeys(all_keys, 0)
format_error_counter = dict.fromkeys(format_keys, 0)
bus_id_values = {128, 256, 512}
stop_name_regex = r'[A-Z]\w+\s?\w+?\s(Road|Avenue|Boulevard|Street)$'
stop_type_values = {'S', 'O', 'F', ''}
a_time_regex = r"([01]\d|2[0-3]):([0-5]\d)$"
bus_lines = dict()

data = json.loads(input())
for entry in data:
    bus_id = entry['bus_id']
    stop_id = entry['stop_id']
    stop_name = entry['stop_name']
    next_stop = entry['next_stop']
    stop_type = entry['stop_type']
    a_time = entry['a_time']

    # Stage 1 - Type and Required
    if type(bus_id) != int:
        type_error_counter['bus_id'] += 1
    if type(stop_id) != int:
        type_error_counter['stop_id'] += 1
    if type(stop_name) != str:
        type_error_counter['stop_name'] += 1
    if type(next_stop) != int:
        type_error_counter['next_stop'] += 1
    if type(stop_type) != str:
        type_error_counter['stop_type'] += 1
    if type(a_time) != str:
        type_error_counter['a_time'] += 1

    # Stage 2 - Format
    if not re.match(stop_name_regex, stop_name):
        format_error_counter['stop_name'] += 1
    if entry['stop_type'] not in stop_type_values:
        format_error_counter['stop_type'] += 1
    if not re.match(a_time_regex, entry['a_time']):
        format_error_counter['a_time'] += 1

    # Stage 3 - Bus line info
    if bus_id in bus_lines.keys():
        bus_lines[bus_id] += 1
    else:
        bus_lines[bus_id] = 1

# type_error_count = sum(type_error_counter.values())
# print(f"Type and required field validations: {format_error_count} errors")
# for key in all_keys:
#    print(f"{key}: {format_error_counter[key]}")

# format_error_count = sum(format_error_counter.values())
# print(f"Format validations: {format_error_counter} errors")
# for key in format_keys:
#    print(f"{key}: {format_error_counter[key]}")

print("Line names and number of stops:")
for k in bus_lines:
    print(f"bus_id: {k}, stops: {bus_lines[k]}")
