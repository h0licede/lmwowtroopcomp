import streamlit as st
import pandas as pd

# Load the data
data = {'Enemy Comp': ['424, 947, 857', '442, 992', '442, 424 (All variants), 992', '442, 992, 208, 055', '749, 659, 424, 055', 'All 424 variants, 208'],
        'Suggested Comp': ['749', '947', '208', '992', '442', '055'],
        'This Comp Counters Suggested': ['424, 749, 208, 055', '(992, 442, 424 variants) - Must be in ranged wedge and 055 is good to snipe 208.', '424, 749, 758, 659, 055', '947, 523, Inf Blast, 208, 974, 866', '208, 947, 523, 974, 866', '992, 442, 866, 974']}

df = pd.DataFrame(data)

# Define the functions
def search_comp(user_input):
    found = False
    for index, row in df.iterrows():
        if user_input in row['Enemy Comp'] or user_input == row['Suggested Comp'] or user_input in row['This Comp Counters Suggested']:
            found = True
            message = f"Enemy Comp: {row['Enemy Comp']}\nSuggested Comp: {row['Suggested Comp']}\nThis Comp Counters Suggested: {row['This Comp Counters Suggested']}"
            st.success(message)
            break
    if not found:
        st.warning("No matching troop comp found. Please enter a valid 3 digit number.")

# Create the Streamlit app
def main():
    st.title("Troop Comp Counter Bot")
    st.write("Welcome to the troop comp counter bot. Enter a 3 digit number to get information on troop comps.")
    user_input = st.text_input("Enter a 3 digit number:")
    if user_input:
        search_comp(user_input)

if __name__ == "__main__":
    main()
