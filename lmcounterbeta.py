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

def main():
    st.header("Troop Suggestions")

    # Read data from the data file
    with open("data.txt", "r") as f:
        data = f.readlines()

    # Create a dictionary to store the data
    troop_data = {}
    for entry in data:
        entry = entry.strip().split(",")
        enemy_comp = entry[0]
        enemy_form = entry[1]
        suggested_comp = entry[2]
        suggested_form = entry[3]
        troop_data[(enemy_comp, enemy_form)] = (suggested_comp, suggested_form)

    # Create the search form
    st.subheader("Search Enemy Troop Composition and Formation")
    enemy_comp = st.number_input("Enter Enemy Troop Composition (3-digit number)", min_value=0, max_value=999, step=1)
    enemy_form = st.selectbox("Enter Enemy Troop Formation", ["Infantry Phalanx", "Ranged Phalanx", "Cavalry Phalanx", "Infantry Wedge", "Ranged Wedge", "Cavalry Wedge"])

    # Get the suggested troop composition and formation
    suggested_comp, suggested_form = troop_data.get((enemy_comp, enemy_form), ("", ""))

    # Display the result
    if suggested_comp and suggested_form:
        st.subheader("Suggested Troop Composition and Formation")
        st.write(f"Troop Composition: {suggested_comp}")
        st.write(f"Troop Formation: {suggested_form}")
    else:
        st.subheader("No Matching Troop Data Found")

if __name__ == "__main__":
    main()
