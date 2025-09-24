import tkinter as tk



class UIComponent:

    MENU_FONT = ("Segoe UI", 11, "bold")
    MENU_BG = "#2E3440"
    MENU_FG = "#ECEFF4"
    MENU_HOVER = "#313244"
    MENU_ACTIVE = "#45475A"

    CONTENT_BG = "#3B4252"
    CONTENT_FG = "#D8DEE9"
    CONTENT_FONT = ("Calibri", 12)

    @staticmethod
    def ui_menu(root: tk.Frame, content_frame:tk.Frame, routes: dict):
        tk.Label(root, text="Menu", background=UIComponent.MENU_BG, foreground=UIComponent.MENU_FG, font=UIComponent.MENU_FONT).pack()
        for name, screen in routes.items():
            btn = tk.Button(root, text=name, command=lambda f=screen: f(content_frame))
            btn.pack(side="left", padx=5, pady=10)
    
    @staticmethod
    def ui_menu_btn(root: tk.Frame):
        pass