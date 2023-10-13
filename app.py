import streamlit as st
from cryptography.fernet import Fernet

st.title("Text Encryption and Decryption")

# Generate or load the encryption key
def generate_key():
    return Fernet.generate_key()

def load_key():
    try:
        return open("secret.key", "rb").read()
    except:
        return generate_key()

key = load_key()
fernet = Fernet(key)

st.sidebar.subheader("Actions")
action = st.sidebar.radio("Choose an action:", ("Encrypt", "Decrypt"))

if action == "Encrypt":
    st.subheader("Encryption")
    text = st.text_area("Enter the text to encrypt:")
    if st.button("Encrypt"):
        if text:
            encrypted_text = fernet.encrypt(text.encode()).decode()
            st.write("Encrypted Text:")
            st.write(encrypted_text)

if action == "Decrypt":
    st.subheader("Decryption")
    text = st.text_area("Enter the text to decrypt:")
    if st.button("Decrypt"):
        if text:
            try:
                decrypted_text = fernet.decrypt(text.encode()).decode()
                st.write("Decrypted Text:")
                st.write(decrypted_text)
            except Exception as e:
                st.write("Error: " + str(e))

# Add an option to generate a new encryption key
if st.sidebar.button("Generate New Key"):
    key = generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    st.sidebar.success("A new encryption key has been generated and saved.")

# Display the encryption key (for demonstration purposes)
st.sidebar.subheader("Encryption Key")
st.sidebar.code(key)

st.write("Note: This app uses Fernet encryption to encrypt and decrypt text.")
