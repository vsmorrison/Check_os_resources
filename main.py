import os
import psutil
import resources_utilities
import argparse
import time
from datetime import datetime
import save_results


def main(cpu_interval, stat_interval):
    process = psutil.Process()
    pid = os.getpid()
    while True:
        timestamp = datetime.now()
        cpu_usage = resources_utilities.get_cpu_usage_info(
            process, cpu_interval
        )
        memory_usage = resources_utilities.get_memory_usage_info(process)
        file_descriptors = resources_utilities.get_file_descriptors_info(process)
        stats = {
            'Date': timestamp.strftime("%d/%m/%Y, %H:%M:%S"),
            'Process ID': pid,
            'CPU Utilization': f'{cpu_usage}%',
            'Resident Set Size': memory_usage.rss,
            'Virtual Memory Size': memory_usage.vms,
            'File Descriptors': file_descriptors
        }
        save_results.save_statistics_to_file(stats)
        time.sleep(stat_interval)
        #delete
        print(stats)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'cpu_interval', type=float, default=0.1, help='interval for CPU check'
    )
    parser.add_argument(
        'stats_refresh_value', type=int, default=1, help='''
        new value for stats appears per entered value'''
    )
    args = parser.parse_args()
    main(args.cpu_interval, args.stats_refresh_value)
