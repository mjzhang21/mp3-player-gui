import pygame
import tkinter as tk
from tkinter import filedialog

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Amazing MP3 Player")
        self.root.geometry("800x600")

        self.song_dict = {}
        self.path = ""
        self.count = 0
        self.mxstate = 0 #music play state

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

        self.root.rowconfigure(0, weight=4)
        self.root.rowconfigure(1, minsize=100, weight=0)
        self.root.columnconfigure(0, weight=4)
        self.root.columnconfigure(1, minsize = 200, weight = 1)
        

        self.song_listbox = tk.Listbox(self.root, bg="gray43", fg="white", font = ('Times', 18), width = 8)
        self.song_listbox.grid(row=0, column=1, rowspan=2, sticky="nsew")

        self.control_frame = tk.Frame(self.root)
        self.control_frame.grid(row=1, column=0, sticky="ns")

        self.btn_back = tk.Button(self.control_frame, image=self.back)
        self.btn_play= tk.Button(
            self.control_frame, image=self.play, command=self.toggle_play_pause
        )
        self.btn_forward = tk.Button(self.control_frame, image=self.forward)

        self.btn_back.grid(row=0, column=0, sticky="ew", padx=15)
        self.btn_play.grid(row=0, column=1, sticky="ew", padx=15)
        self.btn_forward.grid(row=0, column=2, sticky="ew", padx=15)
        
        self.song_listbox.bind('<<ListboxSelect>>', self.on_select)

    def add_song(self):
        song_path = tk.filedialog.askopenfilename(
            title="Select a file", filetypes=(("mp3 Files", "*.mp3"),),initialdir = r"C:\Users\piefo\Music\playlists"
        )
        if song_path:
            song_name = song_path.split("/")[-1].split(".")[:-1]
            self.song_dict[self.count] = [song_name, song_path]
            self.song_listbox.insert(self.count, song_name)
            self.count += 1
    
    def toggle_play_pause(self):
        if self.path == "":
            return
        
        if self.mxstate == 0:  # music not started
            pygame.mixer.music.play()
            self.btn_play.configure(image = self.pause)
            self.mxstate =  1
            return
            
        if self.mxstate == 1:  # music playing
            pygame.mixer.music.pause()
            self.btn_play.configure(image = self.play)
        else:  # music paused
            pygame.mixer.music.unpause()
            self.btn_play.configure(image = self.pause)
        self.mxstate = 3-self.mxstate  # swap pause state        
           
                
    def on_select(self, event):
    
        w = event.widget
        index = int(w.curselection()[0])
        
        song_path = self.song_dict[index][1]
        if song_path == self.path:
            return
        if song_path:
            self.path = song_path
        pygame.mixer.music.load(self.path)
        
        self.mxstate = 0
        self.btn_play.configure(image = self.play)
        
   
if __name__ == "__main__":

    root = tk.Tk()
    MusicPlayer(root)
    root.mainloop()
