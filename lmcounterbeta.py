import streamlit as st
import requests

# Define the Formspree API endpoint
endpoint = "https://formspree.io/f/xwkjnzgp"

def main():
    st.header("Contact Us")

    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    submit_button = st.button("Submit")

    if submit_button:
        # Set the form data as a dictionary
        form_data = {
            "Name": name,
            "Email": email,
            "Message": message
        }

        # Send the form data using a POST request
        response = requests.post(endpoint, data=form_data)

        # Check if the request was successful and display appropriate message
        if response.status_code == 200:
            st.success("Message sent successfully!")
        else:
            st.error("Error sending message. Please try again.")

if __name__ == "__main__":
    main()
