import streamlit as st

# Example credentials (in-memory for simplicity)
CREDENTIALS = {
    "user1": "password1",
    "user2": "password2"
}

def register(username, password):
    """Register a new user by adding their credentials to the store."""
    if username in CREDENTIALS:
        return False  # User already exists
    CREDENTIALS[username] = password
    return True

def main():
    st.title("Sign In")

    new_username = st.text_input("New Username")
    new_password = st.text_input("New Password", type="password")
    sign_in_button = st.button("Sign in")

    if sign_in_button:
        if register(new_username, new_password):
            st.success("Registration successful! Please log in.")
            if st.button("Go to Log In page"):
                st.session_state.page = "login"
                st.experimental_rerun()
        else:
            st.error("Username already exists. Please choose another.")

if __name__ == "__main__":
    if "page" not in st.session_state:
        st.session_state.page = "sign_in"
    if st.session_state.page == "sign_in":
        main()
    elif st.session_state.page == "login":
        import login
        login.main()
