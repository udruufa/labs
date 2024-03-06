import tkinter as tk

def dels():
    global zad
    zad.delete(0, tk.END)

window = tk.Tk()
frame = tk.Frame()

txt = tk.Label(
    text="text12345"
)
txt.pack()
frame.pack()
zad = tk.Entry()
zad.pack()
button = tk.Button(
    text="Save",
    master=frame,
    command=zad.dels
)
button.pack()

window.mainloop()

