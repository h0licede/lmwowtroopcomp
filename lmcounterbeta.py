import streamlit as st
import pandas as pd

def main():
    st.title('Troop Comp Counter Bot')
    st.write('Type in an enemy comp as a 3-digit number:')

    data = {'Enemy Comp': ['424, 947, 857', '442, 992', '442, 424 (All variants), 992', '442, 992, 208, 055', '749, 659, 424, 055', 'All 424 variants, 208'],
            'Suggested Comp': ['749', '947', '208', '992', '442', '055'],
            'Suggested Comp Can Be Countered By': ['424, 749, 208, 055', '(992, 442, 424 variants) - Must be in ranged wedge and 055 is good to snipe 208.', '424, 749, 758, 659, 055', '947, 523, Inf Blast, 208, 974, 866', '208, 947, 523, 974, 866', '992, 442, 866, 974']}

    df = pd.DataFrame(data)

    user_input = st.text_input('Enter 3-digit number')
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

if __name__ == '__main__':
    main()
