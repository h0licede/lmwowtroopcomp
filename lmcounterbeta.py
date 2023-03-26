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

# Read data from text file
data_file = "data.txt"
data = []
with open(data_file, "r") as f:
    for line in f.readlines():
        comps = line.strip().split(",")
        data.append({
            "enemy_comp": comps[0],
            "enemy_form": comps[1],
            "suggested_comp": comps[2],
            "suggested_form": comps[3]
        })

# Define function for searching
def search():
    enemy_comp = st.text_input("Enter enemy composition:")
    enemy_form = st.selectbox("Select enemy formation:", ["Infantry Phalanx", "Ranged Phalanx", "Cavalry Phalanx", "Infantry Wedge", "Ranged Wedge", "Cavalry Wedge"])

    # Filter data based on user input
    results = [d for d in data if d["enemy_comp"] == enemy_comp and d["enemy_form"] == enemy_form]

    # Display results
    if results:
        st.write("Suggested Troop Composition and Formation:")
        for result in results:
            st.write(f"{result['suggested_comp']} {result['suggested_form']}")
    else:
        st.write("No results found.")

# Create Streamlit app
def app():
    st.title("Troop Suggestion Tool")

    search_button = st.button("Search")
    if search_button:
        search()

if __name__ == "__main__":
    app()
