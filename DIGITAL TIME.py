import tkinter as tk
from time import strftime

def time():
    string = strftime('%H:%M:%S %p')  # Format: Hour:Minute:Second AM/PM
    label.config(text=string)
    label.after(1000, time)  # Update every 1000 milliseconds (1 second)

# Create GUI window
root = tk.Tk()
root.title('Digital Clock')

# Customize label
label = tk.Label(root, font=('Arial', 50), background='black', foreground='cyan')
label.pack(anchor='center')

time()  # Start the clock
root.mainloop()
