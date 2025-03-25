import customtkinter as ctk
from tkinter import messagebox
import mysql.connector
from datetime import datetime
from big_one import *


class Addtransaction:
    def __init__(self, root):
        self.root = root
        self.root.title("Add transaction")
        self.root.geometry("400x300")
        
        self.frame = ctk.CTkFrame(master=root)
        self.frame.pack(padx=20, pady=20, fill="both", expand=True)

        self.open_add_transaction()


    def open_add_transaction(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        scrollable_frame = ctk.CTkScrollableFrame(self.frame, width=400, height=300)
        scrollable_frame.pack(fill="both", expand=True)

        ctk.CTkLabel(scrollable_frame, text="Reference:").pack(pady=5)
        reference_entry = ctk.CTkEntry(scrollable_frame)
        reference_entry.pack(pady=5)

        ctk.CTkLabel(scrollable_frame, text="Amount:").pack(pady=5)
        montant_entry = ctk.CTkEntry(scrollable_frame)
        montant_entry.pack(pady=5)

        ctk.CTkLabel(scrollable_frame, text="Description:").pack(pady=5)
        descriptionn_entry = ctk.CTkEntry(scrollable_frame)
        descriptionn_entry.pack(pady=5)

        ctk.CTkLabel(scrollable_frame, text="Date (YYYY-MM-DD):").pack(pady=5)
        date_entry = ctk.CTkEntry(scrollable_frame)
        date_entry.pack(pady=5)

        ctk.CTkLabel(scrollable_frame, text="Type:").pack(pady=5)
        type_var = ctk.StringVar()
        type_menu = ctk.CTkOptionMenu(scrollable_frame, values=["Deposit", "Transfer", "Withdrawal"], variable=type_var)
        type_menu.pack(pady=5)

        # Recipient field is hidden initially
        recipient_frame = ctk.CTkFrame(scrollable_frame)
        recipient_label = ctk.CTkLabel(recipient_frame, text="Recipient:")
        recipient_entry = ctk.CTkEntry(recipient_frame)
        recipient_label.pack(side="left", padx=5)
        recipient_entry.pack(side="left", padx=5)
        recipient_frame.pack(pady=5)  
        recipient_frame.pack_forget()

        
        def update_recipient_field(*args):
            if type_var.get() == "Transfer":
                recipient_frame.pack(pady=5)
            else:
                recipient_frame.pack_forget()

        type_var.trace_add("write", update_recipient_field)

        save_button = ctk.CTkButton(
            scrollable_frame, text="Save",
            command=lambda: self.save_transaction(
                reference_entry.get(),
                montant_entry.get(),
                descriptionn_entry.get(),
                date_entry.get(),
                type_var.get(),
                recipient_entry.get() if type_var.get() == "Transfer" else None
            )
        )
        save_button.pack(pady=10)

        ctk.CTkButton(scrollable_frame, text="Return", command=self.go_back_to_transaction).pack(pady=5)

    def data_historic(self):
     try:
        
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="budget_buddy"
        )
        cursor = mydb.cursor()

        
        cursor.execute("SELECT * FROM transaction")
        rows = cursor.fetchall()

        
        for index, row in enumerate(rows, start=1):
            print(f"Line {index} : {row}")

        cursor.close()
        mydb.close()

     except mysql.connector.Error as err:
        messagebox.showerror("Error !", f"Error with the database : {err}")


    def go_back_to_transaction(self):
        self.frame.destroy()
        from transaction_page import TransactionPage
        TransactionPage(self.root)
    
    def save_transaction(self, reference, amount, description, date, type_transaction, recipient):
        if not reference or not amount or not description or not date or not type_transaction:
            messagebox.showerror("Error!", "All fields must be completed")
       
        
        try:
            amount = float(amount)
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error!", "Invalid amount or date format")
            return


        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="budget_buddy"
            )
            cursor = mydb.cursor()

            cursor.execute(
                """INSERT INTO transaction(reference, description, amount, date, type, recipient)
                VALUES (%s, %s, %s, %s, %s, %s)""",
                (reference, description, amount, date, type_transaction, recipient)
            )
            mydb.commit()
            mydb.close()

            self.data_historic()
            messagebox.showinfo("Success", "Transaction added successfully.")
            self.open_add_transaction()
        except mysql.connector.Error as err:
            messagebox.showerror("Error!", f"Database error: {err}")




