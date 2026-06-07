# main.py
import customtkinter as ctk

# Importar todos os modelos para registar no SQLAlchemy
from models.utilizador import Utilizador
from models.paciente import Paciente
from models.consulta import Consulta

from gui.login import LoginWindow

def main():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    app = LoginWindow()
    app.mainloop()

if __name__ == "__main__":
    main()