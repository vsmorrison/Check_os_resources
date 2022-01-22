import psutil
import resources_utilities
import argparse
import time
from datetime import datetime
import save_results
import execute_application


def main(cpu_interval, stat_interval, app_path):
    app_pid = execute_application.execute_app_macos(app_path)
    time.sleep(1)
    process = psutil.Process(app_pid)
    measures = []
    stats = {}
    launch_time = datetime.now().strftime("%d.%m.%Y %H-%M-%S")
    while True:
        timestamp = datetime.now()
        measure = resources_utilities.get_all_utilization(
            process, cpu_interval, timestamp, app_pid
        )
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
    parser.add_argument(
        'app_path', type=str, help='path to application to monitor'
    )
    args = parser.parse_args()
    try:
        main(args.cpu_interval, args.stats_frequency, args.app_path)
    except psutil.NoSuchProcess:
        print('Script execution stopped due to process stop')
    except psutil.AccessDenied:
        print('Give access to folder/file')
