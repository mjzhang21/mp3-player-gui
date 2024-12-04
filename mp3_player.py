import tkinter as tk


root = tk.Tk()
root.title("Amazing MP3 Player")
root.geometry("800x600")

label = tk.Label(
    root,
    text="MP3 Player",
    fg="white",
    bg="blue",
    width=20,
    font=("Arial", 24),
)
label.pack(padx=20, pady=20)

root.mainloop()
