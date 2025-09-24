import tkinter as tk
from ..screens.components import UIComponent

class Screen:

    @staticmethod
    def clear(root: tk.Frame):
        for widget in root.winfo_children():
            widget.destroy()

    @staticmethod
    def home(root: tk.Frame):
        Screen.clear(root)
        tk.Label(root, text="Gerenciador de contatos", background=UIComponent.CONTENT_BG, foreground=UIComponent.CONTENT_FG, font=UIComponent.CONTENT_FONT).pack()
    
    @staticmethod
    def add_contact(root: tk.Frame):
        Screen.clear(root)
        tk.Label(root, text="Adicionar contato",background=UIComponent.CONTENT_BG, foreground=UIComponent.CONTENT_FG, font=UIComponent.CONTENT_FONT).pack()

    
    @staticmethod
    def send_email(root: tk.Frame):
        Screen.clear(root)
        tk.Label(root, text="Enviar e-Mail",background=UIComponent.CONTENT_BG, foreground=UIComponent.CONTENT_FG, font=UIComponent.CONTENT_FONT).pack()