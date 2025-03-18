import tkinter
from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

window = customtkinter.CTk()
window.title("Budget Buddy")
window.geometry("800x600")

def submit():
    my_label.configure(text = f'Bienvenue {my_entry.get()}')

def clear():
    my_entry.delete(0, END)

my_label = customtkinter.CTkLabel(window, text = "", font = ("Helvatica", 24))
my_label.pack(pady = 40)

my_entry = customtkinter.CTkEntry(window, placeholder_text = "Votre nom", width = 200, font = ("Helvatica", 15), text_color = "white")
my_entry.pack(pady = 20)

my_button = customtkinter.CTkButton(window, text = "Submit", command = submit, font = ("Helvatica", 15))
my_button.pack(pady = 10)

clear_button = customtkinter.CTkButton(window, text = "Clear", command = clear, font = ("Helvatica", 15))
clear_button.pack(pady = 10)

window.mainloop()