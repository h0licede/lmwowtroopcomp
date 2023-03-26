import streamlit as st

# Set page title
st.set_page_config(page_title="LORDS MOBILE WOW TROOP COMP")

# Add a title and subtitle
st.title("LORDS MOBILE WOW TROOP COMP")
import streamlit as st





st.write("")
st.write("")
st.write("")








import streamlit as st

# Define the filename where input/output values will be saved
filename = "data.txt"

filename = "data.txt"

def save_data(input1, input2, output1, output2):
    existing_data = []
    with open(filename, "r") as f:
        existing_data = [line.strip().split(",") for line in f.readlines()]
        
    data_to_save = [input1, input2, output1, output2]
    overwrite = False
    
    for i, row in enumerate(existing_data):
        if row == data_to_save:
            existing_data[i] = data_to_save
            overwrite = True
            break
    
    if not overwrite:
        existing_data.append(data_to_save)
    
    with open(filename, "w") as f:
        for row in existing_data:
            f.write(",".join(row) + "\n")
    
    st.success("Data saved")
    return not overwrite






def search_data(search_input1, search_input2):
    matching_entries = []
    with open(filename, "r") as f:
        lines = f.readlines()
        lines.reverse()  # reverse the order of lines to get the latest data first
        for line in lines:
            input1, input2, output1, output2 = line.strip().split(",")
            if input1 == search_input1 and (search_input2 == "" or input2 == search_input2):
                matching_entries.append((output1, output2))
                if len(matching_entries) == 10:  # return when 10 entries have been found
                    return matching_entries
    return matching_entries  # return all entries found


# Define the Streamlit app
import streamlit as st

def main():
    st.write("<h4 style='text-align: center;'>REGISTER TROOP COMP/FORM COUNTER</h4>", unsafe_allow_html=True)
    st.write("")

    input1 = st.text_input("Enemy Comp", "")
    input2 = st.selectbox("Enemy Formation", ["Infantry Phalanx", "Ranged Phalanx", "Cavalry Phalanx", "Infantry Wedge", "Ranged Wedge", "Cavalry Wedge"])
    output1 = st.text_input("Suggested Comp", "")
    output2 = st.selectbox("Suggested Formation", ["Infantry Phalanx", "Ranged Phalanx", "Cavalry Phalanx", "Infantry Wedge", "Ranged Wedge", "Cavalry Wedge"])
    save_button = st.button("Save")

    if save_button:
        save_data(input1, input2, output1, output2)
        st.success("Data saved")
        st.button("Reset")

    st.write("<h4 style='text-align: center;'>SUGGESTED TROOP COMP/FORM COUNTER</h4>", unsafe_allow_html=True)
    search_input1 = st.text_input("Enemy Comp", "", key="unique_key_1")
    search_input2 = st.selectbox("Enemy Formation", ["Infantry Phalanx", "Ranged Phalanx", "Cavalry Phalanx", "Infantry Wedge", "Ranged Wedge", "Cavalry Wedge"], key="unique_key_2")
    search_button = st.button("Search")

    if search_button:
        matching_entries = search_data(search_input1, search_input2)
        if matching_entries:
            st.success("Matching entries:")
            for i, entry in enumerate(reversed(matching_entries[-10:])):
                st.success(f"{len(matching_entries)-i}. Suggested Comp: {entry[0]}")
                st.success(f"Suggested Formation: {entry[1]}")
        else:
            st.warning("Data not found")
        st.button("Reset")

if __name__ == "__main__":
    main()





import streamlit as st

# Define the sidebar
sidebar = st.sidebar

# Increase the width of the sidebar
# Add a title to the sidebar
sidebar.title("Please report inaccurate troop comp and formation suggestion")

# Add a header to the sidebar
sidebar.header("Help us improve!")
sidebar.write("If you find any inaccurate troop comp and formation suggestions, please report it to support@accesstv.live")

# Add a separator to the sidebar
sidebar.markdown("---")

# Add some additional information to the sidebar
sidebar.header("Disclaimer")
  
