import tkinter as tk
import pyttsx3
import time
from threading import Thread

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def check_reminder():
    while True:
        current_time = time.strftime("%H:%M")
        if current_time == entry_time.get():
            speak(f"It's time to take your medicine: {entry_medicine.get()}")
            reminder_label.config(text=f"Reminder: {entry_medicine.get()}")
            break
        time.sleep(30)

def set_reminder():
    Thread(target=check_reminder).start()
    reminder_label.config(text="Reminder set!")

# GUI
app = tk.Tk()
app.title("Medicine Reminder")
app.geometry("300x200")

tk.Label(app, text="Medicine Name").pack()
entry_medicine = tk.Entry(app)
entry_medicine.pack()

tk.Label(app, text="Time (HH:MM)").pack()
entry_time = tk.Entry(app)
entry_time.pack()

tk.Button(app, text="Set Reminder", command=set_reminder).pack(pady=10)
reminder_label = tk.Label(app, text="")
reminder_label.pack()

app.mainloop()
