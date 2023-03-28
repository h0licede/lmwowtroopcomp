import streamlit as st
import pandas as pd

# Load the data
data = {'Enemy Comp': ['424, 947, 857', '442, 992', '442, 424 (All variants), 992', '442, 992, 208, 055', '749, 659, 424, 055', 'All 424 variants, 208'],
        'Suggested Comp': ['749', '947', '208', '992', '442', '055'],
        'This Comp Counters Suggested': ['424, 749, 208, 055', '(992, 442, 424 variants) - Must be in ranged wedge and 055 is good to snipe 208.', '424, 749, 758, 659, 055', '947, 523, Inf Blast, 208, 974, 866', '208, 947, 523, 974, 866', '992, 442, 866, 974']}

df = pd.DataFrame(data)

# Define the app
def app():
    # Set the app title
    st.title("Troop Comp Counter Bot")

    # Get user input
    user_input = st.text_input("Enter a 3 digit number to get information on troop comps:")

    # Check if input is valid
    if len(user_input) != 3 or not user_input.isnumeric():
        st.warning("Please enter a valid 3 digit number.")
        return

    # Search for matching troop comp
    found = False
    for index, row in df.iterrows():
        if user_input in row['Enemy Comp'] or user_input == row['Suggested Comp'] or user_input in row['This Comp Counters Suggested']:
            found = True
            st.write(f"Enemy Comp: {row['Enemy Comp']}")
            st.write(f"Suggested Comp: {row['Suggested Comp']}")
            st.write(f"This Comp Counters Suggested: {row['This Comp Counters Suggested']}")
            break

    # Display error message if no match is found
    if not found:
        st.warning("No matching troop comp found. Please enter a valid 3 digit number.")
