import pygame
import tkinter as tk
import tkinter.filedialog


class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Amazing MP3 Player")
        self.root.geometry("700x500")

        self.song_dict = {}
        self.path = ""
        self.count = 0

        pygame.mixer.init()

        self.my_menu = tk.Menu(self.root)
        self.root.config(menu=self.my_menu)
        self.file_menu = tk.Menu(self.my_menu, tearoff=0)

        self.my_menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open", command=self.add_song)
        self.file_menu.add_command(label="Exit", command=quit)

        self.play = tk.PhotoImage(file="images/play-button.png")
        self.pause = tk.PhotoImage(file="images/pause-button.png")
        self.forward = tk.PhotoImage(file="images/forward-button.png")
        self.back = tk.PhotoImage(file="images/back-button.png")

        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, minsize=100, weight=0)
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, minsize=260)

        self.song_listbox = tk.Listbox(self.root, bg="green", fg="white", font=(14))

        self.control_frame = tk.Frame(self.root)

        self.btn_forward = tk.Button(self.control_frame, image=self.forward)
        self.btn_back = tk.Button(self.control_frame, image=self.back)
        self.btn_play = tk.Button(
            self.control_frame, image=self.play, command=self.play_music
        )

        self.btn_back.grid(row=0, column=0, sticky="ew", padx=15)
        self.btn_play.grid(row=0, column=1, sticky="ew", padx=15)
        self.btn_forward.grid(row=0, column=2, sticky="ew", padx=15)

        self.song_listbox.grid(row=0, column=1, rowspan=2, sticky="nsew")
        self.control_frame.grid(row=1, column=0, sticky="ns")

    def add_song(self):
        song_path = tk.filedialog.askopenfilename(
            title="Select a file", filetypes=(("mp3 Files", "*.mp3"),)
        )
        if song_path:
            song_name = song_path.split("/")[-1].split(".")[0]
            self.song_dict[self.count] = [song_name, song_path]
            self.song_listbox.insert(self.count, song_name)
            self.path = song_path
            self.count += 1

    def play_music(self):
        if self.path:
            pygame.mixer.music.load(self.path)
            pygame.mixer.music.play()


root = tk.Tk()
MusicPlayer(root)
root.mainloop()
