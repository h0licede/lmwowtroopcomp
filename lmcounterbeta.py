import streamlit as st
import requests

# Define the Formspree API endpoint
endpoint = "https://formspree.io/f/xwkjnzgp"

def main():
    st.header("Contact Us")

    # Add input fields for enemy troop composition and suggested troop composition
    st.subheader("Enemy Troop Composition")
    enemy_comp = st.number_input("Enter a 3-digit number for the enemy troop composition", min_value=100, max_value=999, step=1)
    st.subheader("Suggested Troop Composition")
    suggested_comp = st.number_input("Enter a 3-digit number for the suggested troop composition", min_value=100, max_value=999, step=1)

    # Add dropdown lists for enemy troop formation and suggested troop formation
    st.subheader("Enemy Troop Formation")
    enemy_form = st.selectbox("Select the enemy troop formation", ["Infantry Phalanx", "Ranged Phalanx", "Cavalry Phalanx", "Infantry Wedge", "Ranged Wedge", "Cavalry Wedge"])
    st.subheader("Suggested Troop Formation")
    suggested_form = st.selectbox("Select the suggested troop formation", ["Infantry Phalanx", "Ranged Phalanx", "Cavalry Phalanx", "Infantry Wedge", "Ranged Wedge", "Cavalry Wedge"])

    submit_button = st.button("Submit")

    if submit_button:
        # Set the form data as a dictionary
        form_data = {
            "Enemy Troop Composition": enemy_comp,
            "Enemy Troop Formation": enemy_form,
            "Suggested Troop Composition": suggested_comp,
            "Suggested Troop Formation": suggested_form
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
