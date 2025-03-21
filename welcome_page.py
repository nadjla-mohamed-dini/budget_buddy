import customtkinter as ctk
from transaction_page import TransactionPage
from big_one import Historic



ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")

class Welcome:
    def __init__(self,root):
        self.root = root
        self.root.title("Budget_Buddy")
        self.root.geometry("400x300")

        self.frame = ctk.CTkFrame(master=root)
        self.frame.pack(pady=20,padx=20, fill="both", expand=True)

        self.welcome_label = ctk.CTkLabel(master=self.frame, text="Welcome back User", font=("Arial",20,"bold"))
        self.welcome_label.pack(pady=20,padx=20, fill="both", expand=True)


        self.button1 = ctk.CTkButton(master=self.frame, text="transaction", command= self.open_transaction_page)
        self.button1.place(rely=0.5,relx=0.25)
        self.button2 = ctk.CTkButton(master=self.frame, text="profil")
        self.button2.pack(pady=5, padx=10,side="top")
        self.button3 = ctk.CTkButton(master=self.frame, text="consultation", command=self.open_consultation_page)
        self.button3.pack(pady=5, padx=10,side="top")

    def open_transaction_page(self):
        self.frame.destroy()
        TransactionPage(self.root)
    def open_consultation_page(self):
        self.frame.destroy()
        Historic(self.root)
        

if __name__ == "__main__":
    app_window = ctk.CTk()
    app = Welcome(app_window)
    app_window.mainloop()