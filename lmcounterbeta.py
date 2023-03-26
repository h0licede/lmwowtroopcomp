import streamlit as st
import requests

# Define the Formspree API endpoint
endpoint = "https://formspree.io/f/xwkjnzgp"

def main():
    st.header("Contact Us")

    # Define the composition input fields
    st.subheader("Enemy Troop Composition")
    enemy_comp = st.number_input("Enter a 3-digit number", min_value=0, max_value=999, value=0, step=1, format="%d")
    suggested_comp = st.number_input("Enter a 3-digit number", min_value=0, max_value=999, value=0, step=1, format="%d")

    # Define the formation dropdown fields
    st.subheader("Enemy Troop Formation")
    enemy_formation = st.selectbox("", ["Infantry Phalanx", "Ranged Phalanx", "Cavalry Phalanx", "Infantry Wedge", "Ranged Wedge", "Cavalry Wedge"])
    suggested_formation = st.selectbox("", ["Infantry Phalanx", "Ranged Phalanx", "Cavalry Phalanx", "Infantry Wedge", "Ranged Wedge", "Cavalry Wedge"])

    submit_button = st.button("Submit")

    if submit_button:
        # Set the form data as a dictionary
        form_data = {
            "Enemy Troop Composition": enemy_comp,
            "Enemy Troop Formation": enemy_formation,
            "Suggested Troop Composition": suggested_comp,
            "Suggested Troop Formation": suggested_formation
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
