import streamlit as st
import requests

# Define the Formspree API endpoint
endpoint = "https://formspree.io/f/xwkjnzgp"

def main():
    st.markdown(
        """
        <div style='text-align:center'>
            <h4 style='font-size: 2em; font-weight: bold;'>Lords Mobile Mix Troop Strategy</h4>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")
    
    st.markdown(
        """
        <div style='text-align:center'>
            <h4 style='font-size: 1em; font-weight: semi-bold;'>Create Your Mix Troop Suggestion Here</h4>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Define the options for the troop formations dropdown
    troop_formations = ['Infantry Phalanx', 'Ranged Phalanx', 'Cavalry Phalanx', 'Infantry Wedge', 'Ranged Wedge', 'Cavalry Wedge']

    # Define the input fields
    enemy_composition = st.number_input("Enemy Troop Composition (3 digit number)", min_value=0, max_value=999, step=1)
    enemy_formation = st.selectbox("Enemy Troop Formation", troop_formations)
    suggested_composition = st.number_input("Suggested Troop Composition (3 digit number)", min_value=0, max_value=999, step=1)
    suggested_formation = st.selectbox("Suggested Troop Formation", troop_formations)
    message = st.text_area("Explain why this mix troop suggestion is ideal? (minimum 250 characters)", max_chars=500)

    submit_button = st.button("Submit")

    if submit_button:
        if len(message) < 250:
            st.warning("Please provide an explanation with at least 250 characters.")
        else:
            # Set the form data as a dictionary
            form_data = {
                "Enemy Troop Composition": enemy_composition,
                "Enemy Troop Formation": enemy_formation,
                "Suggested Troop Composition": suggested_composition,
                "Suggested Troop Formation": suggested_formation,
                "Explanation": message
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

# Read data from file
def read_data():
    with open("data.txt", "r") as f:
        lines = f.readlines()
    data = []
    for line in lines:
        line = line.strip()
        if line:
            values = line.split(",")
            data.append((values[0], values[1], values[2], values[3]))
    return data

# Search for matching results
def search_data(data, enemy_comp, enemy_form):
    matches = []
    for d in data:
        if d[0] == enemy_comp and d[1] == enemy_form:
            matches.append((d[2], d[3]))
    return matches

# Main function
def main():
    st.markdown(
    """
    <div style='text-align:center'>
        <h4 style='font-size: 1em; font-weight: semi-bold;'>Mix Troop Search</h4>
    </div>
    """,
    unsafe_allow_html=True
)

    # Read data from file
    data = read_data()

    # Get user input
    enemy_comp = st.text_input("Enter enemy troop composition (3-digit number)")
    enemy_form = st.selectbox("Select enemy troop formation", ["Infantry Phalanx", "Ranged Phalanx", "Cavalry Phalanx", "Infantry Wedge", "Ranged Wedge", "Cavalry Wedge"])
    search_button = st.button("Search")

    # Show results if search button is clicked
    if search_button:
        matches = search_data(data, enemy_comp, enemy_form)
        if matches:
            st.success("Matching results:")
            for m in matches:
                st.write(f"Suggested troop composition: {m[0]}, Suggested troop formation: {m[1]}")
        else:
            st.warning("No matching results found.")

if __name__ == "__main__":
    main()


import streamlit as st

st.write("<h4 style='text-align: center; font-size: 95%;'>Donation</h4>", unsafe_allow_html=True)

st.write("<h4 style='font-size: 95%; text-align: center;'>If you're feeling generous and want to support my caffeine addiction while I work on this project, consider donating to my coffee fund. I promise I'll use it to stay awake and make more cool stuff 😜</h4>", unsafe_allow_html=True)

st.markdown('<div style="text-align:center; font-size: 95%;"><a href="https://paypal.me/h0licede" target="_blank" rel="noopener noreferrer">Please consider donating to my coffee fund to support my work</a></div>', unsafe_allow_html=True)

st.write("")
st.write("")
st.write("")

st.write("<h4 style='font-size: 95%; text-align: center;'>Join Dark Knights [D!K] guild now! We are looking for experienced rally leaders and T4/T5 fillers to join our team. Be a part of our growing community and conquer the kingdom together.</h4>", unsafe_allow_html=True)

st.write("")

st.markdown(
    f'<div style="display: flex; justify-content: center;"><img src="https://s2.gifyu.com/images/dark-kinights-white-giffddf999a8d0a6add.gif" width="200"/></div>',
    unsafe_allow_html=True
)


import streamlit as st

# Define the sidebar
sidebar = st.sidebar

# Increase the width of the sidebar
# Add a title to the sidebar
sidebar.title("Please report inaccurate troop comp and formation suggestion")

# Add a header to the sidebar
sidebar.header("Help us improve!")
sidebar.write("<p style='font-size: 14px;'>If you find any inaccurate mix troop composition and formation suggestions, please report it to lyricsstanza@gmail.com</p>", unsafe_allow_html=True)

# Add a separator to the sidebar
sidebar.markdown("---")

# Add some additional information to the sidebar
sidebar.header("Disclaimer")
  
sidebar.write("<p style='font-size: 14px;'>This application serves as a basic reference to enhance your gameplay. However, it's essential to keep in mind that the troop compositions and formations recommended may not always be precise. Additionally, your individual account statistics and your opponent's can significantly impact the outcome of battles, even if you have utilized the recommended combination correctly.</p>", unsafe_allow_html=True)
