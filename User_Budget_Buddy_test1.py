import pyodbc
import bcrypt
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Alfr3d",
    database="budget_buddy"
)
cursor = conn.cursor()

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(password, hashed_password):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

def register():
    """New user and checks."""
    first_name = input("First Name: ").strip()
    last_name = input("Last Name: ").strip()
    email = input("Email: ").strip()
    password = input("Password: ").strip()
    
    if not (first_name and last_name and email and password):
        print("Error", "Please fill in all fields.")
        return
    
    hashed_pw = hash_password(password)
    initial_balance = 1000  # Initial balance
    
    try:
        cursor.execute("INSERT INTO user (first_name, last_name, email, password, balance) VALUES (%s, %s, %s, %s, %s)", 
                       (first_name, last_name, email, hashed_pw, initial_balance))
        conn.commit()
        print("Account created successfully!")
    except pyodbc.IntegrityError:
        print("Error: This email is already in use.")
    except Exception as e:
        print(f"Error during registration: {e}")

def login():
    """Login info verification."""
    email = input("Email: ").strip()
    password = input("Password: ").strip()
    
    if not (email and password):
        print("Error: Please fill in all fields.")
        return
    
    try:
        query = "SELECT password, balance FROM user WHERE email = %s"
        print(f"Executing query: {query} with email={email}")  # Debug
        cursor.execute(query, (email,))
        result = cursor.fetchone()
        
        if result:
            hashed_pw, balance = result
            print(f"Retrieved password: {hashed_pw}")  # Debug
        else:
            print("User not found.")
            return

        if verify_password(password, hashed_pw):
            print("Login successful!")
            print(f"Your current balance is: {balance} €")
        else:
            print("Error: Incorrect email or password.")
    except Exception as e:
        print(f"MySQL Error: {e}")

# Register or login
while True:
    print("Choose an option:")
    print("1. Register")
    print("2. Login")
    print("3. Quit")
    
    choice = input("Enter the number of your choice: ").strip()

    if choice == '1':
        register()
    elif choice == '2':
        login()
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid option, please try again.")