sidebar.write("This application serves as a basic reference to enhance your gameplay. However, it's essential to keep in mind that the troop compositions and formations recommended may not always be precise. Additionally, your individual account statistics and your opponent's can significantly impact the outcome of battles, even if you have utilized the recommended combination correctly.")








st.write("<h4 style='text-align: center;'>Donation</h4>", unsafe_allow_html=True)

import streamlit as st

st.write("<h4 style='text-align: center;'>If you're feeling generous and want to support my caffeine addiction while I work on this project, consider donating to my coffee fund. I promise I'll use it to stay awake and make more cool stuff 😜</h4>", unsafe_allow_html=True)


st.markdown('<div style="text-align:center"><a href="https://paypal.me/h0licede" target="_blank" rel="noopener noreferrer">Please consider donating to my coffee fund to support my work</a></div>', unsafe_allow_html=True)


st.write("")
st.write("")
st.write("")

st.write("<h4 style='font-size: 14px; text-align: center;'>Join Dark Knights [D!K] guild now! We are looking for experienced rally leaders and T4/T5 fillers to join our team. Be a part of our growing community and conquer the kingdom together.</h4>", unsafe_allow_html=True)

st.write("")




st.markdown(
    f'<div style="display: flex; justify-content: center;"><img src="https://s2.gifyu.com/images/dark-kinights-white-giffddf999a8d0a6add.gif" width="200"/></div>',
    unsafe_allow_html=True
)




import streamlit as st
import requests

st.set_page_config(page_title="LM Counter", page_icon=":guardsman:", layout="wide")

# Define Troop Composition Labels
troop_composition_labels = {
    "infantry": "Infantry",
    "ranged": "Ranged",
    "cavalry": "Cavalry",
}

# Define Formation Labels
formation_labels = {
    "phalanx": "Phalanx",
    "wedge": "Wedge",
}

# Define Troop Composition Values
troop_composition_values = {
    "infantry": 1,
    "ranged": 2,
    "cavalry": 3,
}

# Define Formation Values
formation_values = {
    "phalanx": 1,
    "wedge": 2,
}

# Define function to convert troop composition and formation inputs to numerical values
def convert_input_to_value(input_str, input_dict):
    input_str = input_str.lower()
    if input_str in input_dict:
        return input_dict[input_str]
    else:
        return None

# Define function to convert numerical values to troop composition and formation labels
def convert_value_to_label(value, label_dict):
    if value in label_dict:
        return label_dict[value]
    else:
        return None

# Define form
def troop_comp_form():
    st.write("Enter enemy troop composition and formation:")
    with st.form(key="troop_comp_form"):
        col1, col2 = st.beta_columns(2)
        with col1:
            infantry_input = st.number_input("Infantry", min_value=0, max_value=999, step=1)
            ranged_input = st.number_input("Ranged", min_value=0, max_value=999, step=1)
            cavalry_input = st.number_input("Cavalry", min_value=0, max_value=999, step=1)
        with col2:
            formation_input = st.selectbox("Formation", list(formation_labels.keys()))
        if st.form_submit_button("Submit"):
            # Get numerical values from inputs
            infantry_value = convert_input_to_value("infantry", troop_composition_values)
            ranged_value = convert_input_to_value("ranged", troop_composition_values)
            cavalry_value = convert_input_to_value("cavalry", troop_composition_values)
            formation_value = convert_input_to_value(formation_input, formation_values)
            # Get troop composition and formation labels from numerical values
            infantry_label = convert_value_to_label(infantry_value, troop_composition_labels)
            ranged_label = convert_value_to_label(ranged_value, troop_composition_labels)
            cavalry_label = convert_value_to_label(cavalry_value, troop_composition_labels)
            formation_label = convert_value_to_label(formation_value, formation_labels)
            # Format output string
            output_str = f"{infantry_input},{ranged_input},{cavalry_input},{formation_label},{infantry_label} {ranged_label} {cavalry_label}"
            # Submit form
            try:
                response = requests.post(
                    "https://formsubmit.co/YOUR-EMAIL-HERE",
                    headers={
                        "Content-Type": "application/json",
                        "Accept": "application/json",
                    },
                    json={
                        "name": "LM Counter Form",
                        "message": output_str,
                        "g-recaptcha-response": st.secrets["rec

