import tkinter as tk
from tkinter import ttk

class Screen:

    @staticmethod
    def clear(root: tk.Frame):
        for widget in root.winfo_children():
            widget.destroy()

    @staticmethod
    def home(root: tk.Frame):
        Screen.clear(root)
        ttk.Label(root, text="Gerenciador de contatos", background="white").pack()
    
    @staticmethod
    def add_contact(root: tk.Frame):
        Screen.clear(root)
        ttk.Label(root, text="Adicionar contato")

    
    @staticmethod
    def send_email(root: tk.Frame):
        Screen.clear(root)
        ttk.Label(root, text="Enviar e-Mail")
