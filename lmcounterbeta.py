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

def read_data_file(file_path):
    """
    Reads the data file and returns a dictionary of lists containing
    the troop compositions and formations.
    """
    data_dict = {}
    with open(file_path, "r") as f:
        for line in f:
            comps, formation = line.strip().split(",")
            if comps not in data_dict:
                data_dict[comps] = []
            data_dict[comps].append(formation)
    return data_dict

def main():
    st.header("Troop Composition Finder")

    # Read data file and store the troop compositions and formations in a dictionary
    data_dict = read_data_file("data.txt")

    # Get user input for enemy troop composition and formation
    enemy_comps = st.text_input("Enemy Troop Composition (3 digits)", max_chars=3)
    enemy_formation = st.selectbox("Enemy Troop Formation", ["Infantry Phalanx", "Ranged Phalanx", "Cavalry Phalanx", "Infantry Wedge", "Ranged Wedge", "Cavalry Wedge"])

    # Show suggested troop compositions and formations
    if st.button("Search"):
        # Check if enemy troop composition exists in the data dictionary
        if enemy_comps in data_dict:
            st.success(f"Suggested Troop Composition: {enemy_comps}")
            st.write("Suggested Troop Formations:")
            for formation in data_dict[enemy_comps]:
                st.write(formation)
        else:
            st.error("Enemy Troop Composition not found in data file")

if __name__ == "__main__":
    main()
