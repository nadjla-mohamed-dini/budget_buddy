import tkinter
from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

window = customtkinter.CTk()
window.title("Budget Buddy")
window.geometry("800x600")

def submit():
    my_label.configure(text = f'Déposé {my_entry.get()} €')

def clear():
    my_entry.delete(0, END)

my_label = customtkinter.CTkLabel(window, text = "", font = ("Helvatica", 24))
my_label.place(relx = 0.7, rely = 0.3)

my_entry = customtkinter.CTkEntry(window, placeholder_text = "Combien ?", width = 200, font = ("Helvatica", 15), text_color = "white")
my_entry.place(relx = 0.1, rely = 0.3)

my_button = customtkinter.CTkButton(window, text = "Submit", command = submit, font = ("Helvatica", 15))
my_button.place(relx = 0.4, rely = 0.3)

clear_button = customtkinter.CTkButton(window, text = "Clear", command = clear, font = ("Helvatica", 15))
clear_button.place(relx = 0.14, rely = 0.4)

def submit():
    my_label2.configure(text = f'Retiré {my_entry2.get()} €')

my_label2 = customtkinter.CTkLabel(window, text = "", font = ("Helvatica", 24))
my_label2.place(relx = 0.7, rely = 0.6)

my_entry2 = customtkinter.CTkEntry(window, placeholder_text = "Combien ?", width = 200, font = ("Helvatica", 15), text_color = "white")
my_entry2.place(relx = 0.1, rely = 0.6)

my_button2 = customtkinter.CTkButton(window, text = "Submit", command = submit, font = ("Helvatica", 15))
my_button2.place(relx = 0.4, rely = 0.6)

clear_button2 = customtkinter.CTkButton(window, text = "Clear", command = clear, font = ("Helvatica", 15))
clear_button2.place(relx = 0.14, rely = 0.7)



window.mainloop()