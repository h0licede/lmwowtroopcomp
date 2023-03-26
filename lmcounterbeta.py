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

st.title("Troop Suggestion App")

# Load the data from data.txt into a dictionary
data = {}
with open("data.txt", "r") as f:
    for line in f:
        enemy_composition, enemy_formation, suggested_composition, suggested_formation = line.strip().split(",")
        key = (enemy_composition, enemy_formation)
        value = (suggested_composition, suggested_formation)
        if key not in data:
            data[key] = []
        data[key].append(value)

# Get user input
enemy_composition = st.text_input("Enemy Troop Composition (3 digits)")
enemy_formation_options = ["Infantry Phalanx", "Ranged Phalanx", "Cavalry Phalanx", "Infantry Wedge", "Ranged Wedge", "Cavalry Wedge"]
enemy_formation = st.selectbox("Enemy Troop Formation", enemy_formation_options)

# Search for matching results
if enemy_composition.isdigit() and len(enemy_composition) == 3:
    key = (enemy_composition, enemy_formation)
    if key in data:
        st.write("Suggested Troop Compositions and Formations:")
        for value in data[key]:
            st.write(f"- {value[0]} - {value[1]}")
    else:
        st.write("No matching results found.")
else:
    st.write("Please enter a valid 3-digit enemy troop composition.")

