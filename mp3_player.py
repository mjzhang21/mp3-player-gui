import pygame
import tkinter as tk
import os
from tkinter import filedialog


class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Amazing MP3 Player")
        self.root.geometry("800x600")

        self.playlist = []
        self.current_song = ""
        self.mxstate = 0  # music play state

        pygame.mixer.init()

        self.my_menu = tk.Menu(self.root)
        self.root.config(menu=self.my_menu)
        self.file_menu = tk.Menu(self.my_menu, tearoff=0)
        self.my_menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Select Folder", command=self.add_playlist)
        self.file_menu.add_command(label="Exit", command=quit)

        self.play = tk.PhotoImage(file="images/play-button.png")
        self.pause = tk.PhotoImage(file="images/pause-button.png")

        self.forward = tk.PhotoImage(file="images/forward-button.png")
        self.back = tk.PhotoImage(file="images/back-button.png")

        self.root.rowconfigure(0, weight=4)
        self.root.rowconfigure(2, minsize=100, weight=0)
        self.root.columnconfigure(0, weight=4)

        self.song_listbox = tk.Listbox(
            self.root,
            bg="gray43",
            fg="white",
            font=("Times", 18),
            width=8,
            activestyle=tk.NONE,
        )
        self.song_listbox.grid(row=0, column=0, rowspan=1, sticky="nsew")

        self.control_frame = tk.Frame(self.root)
        self.control_frame.grid(row=2, column=0, sticky="ns")

        self.btn_back = tk.Button(
            self.control_frame, image=self.back, command=self.previous_song
        )
        self.btn_play = tk.Button(
            self.control_frame, image=self.play, command=self.toggle_play_pause
        )
        self.btn_forward = tk.Button(
            self.control_frame, image=self.forward, command=self.next_song
        )

        self.btn_back.grid(row=2, column=0, sticky="ew", padx=15)
        self.btn_play.grid(row=2, column=1, sticky="ew", padx=15)
        self.btn_forward.grid(row=2, column=2, sticky="ew", padx=15)

        self.song_listbox.bind("<<ListboxSelect>>", self.on_select)
        self.w = tk.Scale(root, from_=0, to=200, orient="horizontal")
        self.w.grid(row=1, column=0)

        self.check_if_finished

    def check_if_finished(self):

        if self.mxstate == 2 or pygame.mixer.music.get_busy():
            print("Song is not finished")
        else:
            print("Song is finshed")

    def add_playlist(self):
        self.root.directory = tk.filedialog.askdirectory(title="Select a folder")
        self.playlist.clear()
        self.song_listbox.delete(0, tk.END)

        for file in os.listdir(self.root.directory):
            name, ext = os.path.splitext(file)
            if ext == ".mp3":
                self.playlist.append(file)

        for song in self.playlist:
            self.song_listbox.insert("end", song.split(".")[0])

    def toggle_play_pause(self):
        if not self.playlist:
            return

        if self.mxstate == 0:  # music not started

            pygame.mixer.music.play()
            self.btn_play.configure(image=self.pause)
            self.mxstate = 1
            return

        if self.mxstate == 1:  # music playing
            pygame.mixer.music.pause()
            self.btn_play.configure(image=self.play)
        else:  # music paused
            pygame.mixer.music.unpause()
            self.btn_play.configure(image=self.pause)
        self.mxstate = 3 - self.mxstate  # swap pause state

    def next_song(self):
        # next_one is a tuple with index of song in first position
        next_one = self.song_listbox.curselection()
        try:
            next_one[0] + 1 == len(self.playlist)
        except IndexError:
            return
        
        next_one = next_one[0] + 1
        self.song_listbox.selection_clear(0, tk.END)
        self.song_listbox.selection_set(next_one)
        self.current_song = self.playlist[next_one]
        self.mxstate = 1
        self.btn_play.configure(image=self.pause)

        pygame.mixer.music.load(os.path.join(root.directory, self.current_song))
        pygame.mixer.music.play()

    def previous_song(self):
        # next_one is a tuple with index of song in first position
        prev_one = self.song_listbox.curselection()
        try:
            prev_one[0] == 0
        except IndexError:
            return
        prev_one = prev_one[0] - 1
        self.song_listbox.selection_clear(0, tk.END)
        self.song_listbox.selection_set(prev_one)
        self.current_song = self.playlist[prev_one]
        self.mxstate = 1
        self.btn_play.configure(image=self.pause)

        pygame.mixer.music.load(os.path.join(root.directory, self.current_song))
        pygame.mixer.music.play()

    def on_select(self, event):

        w = event.widget
        index = int(w.curselection()[0])

        if self.current_song == self.playlist[index]:
            return
        self.current_song = self.playlist[index]
        self.mxstate = 0
        self.btn_play.configure(image=self.play)
        pygame.mixer.music.load(os.path.join(root.directory, self.current_song))


if __name__ == "__main__":

    root = tk.Tk()
    MusicPlayer(root)
    root.mainloop()
