import tkinter as tk
from tkinter import ttk

class UIComponent:

    @staticmethod
    def ui_menu(root: tk.Frame, content_frame:tk.Frame, routes: dict):
        for name, screen in routes.items():
            btn = ttk.Button(root, text=name, command=lambda f=screen: f(content_frame))
            btn.pack(side="left", padx=5, pady=10)