import streamlit as st
import requests

# Define the Formspree API endpoint
endpoint = "https://formspree.io/f/xwkjnzgp"

def main():
    st.header("Lords Mobile Mixed Troop Strategy")

    # Define the options for the troop formations dropdown
    troop_formations = ['Infantry Phalanx', 'Ranged Phalanx', 'Cavalry Phalanx', 'Infantry Wedge', 'Ranged Wedge', 'Cavalry Wedge']

    # Define the input fields
    enemy_composition = st.number_input("Enemy Troop Composition (3 digit number)", min_value=0, max_value=999, step=1)
    enemy_formation = st.selectbox("Enemy Troop Formation", troop_formations)
    suggested_composition = st.number_input("Suggested Troop Composition (3 digit number)", min_value=0, max_value=999, step=1)
    suggested_formation = st.selectbox("Suggested Troop Formation", troop_formations)

    submit_button = st.button("Submit")

    if submit_button:
        # Set the form data as a dictionary
        form_data = {
            "Enemy Troop Composition": enemy_composition,
            "Enemy Troop Formation": enemy_formation,
            "Suggested Troop Composition": suggested_composition,
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

    
    
import streamlit as st

def search_suggested_composition(data, enemy_composition, enemy_formation):
    for row in data:
        if row[0] == enemy_composition and row[1] == enemy_formation:
            return row[2], row[3]
    return "No suggestion found for the given enemy composition and formation.", ""

def main():
    st.header("Search for Suggested Troop Composition and Formation")

    # Load data from file
    with open("data.txt", "r") as f:
        data = [line.strip().split(",") for line in f]

    # Get user inputs
    enemy_composition = st.text_input("Enter enemy troop composition (3 digits)", max_chars=3)
    enemy_formation = st.selectbox("Select enemy troop formation", ["Infantry Phalanx", "Ranged Phalanx", "Cavalry Phalanx", "Infantry Wedge", "Ranged Wedge", "Cavalry Wedge"])
    search_button = st.button("Search")

    # Search for suggested composition and formation if search button is pressed
    if search_button:
        suggested_composition, suggested_formation = search_suggested_composition(data, enemy_composition, enemy_formation)
        st.write(f"Suggested troop composition: {suggested_composition}")
        st.write(f"Suggested troop formation: {suggested_formation}")

if __name__ == "__main__":
    main()
