# Create a simple window with Python and Tkinter
# With Size, title and status bar 
import tkinter as tk

root = tk.Tk()
root.geometry('300x150')
root.title("Hello World!")

statusbar = tk.Label(root, text="Ready", anchor=tk.W)

statusbar.pack(side=tk.BOTTOM, fill=tk.X)

root.mainloop()
