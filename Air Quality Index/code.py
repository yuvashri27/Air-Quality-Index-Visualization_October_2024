import os
import streamlit as st

# Inject custom CSS for background color
def add_background_color(color):
    css = f"""
    <style>
    .stApp {{
        background-color: {color};
        color: black; /* Optional: Set text color to black for better visibility */
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


def login_page():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        valid_users = {"your_username": "123"}  # Replace with secure storage
        if username in valid_users and valid_users[username] == password:
            st.session_state.authenticated = True
        else:
            st.error("Incorrect username or password")


def dashboard():
    st.title("Dashboard")
    dashboard_url = """<iframe title="AQI" width="1024" height="612" 
    src="https://app.powerbi.com/view?r=eyJrIjoiN2VhNGQyZmYtOTljMi00YTQ2LTgwM2ItNDg5MGNhYmUxNzRhIiwidCI6ImRkZmNiNjk0LThiMzQtNDIxZi04ZWYyLThiOGE4NDA5MDM2YiJ9" 
    frameborder="0" allowFullScreen="true"></iframe>"""
    st.components.v1.html(dashboard_url, width=1024, height=612)

    pbix_path = "AQI.pbix"  # Replace with your .pbix file path
    if os.path.exists(pbix_path):
        with open(pbix_path, "rb") as file:
            st.download_button(
                label="Download Power BI Report as PBIX",
                data=file.read(),
                file_name="AQI.pbix",
                mime="application/octet-stream",
            )
    else:
        st.warning("PBIX file not found!")

    if st.button("Logout"):
        st.session_state.authenticated = False


# Initialize session state
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

# Add background color
add_background_color("#ADD8E6")  # Light blue background

# Render the appropriate page
if not st.session_state.authenticated:
    login_page()
else:
    dashboard()
