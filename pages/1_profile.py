import streamlit as st

# Custom CSS styling
st.markdown("""
<style>
/* Global body styling */
body {
  background-color: #f0f2f6;
}

/* Title styling */
h1, h2, h3 {
  font-family: 'Roboto', sans-serif;
  color: #333;
  text-align: center;
}

/* Styling for text inputs */
div.stTextInput > div > div > input {
  border: 2px solid #ccc;
  border-radius: 5px;
  padding: 10px 20px;
  font-size: 16px;
}

/* Button styling */
div.stButton > button {
  background-color: #4CAF50;
  color: white;
  border-radius: 5px;
  border: none;
  padding: 10px 20px;
  font-size: 16px;
  transition: background-color 0.3s ease;
}
div.stButton > button:hover {
  background-color: #45a049;
}

/* Sidebar styling */
div[data-testid="stSidebar"] {
  background-color: #ffffff;
  padding: 20px;
  border-right: 1px solid #e6e6e6;
}

/* Alert message styling */
div.stAlert {
  font-family: 'Roboto', sans-serif;
  font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

# Simulated user database (for demo purposes only)
if "users" not in st.session_state:
    st.session_state.users = {"testuser": {"password": "testpass"}}
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        # Check if username exists and password matches
        if username in st.session_state.users and st.session_state.users[username]["password"] == password:
            st.success("Logged in successfully!")
            st.session_state.logged_in = True
        else:
            st.error("Invalid username or password.")

def register():
    st.title("Register")
    new_username = st.text_input("Choose a Username", key="new_username")
    new_password = st.text_input("Choose a Password", type="password", key="new_password")
    confirm_password = st.text_input("Confirm Password", type="password", key="confirm_password")
    
    if st.button("Register"):
        if new_username in st.session_state.users:
            st.error("Username already exists. Please choose another one.")
        elif new_password != confirm_password:
            st.error("Passwords do not match. Please try again.")
        else:
            # Save the new user
            st.session_state.users[new_username] = {"password": new_password}
            st.success("Registration successful! Please go to Login.")

def main():
    menu = st.sidebar.selectbox("Menu", ["Login", "Register"])
    
    if st.session_state.logged_in:
        st.write("Welcome, you're logged in!")
        # Your main app content goes here...
    else:
        if menu == "Login":
            login()
        elif menu == "Register":
            register()

if __name__ == "__main__":
    main()
