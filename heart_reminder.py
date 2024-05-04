import os
import time
import tkinter as tk
import tkinter.font as tkFont
import random
import sys
import winreg

start_dir = os.getcwd()
def cute_words():
    cute_words =[
    "Это напоминание о том что ты..\nЛучше всех!!!",
    "Это напоминание про то...\n Как сильно я тебя люблю!<3",
    "Это напоминание про то...\n Что ты самая красивая",
    "Это напоминание про то...\n Что ты самая лучшая девочка",
    "Это напоминание про то...\n Какая ты ахуенная!",
    "Это напоминание про то...\n Таких как ты нет!",
    "Это напоминание про то...\n Какие у тебя красивые глазки!",
    "Это напоминание про то...\n Какая у тебя красивая улыбка!"]
    cute_words = random.choice(cute_words)
    return cute_words

def add_to_startup():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Run', 0, winreg.KEY_WRITE)
    program_path = os.path.abspath(sys.argv[0])
    winreg.SetValueEx(key, 'Love_reminder', 0, winreg.REG_SZ, program_path)
    key.Close()

def get_elapsed_time():
    file_path = os.path.join(start_dir, "reminder")
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            elapsed_time = time.time() - float(f.read())
    else:
        elapsed_time = 0
    return elapsed_time

def write_current_time():
    file_path = os.path.join(start_dir, "reminder")
    if os.path.exists(file_path):
        os.remove(file_path)
    with open(file_path, "w") as f:
        f.write(str(time.time()))

def show_reminder_window():
    root = tk.Tk()
    root.title("Напоминание")
    root.geometry("450x140")
    root.resizable(width=False, height=False)
    root.configure(bg="#ffc0cb")
    font_style = tkFont.Font(family="Helvetica", size=14, weight="bold")
    font_style2 = tkFont.Font(family="Helvetica", size=8, weight="bold")
    image_path = 'heart.png'
    heart_image = tk.PhotoImage(file=image_path)
    tk.Label(root, image=heart_image, width=65, height=65, bg="#ffc0cb").grid(row=0, column=0, padx=20, pady=20)
    tk.Label(root, text=cute_words(), font=font_style, bg="#ffc0cb").grid(row=0, column=1, padx=(0,20), sticky="W")
    tk.Button(root, text="<3", font=font_style2, command=root.destroy, padx=10, bg="#FFC0CB").grid(row=1, column=1, padx=0, pady=0)
    root.mainloop()

if __name__ == "__main__":
    while True:
        elapsed_time = get_elapsed_time()
        if elapsed_time >= 36000:
            show_reminder_window()
            write_current_time()
        else:
            write_current_time()
        time.sleep(60)
