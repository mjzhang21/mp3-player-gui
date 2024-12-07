import tkinter as tk

root = tk.Tk()
root.title("Amazing MP3 Player")
root.geometry("700x500")


play = tk.PhotoImage(file="images/play-button.png")
pause = tk.PhotoImage(file="images/pause-button.png")
forward = tk.PhotoImage(file="images/forward-button.png")
back = tk.PhotoImage(file="images/back-button.png")


root.rowconfigure(0, weight=1)
root.rowconfigure(1, minsize=100, weight=0)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, minsize=260)
song_listbox = tk.Listbox(root, bg="green", fg="white")

control_frame = tk.Frame(root)

btn_forward = tk.Button(control_frame, image=forward)
btn_back = tk.Button(control_frame, image=back)
btn_play = tk.Button(control_frame, image=play)

btn_back.grid(row=0, column=0, sticky="ew", padx=15)
btn_play.grid(row=0, column=1, sticky="ew", padx=15)
btn_forward.grid(row=0, column=2, sticky="ew", padx=15)

song_listbox.grid(row=0, column=1, rowspan=2, sticky="nsew")
control_frame.grid(row=1, column=0, sticky="ns")


root.mainloop()
