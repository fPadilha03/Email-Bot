# 📋 Gerenciador de Contatos + E-mail Automático (Python + Excel + Tkinter)

Este projeto é um sistema simples e eficiente para pequenas empresas que precisam **organizar seus contatos em planilhas** e **enviar e-mails automáticos com poucos cliques**.

✅ Interface gráfica amigável (Tkinter)  
✅ Cadastro de contatos direto em planilha Excel  
✅ Envio de e-mails automáticos com nome do cliente  
✅ Estrutura de código modular e profissional  

---

## 🛠️ Tecnologias Utilizadas
- Python 3.x
- Tkinter (Interface Gráfica)
- openpyxl (Manipulação de Excel)
- smtplib (Envio de E-mails)

---

## 📦 Estrutura do Projeto
```
meu_projeto/
├── main.py                    # Arquivo principal para execução
├── core/
│   └── app.py                 # Classe principal do aplicativo (Tkinter)
├── screens/
│   └── screen_manager.py      # Gerenciamento de Telas (Home, Cadastro, etc)
├── services/
│   └── email_service.py       # Lógica de envio de e-mails
├── utils/
│   └── excel_handler.py       # Manipulação da planilha Excel
├── contatos.xlsx              # Planilha onde os contatos são salvos
```

---

## 🚀 Como Executar

1. Clone o projeto:
    ```bash
    git clone https://github.com/seuusuario/meu_projeto.git
    cd meu_projeto
    ```

2. Instale as dependências (se necessário):
    ```bash
    pip install openpyxl
    ```

3. Execute o sistema:
    ```bash
    python main.py
    ```

---

## 💡 Como Funciona?

1. Tela inicial com botões:
    - Adicionar Contato
    - Enviar E-mail Automático
2. Na tela de cadastro, você digita nome e e-mail.
3. O contato é salvo na planilha Excel.
4. Futuramente, poderá enviar e-mails automáticos personalizados.

---