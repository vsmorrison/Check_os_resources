import subprocess


def execute_app(app_path):
    application = subprocess.Popen(['open', app_path], shell=False)
    return application.pid
