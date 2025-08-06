from screens.screen_manager import Screen
import tkinter as tk

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Gerenciador de contatos")
        self.root.geometry("800x600")
    
    def run(self):
        Screen.home(self.root)
        self.root.mainloop()