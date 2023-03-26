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

def get_suggestions(composition, formation):
    with open('data.txt', 'r') as f:
        lines = f.readlines()

    matching_results = []
    for line in lines:
        parts = line.strip().split(',')
        if parts[0] == composition and parts[1] == formation:
            matching_results.append((parts[2], parts[3]))

    return matching_results

def main():
    st.header('Troop Suggestions')

    # Get user input for enemy composition
    composition = st.text_input('Enemy Troop Composition', max_chars=3)

    # Get user input for enemy formation
    formation_options = ['Infantry Phalanx', 'Ranged Phalanx', 'Cavalry Phalanx', 'Infantry Wedge', 'Ranged Wedge', 'Cavalry Wedge']
    formation = st.selectbox('Enemy Troop Formation', formation_options)

    # Get suggestions if search button is clicked
    if st.button('Search'):
        # Get matching results
        matching_results = get_suggestions(composition, formation)
        
        # Display matching results
        if matching_results:
            st.subheader('Suggested Troop Compositions and Formations:')
            for result in matching_results:
                st.write(f'Composition: {result[0]}, Formation: {result[1]}')
        else:
            st.write('No matching results found.')

if __name__ == '__main__':
    main()

