import streamlit as st
import pandas as pd
import datetime
import os
import time # Import time module for a small delay

# --- Configuration ---
CSV_FILE = 'login_records.csv'
VALID_USERS = {
    "user1": "pass1",
    "admin": "adminpass"
}

# IMPORTANT: Replace with the actual URL of your Butterfly apps web page
BUTTERFLY_APP_URL = "https://winjher.github.io/jerapp/home.html"
# If it's a local HTML file you want to serve, you might need
# to set up a static file server or use st.components.v1.html for embed.
# This assumes it's an external URL.

# --- Functions for CSV handling ---
def initialize_csv():
    """Creates the CSV file with headers if it doesn't exist."""
    if not os.path.exists(CSV_FILE):
        df = pd.DataFrame(columns=["timestamp", "username", "status"])
        df.to_csv(CSV_FILE, index=False)

def record_login_attempt(username, status):
    """Records a login attempt to the CSV file."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_record = pd.DataFrame([{
        "timestamp": timestamp,
        "username": username,
        "status": status
    }])
    new_record.to_csv(CSV_FILE, mode='a', header=False, index=False)

def get_login_records():
    """Reads all login records from the CSV file."""
    if os.path.exists(CSV_FILE):
        return pd.read_csv(CSV_FILE)
    return pd.DataFrame(columns=["timestamp", "username", "status"])

# --- Streamlit App ---
st.set_page_config(page_title="Streamlit Login App", layout="centered")
st.title("Simple Streamlit Login")

initialize_csv()

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in VALID_USERS and VALID_USERS[username] == password:
            st.success(f"Welcome, {username}!")
            st.session_state['logged_in'] = True
            st.session_state['username'] = username # Store username
            record_login_attempt(username, "SUCCESS")

            # --- REDIRECTION LOGIC HERE ---
            if BUTTERFLY_APP_URL:
                # Use st.markdown with HTML and JavaScript for redirection
                # This will open in the current tab
                st.markdown(f"""
                    <script>
                        window.location.href = "{BUTTERFLY_APP_URL}";
                    </script>
                    """, unsafe_allow_html=True)
                
                # Alternatively, to open in a new tab:
                # st.markdown(f"""
                #     <script>
                #         window.open("{BUTTERFLY_APP_URL}", "_blank");
                #     </script>
                #     """, unsafe_allow_html=True)
                
                # Add a small delay to allow the script to execute before rerun
                time.sleep(0.1)
                #st.experimental_rerun() # Rerun to ensure the script executes
            else:
                st.experimental_rerun() # Rerun to show logged-in content
        else:
            st.error("Invalid username or password.")
            record_login_attempt(username, "FAILURE")
else:
    st.success(f"You are logged in as {st.session_state.get('username', 'User')}.")
    st.subheader("Welcome to the Protected Area!")
    st.write("This is content only accessible after successful login.")
    st.write(f"You can now proceed to your [Butterfly Apps]({BUTTERFLY_APP_URL}) page.")
    st.write("---")

    st.subheader("Login Records")
    records_df = get_login_records()
    if not records_df.empty:
        st.dataframe(records_df)
        
        csv_data = records_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Login Records CSV",
            data=csv_data,
            file_name="login_records.csv",
            mime="text/csv",
            key="download_records_csv"
        )
    else:
        st.info("No login records yet.")

    if st.button("Logout"):
        st.session_state['logged_in'] = False
        del st.session_state['username']
        st.experimental_rerun()