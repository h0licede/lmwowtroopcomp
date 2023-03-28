import streamlit as st
import pandas as pd

# Load the data
data = {'Enemy Comp': ['424, 947, 857', '442, 992', '442, 424 (All variants), 992', '442, 992, 208, 055', '749, 659, 424, 055', 'All 424 variants, 208'],
        'Suggested Comp': ['749', '947', '208', '992', '442', '055'],
        'Suggested Comp Can Be Countered By': ['424, 749, 208, 055', '(992, 442, 424 variants) - Must be in ranged wedge and 055 is good to snipe 208.', '424, 749, 758, 659, 055', '947, 523, Inf Blast, 208, 974, 866', '208, 947, 523, 974, 866', '992, 442, 866, 974']}

df = pd.DataFrame(data)

# Define the message handler
def handle_input(user_input):
    found = False
    for index, row in df.iterrows():
        if user_input in row['Enemy Comp'] or user_input == row['Suggested Comp'] or user_input in row['Suggested Comp Can Be Countered By']:
            found = True
            message = f"Enemy Comp: {row['Enemy Comp']}\nSuggested Comp: {row['Suggested Comp']}\nSuggested Comp Can Be Countered By:\n"
            counters = row['Suggested Comp Can Be Countered By']
            if ',' in counters:
                counters = counters.split(',')
                for counter in counters:
                    message += f"\u2022 {counter.strip()}\n"
            else:
                message += f"\u2022 {counters}\n"
            return message
            break
    if not found:
        return "No matching troop comp found. Please enter a valid 3 digit number."

# Set up the app
st.title("Troop Comp Counter App")
user_input = st.text_input("Type in enemy comp in 3 digit number and press Enter:")
if user_input:
    result = handle_input(user_input)
    st.write(result)
