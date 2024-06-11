import os
import webbrowser
import subprocess
from threading import Timer

def open_browser():
    webbrowser.open_new("http://127.0.0.1:8000/auth/login/")

if __name__ == "__main__":
    Timer(1, open_browser).start()

    subprocess.Popen(["python", "manage.py", "runserver"])