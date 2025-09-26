import streamlit as st
import json
from pathlib import Path

# Path to JSON file
DATA_FILE = Path("data/user.json")

# Ensure session_state has users loaded
def login_user(email, password):
    # --- START OF FIX ---
    # Always read the latest user data from the file (the source of truth)
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            try:
                users_on_disk = json.load(f)
            except json.JSONDecodeError:
                users_on_disk = {} # Handle case where file is empty or corrupted
    else:
        users_on_disk = {}
    
    # Check credentials against the data just read from the file
    if email in users_on_disk and users_on_disk[email]["password"] == password:
        # If login is successful, THEN update the session state
        st.session_state.logged_in = True
        st.session_state.email = email
        # Also, ensure the session state's user data is up-to-date
        st.session_state.users = users_on_disk
        return True, "Login successful!"
    # --- END OF FIX ---
    
    return False, "Invalid email or password."

def login_form():
    


    st.markdown(

       """
    <style>
    /* Whole App */
    .stApp {
        background: radial-gradient(circle at top left,rgb(117, 210, 202),rgba(95, 113, 111, 0.85),rgb(76, 95, 100));
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }
    
    /* Glassmorphic Container */
    .main .block-container {
        background: rgba(245, 240, 240, 0.92); /* Transparent silver */
        backdrop-filter: blur(12px); /* Frosted glass */
        border: 1px solid rgba(225, 16, 1, 0.4);
        border-radius: 20px;
        padding: 50px 40px;
        box-shadow: 0 0 30px rgba(217, 228, 217, 0.3);
        max-width: 420px;
        margin: auto;
        animation: floatCard 6s ease-in-out infinite;
    }

    @keyframes floatCard {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-8px); }
    }

    /* Headings */
    h1, h2, h3, h4, h5, h6 {
        color: #bfffc8;
        text-shadow: 0px 0px 8px rgba(144, 238, 144, 0.8);
        text-align: center;
    }

    /* Inputs */
    .stTextInput > div > div > input {
        border: 2px solid rgba(144, 238, 144, 0.6) !important;
        border-radius: 10px;
        padding: 12px;
        background: rgba(42, 42, 42, 0.8) !important;
        color: #f1f1f1 !important;
        font-weight: 500;
        transition: all 0.3s ease-in-out;
    }
    .stTextInput > div > div > input:focus {
        border-color: #90ee90 !important;
        box-shadow: 0px 0px 15px #90ee90;
        outline: none !important;
    }

    /* Labels */
    label {
        color: #a8ffb0 !important;
        font-weight: bold;
    }

    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #90ee90, #5cd65c);
        color: #0a0a0a !important;
        border-radius: 10px;
        padding: 12px 25px;
        font-weight: bold;
        font-size: 16px;
        border: none;
        box-shadow: 0 0 20px rgba(144, 238, 144, 0.5);
        transition: all 0.3s ease-in-out;
        width: 100%;
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #a8ffb0, #77dd77);
        box-shadow: 0 0 25px #90ee90, 0 0 40px rgba(144, 238, 144, 0.8);
        transform: scale(1.05);
    }

    /* Alerts */
    .stAlert.success {
        background: rgba(144, 238, 144, 0.1);
        border-left: 5px solid #90ee90;
        color: #bfffc8;
        border-radius: 10px;
        backdrop-filter: blur(6px);
    }
    .stAlert.error {
        background: rgba(255, 100, 100, 0.1);
        border-left: 5px solid #ff4d4d;
        color: #ffcccc;
        border-radius: 10px;
        backdrop-filter: blur(6px);
    }

    /* Logo */
    .logo-container {
        text-align: center;
        margin-bottom: 25px;
    }
    .logo-container img {
        max-width: 160px;
        border-radius: 50%;
        border: 2px solidrgb(27, 31, 27);
        box-shadow: 0 0 20px rgba(144, 238, 144, 0.6);
    }
    </style>
    """,

    unsafe_allow_html=True
    )
    # --- Logo at the top ---
    st.markdown(
            """
            <div class="logo-container">
                <img src="https://iili.io/KRVRWPf.jpg" alt="LAX EV Station Logo">
            </div>
            """,
            unsafe_allow_html=True
    )

    st.subheader("Login")
    
    # Using st.form for better input management and button callback
    with st.form("login_form"):
            email = st.text_input("Email", key="login_email_form") # Unique key for form input
            password = st.text_input("Password", type="password", key="login_password_form") # Unique key for form input
            
            # Every form must have a submit button
            submitted = st.form_submit_button("Login", use_container_width=True)

            if submitted:
                success, msg = login_user(email, password)
                
                if success:
                    st.success(msg) # Streamlit's default success looks good with this theme
                    st.rerun()
                else:
                    st.error(msg) # Streamlit's default error looks good with this theme