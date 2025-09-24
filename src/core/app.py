from  ..screens.screen_manager import Screen
from ..screens.components import UIComponent
import tkinter as tk

ROUTES = {
    "Home": Screen.home,
    "Add contact": Screen.add_contact,
    "Send e-mail": Screen.send_email,
}

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Gerenciador de contatos")
        self.root.geometry("800x600")

        self.menu = tk.Frame(self.root, bg=UIComponent.MENU_BG, height=200)
        self.menu.pack(side='top', fill='x')

        self.content = tk.Frame(self.root, bg= UIComponent.CONTENT_BG)
        self.content.pack(fill='both', expand=True)
    
    def run(self):
        Screen.home(self.content)
        UIComponent.ui_menu(self.menu, self.content, ROUTES)
        self.root.mainloop()
        