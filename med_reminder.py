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
        for reminder in reminders[:]:  # Copy to avoid modifying while iterating
            if current_time == reminder[1]:
                speak(f"It's time to take your medicine: {reminder[0]}")
                reminder_label.config(text=f"Reminder: {reminder[0]} at {reminder[1]}")
                reminders.remove(reminder)
        time.sleep(30)

def set_reminder():
    medicine = dropdown.get()
    time_set = entry_time.get()
    if medicine and time_set:
        reminders.append((medicine, time_set))
        reminder_label.config(text=f"Reminder set for {medicine} at {time_set}")
        entry_time.delete(0, tk.END)

# GUI
app = tk.Tk()
app.title("Multiple Medicine Reminder")
app.geometry("350x300")

reminders = []  # To store all reminders

tk.Label(app, text="Select Medicine").pack()
medicine_list = ['Paracetamol', 'Ibuprofen', 'Aspirin', 'Vitamin C', 'Antibiotic']
dropdown = tk.StringVar()
dropdown.set(medicine_list[0])  # Default selection
medicine_menu = tk.OptionMenu(app, dropdown, *medicine_list)
medicine_menu.pack()

tk.Label(app, text="Time (HH:MM)").pack()
entry_time = tk.Entry(app)
entry_time.pack()

tk.Button(app, text="Set Reminder", command=set_reminder).pack(pady=10)
reminder_label = tk.Label(app, text="")
reminder_label.pack()

# Start background thread
Thread(target=check_reminder, daemon=True).start()

app.mainloop()
