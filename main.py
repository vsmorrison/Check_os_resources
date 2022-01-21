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
    measures = []
    stats = {}
    launch_time = datetime.now()
    while True:
        timestamp = datetime.now()
        cpu_usage = resources_utilities.get_cpu_usage_info(
            process, cpu_interval
        )
        memory_usage = resources_utilities.get_memory_usage_info(process)
        file_descriptors = resources_utilities.get_file_descriptors_info(process)
        measure = {
            'Date': timestamp.strftime("%d/%m/%Y, %H:%M:%S"),
            'Process ID': pid,
            'CPU Utilization': f'{cpu_usage}%',
            'Resident Set Size': memory_usage.rss,
            'Virtual Memory Size': memory_usage.vms,
            'File Descriptors': file_descriptors
        }
        measures.append(measure)
        stats["resource_measures"] = measures
        save_results.save_statistics_to_file(stats, launch_time)
        time.sleep(stat_interval)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'cpu_interval', type=float, help='interval for CPU check')
    parser.add_argument(
        'stats_frequency', type=int, help='''
        frequency in seconds for new measure to appear'''
    )
    args = parser.parse_args()
    main(args.cpu_interval, args.stats_frequency)
