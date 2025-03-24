import customtkinter as ctk
import mysql.connector
import bcrypt
from tkinter import messagebox
import re

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Alfr3d",
    database="budget_buddy"
)

cursor = conn.cursor()
root = ctk.CTk()
#icon = PhotoImage(file="icons8-finance-64.png")  
#root.iconphoto(True, icon)
root.title("Connexion")
root.geometry("300x500")

welcome_label = ctk.CTkLabel(master=root, text="Budget buddy", font=("Arial", 20, "bold"))
welcome_label.pack(pady=20, padx=20)

page_frame = ctk.CTkFrame(master=root, width=250, height=470, corner_radius=10)
page_frame.place(x=25, y=160)

def is_valid_email(email): 
    email_regex = r"(^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$)"
    return re.match(email_regex, email) is not None

def password_valid(password):
    if len(password)>10:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[!@#%^&*,.()?":{}|<>]', password):
        return False
    return True

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(password, hashed_password):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

def switch_option(switch_to):
    """function for switch to the signup or login"""
    for widget in page_frame.winfo_children():
        widget.destroy()
    if switch_to == 'login':
        login_page_option.configure(fg_color="#1F6AA5", text_color="white")
        signup_page_option.configure(fg_color="white", text_color="black")
        login_page()
    else:
        signup_page_option.configure(fg_color="#1F6AA5", text_color="white")
        login_page_option.configure(fg_color="white", text_color="black")
        signup_page()

login_page_option = ctk.CTkButton(master=root, text="Login", font=("Bold", 20),
                                  width=120, height=40, text_color="white",
                                  corner_radius=10, border_width=2, border_color="white",
                                  hover=False, command=lambda: switch_option('login'))
login_page_option.place(x=25, y=100)

signup_page_option = ctk.CTkButton(master=root, text="Signup", font=("Bold", 20),
                                   width=120, height=40, fg_color="white",
                                   text_color="black", corner_radius=10, border_width=2,
                                   border_color="white", hover=False, command=lambda: switch_option('signup'))
signup_page_option.place(x=155, y=100)

page_frame = ctk.CTkFrame(master=root, width=250, height=470, corner_radius=10)
page_frame.place(x=25, y=160)

def login_page():
    """function for the login interface"""
    ctk.CTkLabel(master=page_frame, text="Login Page", font=("Bold", 25)).place(x=50, y=10)

    email_entry = ctk.CTkEntry(master=page_frame, width=230, height=35, placeholder_text="exemple@gmail.com",
                               border_color="#3B8ED0", border_width=2, corner_radius=10)
    email_entry.place(x=10, y=80)

    password_entry = ctk.CTkEntry(master=page_frame, width=230, height=35, placeholder_text="password",
                                  border_color="#3B8ED0", border_width=2, corner_radius=10, show="*")
    password_entry.place(x=10, y=150)

    def login():
        email = email_entry.get().strip()
        password = password_entry.get().strip()
        
        if not email or not password:
            messagebox.showerror("Error", "Please fill in all fields.")
            return
        
        if not is_valid_email(email):
            messagebox.showerror("Error", "Please enter a valid email.")
            return

        try:
            cursor.execute("SELECT password, balance FROM user WHERE email = %s", (email,))
            result = cursor.fetchone()
            
            if result:
                hashed_pw, balance = result
                if verify_password(password, hashed_pw):
                    messagebox.showinfo("Success", f"Login successful!\nBalance: {balance} €")
                else:
                    messagebox.showerror("Error", "Incorrect email or password.")
            else:
                messagebox.showerror("Error", "User not found.")
        except Exception as e:
            messagebox.showerror("Error MySQL", str(e))

    login_button = ctk.CTkButton(master=page_frame, text="Login", font=("Bold", 20),
                                 width=200, height=40, text_color="white",
                                 corner_radius=10, hover=False, command=login)
    login_button.place(x=25, y=230)
    
def signup_page():
    """function for the signup interface"""
    ctk.CTkLabel(master=page_frame, text="Signup Page", font=("Bold", 25)).place(x=50, y=10)

    name_entry = ctk.CTkEntry(master=page_frame, width=230, height=35, placeholder_text="Name",
                               border_color="#3B8ED0", border_width=2, corner_radius=10)
    name_entry.place(x=10, y=10)

    last_name_entry = ctk.CTkEntry(master=page_frame, width=230, height=35, placeholder_text="Last Name",
                               border_color="#3B8ED0", border_width=2, corner_radius=10)
    last_name_entry.place(x=10, y=60)

    email_entry = ctk.CTkEntry(master=page_frame, width=230, height=35, placeholder_text="exemple@gmail.com",
                               border_color="#3B8ED0", border_width=2, corner_radius=10)
    email_entry.place(x=10, y=110)

    password_entry = ctk.CTkEntry(master=page_frame, width=230, height=35, placeholder_text="Password",
                                  border_color="#3B8ED0", border_width=2, corner_radius=10, show="*")
    password_entry.place(x=10, y=160)

    confirm_password = ctk.CTkEntry(master=page_frame, width=230, height=35, placeholder_text="Confirm Password",
                                    border_color="#3B8ED0", border_width=2, corner_radius=10, show="*")
    confirm_password.place(x=10, y=210)
    
    def register():
        name = name_entry.get().strip()
        last_name = last_name_entry.get().strip()
        email = email_entry.get().strip()
        password = password_entry.get().strip()
        confirm_pw = confirm_password.get().strip()
        
        if not email or not password or not confirm_pw:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        if not is_valid_email(email):
            messagebox.showerror("Error", "Please enter a valid email.")
            return
        if not password_valid(password):
            messagebox.showerror("Error", "Password must have at least ten characters, one uppercase letter, one lowercase letter, one number and one special character")
            return
        if password != confirm_pw:
            messagebox.showerror("Error", "Passwords do not match.")
            return
        
        hashed_pw = hash_password(password)
        solde_initial = 1000
        
        try:
            cursor.execute("INSERT INTO user (last_name, name, email, password, balance) VALUES (%s, %s, %s, %s, %s)", 
                           (last_name, name, email, hashed_pw, solde_initial))
            conn.commit()
            messagebox.showinfo("Success", "Account successfully created!")
        except mysql.connector.errors.IntegrityError:
            messagebox.showerror("Error", "This email is already in use.")
        except Exception as e:
            messagebox.showerror("Erreur MySQL", str(e))

    signup_button = ctk.CTkButton(master=page_frame, text="Signup", font=("Bold", 20),
                                  width=200, height=40, text_color="white",
                                  corner_radius=10, hover=False, command=register)
    signup_button.place(x=25, y=260)

login_page()
root.mainloop()