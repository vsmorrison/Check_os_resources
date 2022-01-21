import json


def save_statistics_to_file(stats, time):
    filepath = f'Process utilization{time.strftime("[%d-%m-%Y %H:%M:%S]")}.json'
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(stats, file)
