import tkinter
from tkinter import *
from tkinter import messagebox
import customtkinter
from customtkinter import *
from PIL import Image

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

window = customtkinter.CTk()
window.title("Retrait d'Argent")
window.resizable(False, False)
window.geometry("800x600") 

def main():
        window.destroy()
        import main_menu
        print("Menu principal")

return_button = customtkinter.CTkButton(window, text = "Menu", cursor = "hand2", command = main)
return_button.place(rely=0.5,relx=0.2)

window.mainloop()