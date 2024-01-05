import pyautogui
import time
import tkinter as tk

def click_multiple_times(num_clicks, delay_between_clicks):
    for _ in range(num_clicks):
        pyautogui.click()
        time.sleep(delay_between_clicks)

def start_clicker():
    num_clicks = int(clicks_entry.get())
    delay_between_clicks = float(delay_entry.get())
    click_multiple_times(num_clicks, delay_between_clicks)


root = tk.Tk()
root.title("Auto Clicker By qtkn")

label1 = tk.Label(root, text="Number of Clicks:")
label1.pack()

clicks_entry = tk.Entry(root)
clicks_entry.pack()

label2 = tk.Label(root, text="Delay Between Clicks On Seconds:")
label2.pack()

delay_entry = tk.Entry(root)
delay_entry.pack()

start_button = tk.Button(root, text="Start Auto Clicker", command=start_clicker)
start_button.pack()

root.mainloop()