import customtkinter as ctk
from tkinter import messagebox
import mysql.connector
from datetime import datetime


class Addtransaction:
    def __init__(self,root):
        self.root = root
        self.root.title("Add transaction")
        self.root.geometry("400x300")
        
        self.frame = ctk.CTkFrame(master=root)
        self.frame.pack(padx=20, pady=20,fill="both",expand=True)

        self.open_add_transaction()

       
        

    def open_add_transaction(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        ctk.CTkLabel(self.frame, text="Reference:").pack(pady=5)
        reference_entry = ctk.CTkEntry(self.frame)
        reference_entry.pack(pady=5)

        ctk.CTkLabel(self.frame, text="Amount:").pack(pady=5)
        montant_entry = ctk.CTkEntry(self.frame)
        montant_entry.pack(pady=5)

        ctk.CTkLabel(self.frame, text="Description:").pack(pady=5)
        descriptionn_entry = ctk.CTkEntry(self.frame)
        descriptionn_entry.pack(pady=5)

        ctk.CTkLabel(self.frame, text="Date (YYYY-MM-DD):").pack(pady=5)
        date_entry = ctk.CTkEntry(self.frame)
        date_entry.pack(pady=5)

        ctk.CTkLabel(self.frame, text= "Type:").pack(pady=5)
        type_menu = ctk.CTkOptionMenu(self.frame, values=["Deposit", "Transfer", "Withdrawal"])
        type_menu.pack(pady=5)

        save_button = ctk.CTkButton(self.frame, text="Save", command= lambda: self.save_transaction(reference_entry.get(),
                                                                                                    montant_entry.get(),
                                                                                                    descriptionn_entry.get(),
                                                                                                    date_entry.get(),
                                                                                                    type_menu.get(),
                                                                                                    self.frame))
        save_button.pack(pady=10)

        ctk.CTkButton(self.frame, text="Return", command=self.go_back_to_transaction).pack(pady=5)
    def go_back_to_transaction(self):
        self.frame.destroy()
        from transaction_page import TransactionPage
        TransactionPage(self.root)

    def save_transaction(self, reference, amount, description, date, type_transaction, window):

        if not reference or not amount or not description or not date or not type_transaction:
            messagebox.showerror("Error!", "all fields must be completed")
            return
        
        try:
            amount = float(amount)
            datetime.strptime(date, "%Y-%m-%d")

        except ValueError:
            messagebox.showerror("Error!", "Invalide amount or date")

        try:
            mydb = mysql.connector.connect ( 
                host = "localhost",
                user = "root",
                password = "",
                database = "budget_buddy"
            )
            cursor = mydb.cursor()

            cursor.execute ("""INSERT INTO transaction(reference, description, amount, date, type)
                            VALUES ( %s, %s, %s, %s, %s)
                            """,(reference, description, amount, date, type_transaction))
            mydb.commit()
            mydb.close()

            messagebox.showinfo("Succes", "Transaction add with succes.")
            self.open_add_transaction()
        except mysql.connector.Error as err:
            messagebox.showerror("Erreur", f"Erreur avec la base de données : {err}")



