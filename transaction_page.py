import customtkinter as ctk
from add_transaction import Addtransaction


class TransactionPage:
    def __init__(self, root):
        self.root = root
        self.root.title('Transactions')
        self.root.geometry("600x400")  

        self.frame = ctk.CTkFrame(master=root)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.setup_transaction_page()

    def setup_transaction_page(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

 
        self.title_label = ctk.CTkLabel(master=self.frame, text="Transactions", font=("Arial", 24, "bold"))
        self.title_label.pack(pady=10)

      
        button_frame = ctk.CTkFrame(self.frame)
        button_frame.pack(pady=20)

        self.add_button = ctk.CTkButton(master=button_frame, text="Add a Transaction", command=self.open_add_transaction)
        self.add_button.pack(side="left", padx=10)

        self.back_button = ctk.CTkButton(master=button_frame, text="Return", command=self.go_back_to_welcome)
        self.back_button.pack(side="left", padx=10)


    def go_back_to_welcome(self):
        self.frame.destroy()
        from welcome_page import Welcome
        Welcome(self.root)
    
    def open_add_transaction(self):
        self.frame.destroy()
        Addtransaction(self.root)


    
       

