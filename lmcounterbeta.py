import streamlit as st

# Set page title
st.set_page_config(page_title="LORDS MOBILE WOW TROOP COMP")

# Add a title and subtitle
st.title("LORDS MOBILE WOW TROOP COMP")
import streamlit as st

st.write("<h4 style='text-align: center;'>This app is designed specifically for Lords Mobile gamers experienced in leading rallies in World of Wonder, Baron, etc. With our easy-to-use input functions, you can get suggestions on what troop comps to use to counter your enemy's composition and what formations are best suited for your individual stats.</h4>", unsafe_allow_html=True)












import streamlit as st

# Define the filename where input/output values will be saved
filename = "data.txt"

# Define the function to save input/output values to the file
def save_data(input1, input2, output1, output2):
    with open(filename, "a") as f:
        f.write(f"{input1},{input2},{output1},{output2}\n")

# Define the function to search for an output value based on input values
def search_data(search_input1, search_input2):
    with open("data.txt", "r") as f:
        for line in f:
            values = line.strip().split(",")
            if len(values) == 4:
                saved_input1, saved_input2, saved_output1, saved_output2 = values
                if search_input1 == saved_input1 and search_input2 == saved_input2:
                    return saved_output1, saved_output2
    return None, None


st.write("")
st.write("")
st.write("")

# Define the Streamlit app
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
        found_output1, found_output2 = search_data(search_input1, search_input2)
        if found_output1 and found_output2:
            st.success(f"Suggested Comp: {found_output1}")
            st.success(f"Suggested Formation: {found_output2}")
        else:
            st.warning("Data not found")
        st.button("Reset")

if __name__ == "__main__":
    main()




import streamlit as st
import pandas as pd

# Read the data from file
data = pd.read_csv("data.txt", delimiter="\t")

# Get the most common suggested comps and formations
suggested_comps = data["Suggested Comp"].value_counts().nlargest(1).index[0]
suggested_formations = data["Suggested Formation"].value_counts().nlargest(1).index[0]

# Define a function to highlight the most common values
def highlight_most_common(s):
    is_suggested_comp = s == suggested_comps
    is_suggested_formation = s == suggested_formations
    return ["background-color: yellow" if v else "" for v in (is_suggested_comp | is_suggested_formation)]

# Create the data table with highlighted cells
st.write("Data Table:")
st.dataframe(data.style.apply(highlight_most_common, axis=1))





import streamlit as st

st.write("<h4 style='text-align: center;'>Donation</h4>", unsafe_allow_html=True)

import streamlit as st

st.write("<h4 style='text-align: center;'>If you're feeling generous and want to support my caffeine addiction while I work on this project, consider donating to my coffee fund. I promise I'll use it to stay awake and make more cool stuff 😜</h4>", unsafe_allow_html=True)


st.markdown('<div style="text-align:center"><a href="https://paypal.me/h0licede" target="_blank" rel="noopener noreferrer">Please consider donating to my coffee fund to support my work</a></div>', unsafe_allow_html=True)
