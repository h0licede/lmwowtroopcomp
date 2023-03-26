import streamlit as st

# Set page title
st.set_page_config(page_title="LORDS MOBILE WOW TROOP COMP")

# Add a title and subtitle
st.title("LORDS MOBILE WOW TROOP COMP")
import streamlit as st

st.write("<h4 style='text-align: center;'>This app is designed specifically for inexperienced / experienced Lords Mobile gamers who lead rallies in World of Wonder, Baron, etc. Using our easy-to-use input functions, you can register and save data on enemy compositions and the troop compositions and formations that you used to counter them. The app uses this registered data to suggest the most common troop compositions and formations used to counter a given enemy composition. The search results show the three most common registered entries for each enemy composition and formation combination.</h4>", unsafe_allow_html=True)








import streamlit as st
import pandas as pd

# Create a table to store user inputs and suggested troop comps and formations
df = pd.DataFrame(columns=['Enemy Troop Comp', 'Enemy Formation', 'Suggested Troop Comp', 'Suggested Formation'])

# Create a form for users to enter their enemy troop comp and formation
enemy_troop_comp = st.selectbox('Enemy Troop Comp', ['Infantry Phalanx', 'Ranged Phalanx', 'Cavalry Phalanx', 'Infantry Wedge', 'Ranged Wedge', 'Cavalry Wedge'])
enemy_formation = st.selectbox('Enemy Formation', ['Infantry Phalanx', 'Ranged Phalanx', 'Cavalry Phalanx', 'Infantry Wedge', 'Ranged Wedge', 'Cavalry Wedge'])

# Define a function to suggest troop comps and formations based on user inputs
def suggest_troop_comp_and_formation(enemy_troop_comp, enemy_formation):
    # Insert your algorithm here to suggest troop comps and formations based on user inputs
    # For now, let's just suggest the same values as the user inputs
    suggested_troop_comp = enemy_troop_comp
    suggested_formation = enemy_formation
    return suggested_troop_comp, suggested_formation

# Add user inputs and suggested troop comps and formations to the table
if st.button('Add to Table'):
    suggested_troop_comp, suggested_formation = suggest_troop_comp_and_formation(enemy_troop_comp, enemy_formation)
    df.loc[len(df)] = [enemy_troop_comp, enemy_formation, suggested_troop_comp, suggested_formation]

# Display the table
st.dataframe(df)









st.write("<h4 style='text-align: center;'>Donation</h4>", unsafe_allow_html=True)

import streamlit as st

st.write("<h4 style='text-align: center;'>If you're feeling generous and want to support my caffeine addiction while I work on this project, consider donating to my coffee fund. I promise I'll use it to stay awake and make more cool stuff 😜</h4>", unsafe_allow_html=True)


st.markdown('<div style="text-align:center"><a href="https://paypal.me/h0licede" target="_blank" rel="noopener noreferrer">Please consider donating to my coffee fund to support my work</a></div>', unsafe_allow_html=True)
