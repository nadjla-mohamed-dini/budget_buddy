import pyodbc
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.title("Budget Buddy")
app.geometry("800x600")

def connect_db():
    try:
        databa

entry_database = customtkinter.CTkEntry(app, placeholder_text = "database")
entry_database.place(relx = 0.1, rely = 0.2)

connect_button = customtkinter.CTkButton(app, text = 'connect', command = connect_db)
connect_button.place(relx = 0.1, rely = 0.3)

info_label = customtkinter.CTkLabel(app, text = 'turtle')
info_label.place(relx = 0.1, rely = 0.4)

app.mainloop()

connection = pyodbc.connect('DRIVER = {SQL Server};' + 'Server = budget')