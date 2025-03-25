import customtkinter as ctk
import mysql.connector
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  
import pandas as pd


class Historic:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x600")
        self.tabView = ctk.CTkTabview(self.root)
        self.tabView.pack(padx=20, pady=20, fill="both", expand=True)

        self.tabView.add("Transactions")
        self.tabView.add("Graph")
        self.tabView.add("Balance")

       
        self.transactions_frame = ctk.CTkFrame(self.tabView.tab("Transactions"))
        self.transactions_frame.pack(fill="both", expand=True, padx=10, pady=10)

    
        filter_frame_top = ctk.CTkFrame(self.transactions_frame)
        filter_frame_top.pack(side="top", fill="x", pady=5, padx=5)

        
        self.filter_options = ["ID", "Type", "Amount"]
        self.filter_combo = ctk.CTkComboBox(filter_frame_top, values=self.filter_options, state="readonly", width=100)
        self.filter_combo.pack(side="left", padx=5)
        self.filter_combo.set("Filter by")

        self.filter_entry = ctk.CTkEntry(filter_frame_top, font=("arial", 12), width=120)
        self.filter_entry.pack(side="left", padx=5)

        ctk.CTkButton(filter_frame_top, text="Filter", command=self.filter_transactions, width=80, height=25).pack(side="left", padx=5)
        ctk.CTkButton(filter_frame_top, text="Show all", command=self.load_transactions, width=80, height=25).pack(side="left", padx=5)

        
        self.date_debut_entry = ctk.CTkEntry(filter_frame_top, placeholder_text="Date start (YYYY-MM-DD)", width=120)
        self.date_debut_entry.pack(side="left", padx=5)

        self.date_fin_entry = ctk.CTkEntry(filter_frame_top, placeholder_text="Date end (YYYY-MM-DD)", width=120)
        self.date_fin_entry.pack(side="left", padx=5)

        ctk.CTkButton(filter_frame_top, text="Filter by Date", command=self.filter_by_date, width=100, height=25).pack(side="left", padx=5)

        
        self.tree_frame = ctk.CTkFrame(self.transactions_frame)
        self.tree_frame.pack(fill="both", expand=True, padx=5, pady=5)

        
        self.tree = ttk.Treeview(
            self.tree_frame,
            columns=("ID", "Description", "Reference", "Amount", "Date", "Type", "Recipient"),
            show="headings"
        )
        self.tree.pack(expand=True, fill="both", padx=20, pady=20)

       
        columns = ["ID", "Description", "Reference", "Amount", "Date", "Type", "Recipient"]
        for col in columns:
            self.tree.heading(col, text=col, anchor="center")  
            self.tree.column(col, anchor="center")  

        
        self.tree.column("ID", width=50)
        self.tree.column("Description", width=150)
        self.tree.column("Reference", width=100)
        self.tree.column("Amount", width=100)
        self.tree.column("Date", width=100)
        self.tree.column("Type", width=100)
        self.tree.column("Recipient", width=150)

        
        button_frame_bottom = ctk.CTkFrame(self.transactions_frame)
        button_frame_bottom.pack(side="bottom", fill="x", pady=5, padx=5)

        
        center_frame = ctk.CTkFrame(button_frame_bottom)
        center_frame.pack(side="top", pady=5)

        self.id_entry = ctk.CTkEntry(center_frame, placeholder_text="ID of transaction", width=100)
        self.id_entry.pack(side="left", padx=5)

        ctk.CTkButton(center_frame, text="Delete", command=self.delete_transaction, width=80, height=25).pack(side="left", padx=5)
        ctk.CTkButton(center_frame, text="Refresh", command=self.load_transactions, width=80, height=25).pack(side="left", padx=5)
        ctk.CTkButton(center_frame, text="Return", command=self.go_back, width=80, height=25).pack(side="left", padx=5)

        
        self.load_transactions()

        
        self.graph_frame = ctk.CTkFrame(self.tabView.tab("Graph"))
        self.graph_frame.pack(fill="both", expand=True, padx=10, pady=10)

        
        self.load_graph()

    def load_transactions(self, filter_by=None, filter_value=None, date_debut=None, date_fin=None):
        """Load the transaction from the database and posted in the Treeview."""
        try:
            
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="budget_buddy"
            )
            cursor = mydb.cursor()

            
            if filter_by and filter_value:
                query = f"SELECT id, description, reference, amount, date, type, recipient FROM transaction WHERE {filter_by} = %s"
                cursor.execute(query, (filter_value,))
            elif date_debut and date_fin:
                query = "SELECT id, description, reference, amount, date, type, recipient FROM transaction WHERE date BETWEEN %s AND %s"
                cursor.execute(query, (date_debut, date_fin))
            else:
                cursor.execute("SELECT id, description, reference, amount, date, type, recipient FROM transaction")

            rows = cursor.fetchall()

            
            for item in self.tree.get_children():
                self.tree.delete(item)

            
            for row in rows:
                self.tree.insert("", "end", values=row)

            cursor.close()
            mydb.close()

        except mysql.connector.Error as err:
            messagebox.showerror("Error !", f"Error with the database : {err}")

    def load_graph(self):
        """Load and display graph in 'Graph' tab'."""
        try:
            
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="budget_buddy"
            )
            cursor = mydb.cursor()

           
            cursor.execute("SELECT date, amount FROM transaction")
            rows = cursor.fetchall()

            # Convert the data in DataFrame
            df = pd.DataFrame(rows, columns=["date", "amount"])

            
            fig, ax = plt.subplots()
            ax.scatter(df["date"], df["amount"], color="blue")
            ax.set_title("Amount according to date")
            ax.set_xlabel("Date")
            ax.set_ylabel("Montant")

            
            canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill="both", expand=True)

            cursor.close()
            mydb.close()

        except mysql.connector.Error as err:
            messagebox.showerror("Error !", f"Error with the database : {err}")

    def filter_transactions(self):
        
        filter_by = self.filter_combo.get()  
        filter_value = self.filter_entry.get() 

        if not filter_by or not filter_value:
            messagebox.showwarning("Warning", "Select a filter and entera value.")
            return

        
        self.load_transactions(filter_by=filter_by.lower(), filter_value=filter_value)

    def filter_by_date(self):
        
        date_debut = self.date_debut_entry.get()
        date_fin = self.date_fin_entry.get()

        if not date_debut or not date_fin:
            messagebox.showwarning("Warning", "Enter a date start and a date end.")
            return

        try:
            datetime.strptime(date_debut, "%Y-%m-%d")
            datetime.strptime(date_fin, "%Y-%m-%d")
        except ValueError:
            messagebox.showwarning("Warning", "format for dates must be YYYY-MM-DD.")
            return

        
        self.load_transactions(date_debut=date_debut, date_fin=date_fin)

    def delete_transaction(self):

        transaction_id = self.id_entry.get()

        if not transaction_id:
            messagebox.showwarning("Warning", "Enter a valid ID.")
            return

        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="J",
                database="budget_buddy"
            )
            cursor = mydb.cursor()
            cursor.execute("DELETE FROM transaction WHERE id = %s", (transaction_id,))
            mydb.commit()

            if cursor.rowcount > 0:
                messagebox.showinfo("Success", f"Transaction with  ID {transaction_id} delete with success.")
                self.load_transactions()  
            else:
                messagebox.showinfo( f"None transaction find with ID {transaction_id}.")

            cursor.close()
            mydb.close()

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error with the database : {err}")

    def go_back(self):

        self.tabView.destroy()
        from welcome_page import Welcome


