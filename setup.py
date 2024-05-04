import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os", "tkinter", "tkinter.font", "time"], "include_files": ["heart.png"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="heart_reminder",
    version="1.0",
    description="A program that reminds you how much you are loved",
    options={"build_exe": build_exe_options},
    executables=[Executable("heart_reminder.py", base=base)]
)
