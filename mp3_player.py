import tkinter as tk


class MusicPlayer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Amazing MP3 Player")
        self.root.geometry("800x600")

        self.label = tk.Label(self.root, text="MP3 Player", font=("Arial", 24))
        self.label.pack(padx=20, pady=20)

        self.root.mainloop()


MusicPlayer()
