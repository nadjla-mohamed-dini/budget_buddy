import tkinter
from tkinter import *
from tkinter import messagebox
import customtkinter
from customtkinter import *
from PIL import Image


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

window = customtkinter.CTk()
window.title("Page de Connexion")
window.resizable(False, False)
window.geometry("800x600") 

def login():
    if username_entry.get() == '' or password_entry.get() == '':
        messagebox.showerror("Erreur", "Tous les champs ne sont pas remplis")
        print("erreur de connexion")
    elif username_entry.get() == 'a' or password_entry.get() == 'a':
        messagebox.showinfo("Connexion", "Bienvenue")
        window.destroy()
        import main_menu
        print("Connecté")
    else:
        messagebox.showerror("Erreur", "Mauvais identifiants")



welcome_label = customtkinter.CTkLabel(window, text = "Budget Buddy", bg_color = "#242424", font = ("arial", 40))
welcome_label.place(rely=0.15,relx=0.2)

username_entry = customtkinter.CTkEntry(window, placeholder_text = "Email", width = 200)
username_entry.place(rely=0.3,relx=0.2)

password_entry = customtkinter.CTkEntry(window, placeholder_text = "Mot de Passe", width = 200, show = '*')
password_entry.place(rely=0.4,relx=0.2)

login_button = customtkinter.CTkButton(window, text = "Connexion", cursor = "hand2", command = login)
login_button.place(rely=0.5,relx=0.2)

window.mainloop()