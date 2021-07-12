import json
import re

all_keys = ['bus_id', 'stop_id', 'stop_name', 'next_stop', 'stop_type', 'a_time']
error_counter = dict.fromkeys(all_keys, 0)
stop_name_regex = r'[A-Z]\w+\s?\w+?\s(Road|Avenue|Boulevard|Street)$'
stop_type_values = {'S', 'O', 'F', ''}
a_time_regex = r"([01]\d|2[0-3]):([0-5]\d)$"

data = json.loads(input())
for entry in data:
    if type(entry['bus_id']) != int:
        error_counter['bus_id'] += 1
    if type(entry['stop_id']) != int:
        error_counter['stop_id'] += 1
    if type(entry['stop_name']) != str or entry['stop_name'] == '':
        error_counter['stop_name'] += 1
    if type(entry['next_stop']) != int:
        error_counter['next_stop'] += 1
    if type(entry['stop_type']) != str or entry['stop_type'] not in stop_type_values:
        error_counter['stop_type'] += 1
    if type(entry['a_time']) != str or entry['stop_name'] == '':
        error_counter['a_time'] += 1

error_count = sum(error_counter.values())
print(f"Type and required field validations: {error_count} errors")
for key in all_keys:
    print(f"{key}: {error_counter[key]}")
