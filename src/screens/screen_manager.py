import tkinter as tk

class Screen:

    @staticmethod
    def clear(root: tk.Tk):
        for widget in root.winfo_children():
            widget.destroy()

    @staticmethod
    def home(root: tk.Tk):
        Screen.clear(root)
        tk.Label(root, text="Gerenciador de Contatos", font=("Arial", 16)).pack(pady=20)
        tk.Button(root, text="Adicionar Contato", width=25, command=lambda: Screen.add_contact(root)).pack(pady=10)
        tk.Button(root, text="Enviar E-mail Automático", width=25, command=lambda: Screen.send_email(root)).pack(pady=10)
    
    @staticmethod
    def add_contact(root: tk.Tk):
        Screen.clear(root)
        tk.Label(root, text="Cadastro de Contato", font=("Arial", 14)).pack(pady=10)
    
    @staticmethod
    def send_email(root: tk.Tk):
        Screen.clear(root)
        tk.Label(root, text="Envio de email de cobrança", font=("Arial", 14)).pack(pady=10)