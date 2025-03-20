import customtkinter as ctk
import mysql.connector
from add_transaction import Addtransaction


class TransactionPage:
    def __init__(self,root):
        self.root = root
        self.root.title('Transactions')
        self.root.geometry("400x300")

        self.frame = ctk.CTkFrame(master=root)
        self.frame.pack(pady=20, padx=20,fill="both", expand=True)

        self.setup_transaction_page()
    def setup_transaction_page(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        self.left_label = ctk.CTkLabel(master=self.frame, text="Transaction", font=("Arial",18,"bold"),width=100,height=50,anchor="n")
        self.left_label.pack(side="left",padx=20, pady=5)
        
        self.back_button = ctk.CTkButton(master=self.frame, text="Return",command=self.go_back_to_welcome)
        self.back_button.pack(side="bottom", anchor = "sw", padx=10,pady=10)

        self.add_button = ctk.CTkButton(master=self.frame, text="Add  Transaction", command=self.open_add_transaction)
        self.add_button.pack(side="top", padx=10,pady=10)

    def go_back_to_welcome(self):
        self.frame.destroy()
        from welcome_page import Welcome
        Welcome(self.root)
    
    def open_add_transaction(self):
        self.frame.destroy()
        Addtransaction(self.root)


    
       

