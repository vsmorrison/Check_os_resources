def get_cpu_usage_info(process, cpu_interval):
    cpu_usage = process.cpu_percent(cpu_interval)
    return cpu_usage


def get_memory_usage_info(process):
    memory_usage = process.memory_info()
    return memory_usage


def get_file_descriptors_info(process):
    file_descriptors = process.num_fds()
    return file_descriptors


def get_all_utilization(process, cpu_interval, timestamp, pid):
    cpu_usage = get_cpu_usage_info(process, cpu_interval)
    memory_usage = get_memory_usage_info(process)
    file_descriptors = get_file_descriptors_info(process)
    measure = {
        'Date': timestamp.strftime("%d/%m/%Y, %H:%M:%S"),
        'Process ID': pid,
        'CPU Utilization': f'{cpu_usage}%',
        'Resident Set Size': memory_usage.rss,
        'Virtual Memory Size': memory_usage.vms,
        'File Descriptors': file_descriptors
    }
    return measure
