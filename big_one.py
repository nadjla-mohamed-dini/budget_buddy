import customtkinter as ctk
from CTkTable import CTkTable
import mysql.connector
from tkinter import messagebox


class Historic:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x400")
        self.tabView = ctk.CTkTabview(self.root)
        self.tabView.pack(padx=20, pady=20, fill="both", expand=True)
        

        self.tabView.add("Transactions")
        self.tabView.add("Graph")
        self.tabView.add("Balance")

        
        self.scrollable_frame = ctk.CTkScrollableFrame(self.tabView.tab("Transactions"), width=780, height=350)
        self.scrollable_frame.pack(fill="both", expand=True, padx=10, pady=10)
        self.balance_label = ctk.CTkLabel(self.tabView.tab("Balance"), text="Votre solde actuel : ", font=("Arial", 14))
        self.balance_label.pack(pady=10)

        # Ajouter le tableau 
        default_values = [[""] * 6 for _ in range(10)]  
        headers = [["ID", "Description", "Reference", "Amount", "Date", "Type", "Recipient"]]
        self.table = CTkTable(
            self.scrollable_frame,
            row=len(default_values),
            column=7,
            values=headers + default_values
        )
        self.table.pack(expand=True, fill="both", padx=20, pady=20)

        self.id_entry = ctk.CTkEntry(self.scrollable_frame, placeholder_text="ID de la transaction")
        self.id_entry.pack(pady=5)

        
        top_frame = ctk.CTkFrame(self.scrollable_frame)
        top_frame.pack(side="top", fill="x", pady=5)



        ctk.CTkButton(top_frame, text="Delete", command=self.delete_transaction).pack(side="left", padx=5)
        ctk.CTkButton(top_frame, text="Refresh", command=self.load_transactions).pack(side="left", padx=5)
        ctk.CTkButton(top_frame, text="Return", command=self.go_back).pack(side="left", padx=5)
        seach_options = ["ID","Type","Ammount"]
        seachBox = ctk.CTkComboBox(top_frame, values=seach_options, state="readonly")
        seachBox.pack(side="left", padx=10)
        seachBox.set("Search by")

        seach_entry = ctk.CTkEntry(top_frame, font=("arial", 15, "bold"), width=180)
        seach_entry.pack(pady=10)

        ctk.CTkButton(top_frame, text="search").pack(side="left",padx=5)
        ctk.CTkButton(top_frame, text="show all").pack(side="left",padx=10)

        
        self.load_transactions()
    



    def load_transactions(self):
        try:
            
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="JamalMusiala42!",
                database="budget_buddy"
            )
            cursor = mydb.cursor()
            cursor.execute("SELECT id, description, reference, amount, date, type, recipient FROM transaction")
            rows = cursor.fetchall()  
    

        except mysql.connector.Error as err:
            print(f"Erreur avec la base de données : {err}")
    def delete_transaction(self):
        """Delete a transaction  based on ID."""
        transaction_id = self.id_entry.get()  

        if not transaction_id:
            print("Veuillez entrer un ID valide.")
            return
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="JamalMusiala42!",
                database="budget_buddy"
            )
            cursor = mydb.cursor()
            cursor.execute("DELETE FROM transaction WHERE id = %s", (transaction_id,))
            mydb.commit()

            if cursor.rowcount > 0:
                print(f"Transaction with ID {transaction_id} delete with succes")
                self.load_transactions()  
            else:
                print(f"None transaction find with ID {transaction_id}.")
        except mysql.connector.Error as err:
            print(f"Error with the database : {err}")

            mydb.close()


    def go_back(self):
        self.scrollable_frame.destroy()
        from welcome_page import Welcome
        Welcome(self.root)
    


if __name__ == "__main__":
    app = ctk.CTk()
    Historic(app)
    app.mainloop()
