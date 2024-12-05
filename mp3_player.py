import tkinter as tk


app = tk.Tk()
app.title("Amazing MP3 Player")

# app.columnconfigure(0, minsize=800, weight=1)

# app.rowconfigure(1, minsize=500, weight=1)
song_listbox = tk.Listbox(app, bg="green", fg="white")
song_listbox.pack()

control_frame = tk.Frame(app)


btn_next = tk.Button(control_frame, text="Next Song")
btn_prev = tk.Button(control_frame, text="Prev Song")
btn_play = tk.Button(control_frame, text="Play/Pause")


btn_prev.grid(row=0, column=0, sticky="ns", padx=5)
btn_play.grid(row=0, column=1, sticky="ns", padx=5)
btn_next.grid(row=0, column=2, sticky="ns", padx=5)

control_frame.pack(side="bottom")
app.mainloop()
