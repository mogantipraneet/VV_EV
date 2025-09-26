import streamlit as st
import json
from pathlib import Path
# You will need to import your login_user function if you use auto-login
# from .login import login_user 

# Path to JSON file
DATA_FILE = Path("data/user.json")

# This top-level loading is still good for the rest of the app
if "users" not in st.session_state:
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            st.session_state.users = json.load(f)
    else:
        st.session_state.users = {}

# MODIFIED: This function now accepts the data to save as an argument
def save_users_to_file(users_data):
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(users_data, f, indent=4)

# MODIFIED: The registration logic is now self-contained and safer
def register_user(name, email, password, car_number):
    # Step 1: Always read the latest user data from the file
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            try:
                current_users = json.load(f)
            except json.JSONDecodeError:
                current_users = {} # File is empty or corrupted
    else:
        current_users = {}

    # Step 2: Check if user exists in the data we just loaded
    if email in current_users:
        return False, "User already exists!"
    
    # Step 3: Add the new user to the dictionary
    # Storing vehicles in a list is more flexible
    current_users[email] = {
        "name": name,
        "password": password, # IMPORTANT: Remember to hash this password!
        "vehicles": [car_number.strip()] if car_number else []
    }
    
    # Step 4: Save the complete, updated dictionary back to the file
    save_users_to_file(current_users)
    
    # Step 5: Also update the current session's state to match
    st.session_state.users = current_users
    
    return True, "Registration successful!"

def register_form():
    st.subheader("Register")
    name = st.text_input("Name", key="reg_name")
    email = st.text_input("Email", key="reg_email")
    password = st.text_input("Password", type="password", key="reg_password")
    car_number = st.text_input("Car Number", key="reg_car_number")

    if st.button("Register"):
        # The function call remains the same
        success, msg = register_user(name, email, password, car_number)
        
        if success:
            st.success(msg)
            # You might want to auto-login here or just show the success message
        else:
            st.error(msg)