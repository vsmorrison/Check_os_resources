def get_cpu_usage_info(process, cpu_interval):
    cpu_usage = process.cpu_percent(cpu_interval)
    return cpu_usage


def get_memory_usage_info(process):
    memory_usage = process.memory_info()
    return memory_usage


def get_file_descriptors_info(process):
    file_descriptors = process.num_fds()
    return file_descriptors
