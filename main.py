import os
import psutil
import recources_utilities
import textwrap


def main():
    process = psutil.Process()
    while True:
        cpu_usage = recources_utilities.get_cpu_usage_info(process)
        memory_usage = recources_utilities.get_memory_usage_info(process)
        file_descriptors = recources_utilities.get_file_descriptors_info(process)
        text = f'''\
            CPU Load: {cpu_usage}
            Resident Set Size: {memory_usage.rss}
            Virtual Memory Size: {memory_usage.vms}
            File Descriptors: {file_descriptors}
            '''
        print(textwrap.dedent(text))


if __name__ == "__main__":
    main()
