import streamlit as st
import pandas as pd

# Load the data
data = {'Enemy Comp': ['424, 947, 857', '442, 992', '442, 424 (All variants), 992', '442, 992, 208, 055', '749, 659, 424, 055', 'All 424 variants, 208'],
        'Suggested Comp': ['749', '947', '208', '992', '442', '055'],
        'Suggested Comp Can Be Countered By': ['424, 749, 208, 055', '(992, 442, 424 variants) - Must be in ranged wedge and 055 is good to snipe 208.', '424, 749, 758, 659, 055', '947, 523, Inf Blast, 208, 974, 866', '208, 947, 523, 974, 866', '992, 442, 866, 974']}

df = pd.DataFrame(data)

# Set up the app
st.title("Troop Comp Counter Bot")
user_input = st.text_input("Type in enemy comp in 3 digit number:")

# Define function to check for matches
def check_matches(user_input):
    results = []
    for index, row in df.iterrows():
        if user_input in row['Enemy Comp'] or user_input == row['Suggested Comp'] or user_input in row['Suggested Comp Can Be Countered By']:
            message = f"Enemy Comp: {row['Enemy Comp']}\nSuggested Comp: {row['Suggested Comp']}\nSuggested Comp Can Be Countered By: {row['Suggested Comp Can Be Countered By']}"
            results.append(message)
    if not results:
        results.append("No matching troop comp found. Please enter a valid 3 digit number.")
    return results

# Display results
if user_input:
    results = check_matches(user_input)
    for result in results:
        st.write(result)
