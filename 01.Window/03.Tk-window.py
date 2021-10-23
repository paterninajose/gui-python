# Create a simple window with Python and Tkinter
# With Size, title and status bar 
import tkinter as tk

root = tk.Tk()
# Resizing
root.geometry('1024x768')
root.title("Hello World!")
# Adding icon
root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='images/gui/icons/music.png'))

statusbar = tk.Label(root, text="Ready", anchor=tk.W)

statusbar.pack(side=tk.BOTTOM, fill=tk.X)

root.mainloop()
