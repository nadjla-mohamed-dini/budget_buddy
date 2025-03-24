import customtkinter as ctk
from transaction_page import TransactionPage
from another import Historic
from profile_page import ProfilePage
from tkinter import messagebox


ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")


class Welcome:
    def __init__(self, root):
        self.root = root
        self.root.title("Budget_Buddy")
        self.root.geometry("400x300")

        self.frame = ctk.CTkFrame(master=root)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.welcome_label = ctk.CTkLabel(master=self.frame, text="Welcome", font=("Arial", 20, "bold"))
        self.welcome_label.pack(pady=20, padx=20, fill="both", expand=True)

        self.account_button = ctk.CTkButton(master=self.frame, text="Account", command=self.switch_account)
        self.account_button.pack(pady=5, padx=10, side="top")

        self.button1 = ctk.CTkButton(master=self.frame, text="Transaction", command=self.open_transaction_page)
        self.button1.pack(pady=5, padx=10, side="top")

        self.button2 = ctk.CTkButton(master=self.frame, text="Profil",command=self.open_profile_page)
        self.button2.pack(pady=5, padx=10, side="top")

        self.button3 = ctk.CTkButton(master=self.frame, text="Consultation", command=self.open_consultation_page)
        self.button3.pack(pady=5, padx=10, side="top")


        self.accounts = ["Compte 1", "Compte 2"]  
        self.current_account = self.accounts[0]  

    def switch_account(self):
        """Switch between accounts."""

        account_dialog = ctk.CTkInputDialog(
            title="Change account",
            text=f"Actual account : {self.current_account}\nChoose an account :",
        )
        account_dialog.geometry("300x200")  


        account_choice = account_dialog.get_input()

        if account_choice and account_choice in self.accounts:
            self.current_account = account_choice
            self.welcome_label.configure(text=f"Welcome back User ({self.current_account})")
            messagebox.showinfo("Success", f"Account change for : {self.current_account}")
        else:
            messagebox.showwarning("Error", "Invalide account or no select.")

    def open_transaction_page(self):
        
        self.frame.destroy()
        TransactionPage(self.root)

    def open_consultation_page(self):
        
        self.frame.destroy()
        Historic(self.root)
    def open_profile_page(self):
        
        self.frame.destroy() 
        ProfilePage(self.root, self.return_to_main)

    def return_to_main(self):

        self.frame.destroy()  
        Welcome(self.root) 


if __name__ == "__main__":
    app_window = ctk.CTk()
    app = Welcome(app_window)
    app_window.mainloop()