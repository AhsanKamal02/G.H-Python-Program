import streamlit as st
from cryptography.fernet import Fernet, InvalidToken

# Generate a key for encryption/decryption
def generate_key():
    return Fernet.generate_key()

# Initialize session state variables
if 'data_store' not in st.session_state:
    st.session_state.data_store = {}
if 'fail_count' not in st.session_state:
    st.session_state.fail_count = 0
if 'authorized' not in st.session_state:
    st.session_state.authorized = False
if 'fernet_keys' not in st.session_state:
    st.session_state.fernet_keys = {}
if 'max_failures' not in st.session_state:
    st.session_state.max_failures = 3
if 'page' not in st.session_state:
    st.session_state.page = "login"

def login():
    st.title("Secure Data Storage Login")
    st.write("Please enter your passkey to access the system.")
    passkey = st.text_input("Passkey", type="password")
    if st.button("Login"):
        if passkey:
            st.session_state.authorized = True
            st.session_state.fail_count = 0
            st.session_state.current_passkey = passkey
            if passkey not in st.session_state.fernet_keys:
                key = Fernet.generate_key()
                fernet = Fernet(key)
                st.session_state.fernet_keys[passkey] = fernet
            st.session_state.page = "main"
        else:
            st.error("Passkey cannot be empty.")

def store_data():
    st.header("Store Data")
    data = st.text_area("Data to encrypt and store")
    passkey = st.text_input("Enter a unique passkey to store this data", type="password")
    if st.button("Store Data"):
        if not data.strip():
            st.error("Data cannot be empty.")
            return
        if not passkey:
            st.error("Passkey cannot be empty.")
            return
        if passkey in st.session_state.data_store:
            st.warning("Warning: This passkey already exists, the data will be overwritten with the new data.")
        if passkey not in st.session_state.fernet_keys:
            key = Fernet.generate_key()
            fernet = Fernet(key)
            st.session_state.fernet_keys[passkey] = fernet
        else:
            fernet = st.session_state.fernet_keys[passkey]
        encrypted_data = fernet.encrypt(data.encode('utf-8'))
        st.session_state.data_store[passkey] = encrypted_data
        st.success("Data stored securely with your passkey.")

def retrieve_data():
    st.header("Retrieve Data")
    passkey = st.text_input("Enter your passkey to decrypt data", type="password")
    if st.button("Retrieve Data"):
        if not passkey:
            st.error("Passkey is required to decrypt data.")
            return
        if passkey not in st.session_state.data_store:
            st.error("No data found for the provided passkey.")
            st.session_state.fail_count += 1
            check_failures()
            return
        try:
            fernet = st.session_state.fernet_keys.get(passkey)
            if not fernet:
                st.error("Decryption key unavailable for this passkey.")
                st.session_state.fail_count += 1
                check_failures()
                return
            decrypted_data = fernet.decrypt(st.session_state.data_store[passkey]).decode('utf-8')
            st.success("Data decrypted successfully:")
            st.code(decrypted_data)
            st.session_state.fail_count = 0
        except InvalidToken:
            st.error("Invalid passkey or corrupted data - decryption failed.")
            st.session_state.fail_count += 1
            check_failures()

def check_failures():
    if st.session_state.fail_count >= st.session_state.max_failures:
        st.warning(f"Maximum failed attempts reached ({st.session_state.max_failures}). Reauthorization required.")
        st.session_state.authorized = False
        st.session_state.fail_count = 0
        st.session_state.page = "login"

def main():
    st.set_page_config(page_title="Secure Data Storage", page_icon="🔐")
    if st.session_state.page == "login":
        login()
    elif st.session_state.page == "main":
        if st.session_state.authorized:
            st.sidebar.title("Navigation")
            choice = st.sidebar.radio("Go to:", ["Store Data", "Retrieve Data", "Logout"])
            if choice == "Store Data":
                store_data()
            elif choice == "Retrieve Data":
                retrieve_data()
            elif choice == "Logout":
                st.session_state.authorized = False
                st.session_state.fail_count = 0
                st.info("You have been logged out.")
                st.session_state.page = "login"
        else:
            st.session_state.page = "login"  # Redirect to login if not authorized

if __name__ == "__main__":
    main()