import streamlit as st
import pandas as pd


st.markdown(
    f'<div style="display: flex; justify-content: center;"><img src="https://i.postimg.cc/ZqxVnStT/dark-kinights-logo.png" width="200"/></div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div style='text-align:center'>
        <h4 style='font-size: 2em; font-weight: bold;'>Lords Mobile Mix Troop Strategy</h4>
    </div>
    """,
    unsafe_allow_html=True
)


# Load the data
comps = pd.read_csv('comps.csv')

# Define the app
def app():
    user_input = st.text_input("Type in enemy troop comp in 3 digit number for example:424")

    # Show the results
    if user_input:
        found = False
        for index, row in comps.iterrows():
            if str(row['Enemy Comp']).startswith(str(user_input).lstrip('0')):
                found = True
                # Include leading zeros in the 'Enemy Comp' value
                enemy_comp = str(row['Enemy Comp']).zfill(3)
                message = f"Enemy Comp: {enemy_comp}\nCounter Comp: {row['Counter Comp']}"
                st.write(message)
        if not found:
            st.write("No matching troop comp found. Please enter a valid 3 digit number.")

# Run the app
app()

















    
    
    
st.write("<h4 style='text-align: center; font-size: 95%;'>Donation</h4>", unsafe_allow_html=True)

st.markdown('<div style="text-align:center; font-size: 95%;"><a href="https://paypal.me/h0licede" target="_blank" rel="noopener noreferrer">Please consider donating to my coffee fund to support my work</a></div>', unsafe_allow_html=True)

st.write("")
st.write("")
st.write("")

st.write("<h4 style='font-size: 95%; text-align: center;'>Join Dark Knights [D!K] guild now! We are looking for experienced rally leaders and T4/T5 fillers to join our team. Be a part of our growing community and conquer the kingdom together.</h4>", unsafe_allow_html=True)

st.write("")




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





