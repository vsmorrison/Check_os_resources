import subprocess
import platform


def execute_app_macos(app_path):
    parent = subprocess.Popen(['open', '-a', app_path])
    application_pid = parent.pid + 1
    return application_pid


def execute_app_linux(app_path):
    application = subprocess.Popen([app_path])
    application_pid = application.pid
    return application_pid


def check_platform():
    oper_system = platform.system()
    return oper_system


def execute_on_proper_os(app_path):
    oper_system = check_platform()
    if oper_system == 'Darwin':
        app_pid = execute_app_macos(app_path)
    elif oper_system == 'Linux':
        app_pid = execute_app_linux(app_path)
    return app_pid

