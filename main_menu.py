import tkinter
from tkinter import *
from tkinter import messagebox
import customtkinter
from customtkinter import *
from PIL import Image

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

window = customtkinter.CTk()
window.title("Menu Principal ")
window.resizable(False, False)
window.geometry("800x600") 

def deposit():
        messagebox.showinfo("Déconnexion", "Au Revoir")
        window.destroy()
        print("Déconnecté")

def history():
        window.destroy()
        import history_menu
        print("Déconnecté")

deposit_button = customtkinter.CTkButton(window, text = "Dépôt", height = 70, width = 150, cursor = "hand2", command = history)
deposit_button.place(rely=0.4,relx=0.25)

withdrawal_button = customtkinter.CTkButton(window, text = "Retrait", height = 70, width = 150, cursor = "hand2", command = history)
withdrawal_button.place(rely=0.4,relx=0.5)

history_button = customtkinter.CTkButton(window, text = "Transactions",  height = 70, width = 150, cursor = "hand2", command = history)
history_button.place(rely=0.6,relx=0.25)

graph_button = customtkinter.CTkButton(window, text = "Graphiques", height = 70, width = 150, cursor = "hand2", command = history)
graph_button.place(rely=0.6,relx=0.5)

logoff_button = customtkinter.CTkButton(window, text = "Déconnexion", height = 50, width = 130, cursor = "hand2", command = deposit)
logoff_button.place(rely=0.8,relx=0.2)

window.mainloop()