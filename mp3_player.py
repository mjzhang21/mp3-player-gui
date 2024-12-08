import tkinter as tk
import tkinter.filedialog

root = tk.Tk()
root.title("Amazing MP3 Player")
root.geometry("700x500")

song_dict = {}
count = 0


def add_song():
    global count
    song_path = tk.filedialog.askopenfilename(
        title="Select a file", filetypes=(("mp3 Files", "*.mp3"),)
    )
    song_name = song_path.split("/")[-1].split(".")[0]
    song_dict[count] = [song_name, song_path]
    song_listbox.insert(count, song_name)

    count += 1


my_menu = tk.Menu(root)
root.config(menu=my_menu)
file_menu = tk.Menu(my_menu, tearoff=0)

my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=add_song)
file_menu.add_command(label="Exit", command=quit)

play = tk.PhotoImage(file="images/play-button.png")
pause = tk.PhotoImage(file="images/pause-button.png")
forward = tk.PhotoImage(file="images/forward-button.png")
back = tk.PhotoImage(file="images/back-button.png")

root.rowconfigure(0, weight=1)
root.rowconfigure(1, minsize=100, weight=0)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, minsize=260)

song_listbox = tk.Listbox(root, bg="green", fg="white", font=(14))

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
