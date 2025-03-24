
import customtkinter as ctk
from tkinter import messagebox
import mysql.connector


class ProfilePage:
    def __init__(self, root, return_to_main, user_id):
        """Init the profil page"""
        self.root = root
        self.return_to_main = return_to_main
        self.user_id = user_id

        
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  
            database="budget_buddy"  
        )
        self.cursor = self.db.cursor()

        
        self.frame = ctk.CTkFrame(master=self.root)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        #
        self.title_label = ctk.CTkLabel(
            master=self.frame,
            text="Profil Utilisateur",
            font=("Arial", 20, "bold"),
        )
        self.title_label.pack(pady=20, padx=20)

        
        self.first_name_label = ctk.CTkLabel(master=self.frame, text="Name :")
        self.first_name_label.pack(pady=5, padx=10)
        self.first_name_entry = ctk.CTkEntry(master=self.frame, width=200)
        self.first_name_entry.pack(pady=5, padx=10)

        self.last_name_label = ctk.CTkLabel(master=self.frame, text="Last name :")
        self.last_name_label.pack(pady=5, padx=10)
        self.last_name_entry = ctk.CTkEntry(master=self.frame, width=200)
        self.last_name_entry.pack(pady=5, padx=10)

        self.email_label = ctk.CTkLabel(master=self.frame, text="Email :")
        self.email_label.pack(pady=5, padx=10)
        self.email_entry = ctk.CTkEntry(master=self.frame, width=200)
        self.email_entry.pack(pady=5, padx=10)

        self.password_label = ctk.CTkLabel(master=self.frame, text="*********")
        self.password_label.pack(pady=5, padx=10)
        self.password_entry = ctk.CTkEntry(master=self.frame, width=200, show="*********")
        self.password_entry.pack(pady=5, padx=10)

        # Bouton pour enregistrer les modifications
        self.save_button = ctk.CTkButton(
            master=self.frame,
            text="Save",
            command=self.save_profile,
        )
        self.save_button.pack(pady=20, padx=10)

        
        self.return_button = ctk.CTkButton(
            master=self.frame,
            text="Return",
            command=self.return_to_main,
        )
        self.return_button.pack(pady=10, padx=10)

        
        self.load_profile()

    def load_profile(self):
        
        try:
            
            query = "SELECT first_name, last_name, email, password FROM users WHERE id = %s"
            self.cursor.execute(query, (self.user_id,))
            result = self.cursor.fetchone()

            if result:
                
                self.first_name_entry.insert(0, result[0])  
                self.last_name_entry.insert(0, result[1])  
                self.email_entry.insert(0, result[2])  
                self.password_entry.insert(0, result[3])  
            else:
                messagebox.showwarning("Error", "no user find.")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error whith the database : {err}")

    def save_profile(self):

        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        
        if not first_name or not last_name or not email or not password:
            messagebox.showwarning("Error", "Fill every champs.")
            return

        try:
         
            query = """
                UPDATE users
                SET first_name = %s, last_name = %s, email = %s, password = %s
                WHERE id = %s
            """
            self.cursor.execute(query, (first_name, last_name, email, password, self.user_id))
            self.db.commit()

            messagebox.showinfo("Success", "Profil update !")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error with the database: {err}")

    def return_to_main(self):

        self.frame.destroy()  
        self.return_to_main()  

    def __del__(self):

        if hasattr(self, "cursor"):
            self.cursor.close()
        if hasattr(self, "db"):
            self.db.close()