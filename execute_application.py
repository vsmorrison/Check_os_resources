import subprocess


def execute_app_macos(app_path):
    parent = subprocess.Popen(['open', '-a', app_path])
    application_pid = parent.pid + 1
    return application_pid
