import tkinter as tk
import requests

# Time zones
cities = {
    "Kolkata": "Asia/Kolkata",
    "London": "Europe/London",
    "New York": "America/New_York",
    "Tokyo": "Asia/Tokyo",
    "Sydney": "Australia/Sydney",
    "Dubai": "Asia/Dubai"
}

root = tk.Tk()
root.title("🌍 World Clock Dashboard")
root.geometry("500x400")
root.configure(bg="#1e1e1e")

title = tk.Label(
    root,
    text="WORLD CLOCK",
    font=("Arial", 22, "bold"),
    fg="white",
    bg="#1e1e1e"
)
title.pack(pady=15)

frames = {}
time_labels = {}

for city in cities:
    frame = tk.Frame(root, bg="#2b2b2b", padx=10, pady=10)
    frame.pack(pady=5, fill="x", padx=20)

    city_label = tk.Label(
        frame,
        text=city,
        font=("Arial", 14),
        fg="white",
        bg="#2b2b2b"
    )
    city_label.pack(side="left")

    time_label = tk.Label(
        frame,
        text="--:--:--",
        font=("Courier", 16, "bold"),
        fg="#00ff9c",
        bg="#2b2b2b"
    )
    time_label.pack(side="right")

    time_labels[city] = time_label


def update_time():
    for city, zone in cities.items():
        try:
            url = f"http://worldtimeapi.org/api/timezone/{zone}"
            data = requests.get(url).json()
            time_now = data["datetime"][11:19]
            time_labels[city].config(text=time_now)

        except:
            time_labels[city].config(text="Error")

    root.after(5000, update_time)


update_time()

root.mainloop()