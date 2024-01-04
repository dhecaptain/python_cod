import streamlit as st

def app():
    st.title("ST PETERS CLAVERS SECONDARY SCHOOL WEBSITE")
    st.subheader("login")
    menu = ["Home", "About", "Blog"]
    choice = st.sidebar.selectbox("Select a page", menu)
    if choice == "Home":
        st.write("Welcome to the login page!")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if username == "admin" and password == "password":
                st.success("Logged in as admin.")
            else:
                st.error("Invalid username or password.")
        st.write("Don't have an account? Register below.")
        new_username = st.text_input("New username")
        new_password = st.text_input("New password", type="password")
        if st.button("Register"):
            # Add code to register new user
            st.success(f"User {new_username} registered successfully!")
    elif choice == "About":
        st.write("This is the about page.")
    elif choice == "Blog":
        st.write("This is the blog page.")

if __name__ == "__main__":
    app()
