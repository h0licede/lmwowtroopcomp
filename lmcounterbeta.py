import streamlit as st
import pandas as pd

# Load the data
df = pd.read_csv('comps.csv')

# Define the message handler
def echo():
    user_input = st.text_input('Type in enemy comp in 3 digit number:')
    if user_input:
        found = False
        for index, row in df.iterrows():
            if user_input in row['Enemy Comp'] or user_input == row['Suggested Comp'] or user_input in row['Suggested Comp Can Be Countered By']:
                found = True
                message = f"Enemy Comp: {row['Enemy Comp']}\nSuggested Comp: {row['Suggested Comp']}\nSuggested Comp Can Be Countered By: {row['Suggested Comp Can Be Countered By'].split(',')}"
                st.write(message)
                break
        if not found:
            st.write("No matching troop comp found. Please enter a valid 3 digit number.")

# Set up the app
st.title('Troop Comp Counter Bot')
echo()
