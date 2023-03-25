import streamlit as st

# Set page title
st.set_page_config(page_title="LORDS MOBILE WOW TROOP COMP")

# Add a title and subtitle
st.title("LORDS MOBILE WOW TROOP COMP")
import streamlit as st


st.write("<h4 style='font-size: 14px; text-align: center;'>This app is designed specifically for inexperienced / experienced Lords Mobile gamers who lead rallies in World of Wonder, Baron, etc. Using our easy-to-use input functions, you can register and save data on enemy compositions and the troop compositions and formations that you used to counter them. The app uses this registered data to suggest the most common troop compositions and formations used to counter a given enemy composition. The search results show the three most common registered entries for each enemy composition and formation combination.</h4>", unsafe_allow_html=True)













import streamlit as st

# Define the filename where input/output values will be saved
filename = "data.txt"

# Define the function to save input/output values to the file
def save_data(input1, input2, output1, output2):
    with open(filename, "a") as f:
        f.write(f"{input1},{input2},{output1},{output2}\n")

# Define the function to search for an output value based on input values
def search_data(search_input1, search_input2):
    matching_entries = []
    with open(filename, "r") as f:
        for line in f:
            input1, input2, output1, output2 = line.strip().split(",")
            if input1 == search_input1 and (search_input2 == "" or input2 == search_input2):
                matching_entries.append((output1, output2))
    return matching_entries[:3] # return only the first 3 search results

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
            for i, entry in enumerate(matching_entries[:3]):
                st.success(f"{i+1}. Suggested Comp: {entry[0]}")
                st.success(f"Suggested Formation: {entry[1]}")
        else:
            st.warning("Data not found")
        st.button("Reset")

if __name__ == "__main__":
    main()











st.write("<h4 style='text-align: center;'>Donation</h4>", unsafe_allow_html=True)

import streamlit as st

st.write("<h4 style='text-align: center;'>If you're feeling generous and want to support my caffeine addiction while I work on this project, consider donating to my coffee fund. I promise I'll use it to stay awake and make more cool stuff 😜</h4>", unsafe_allow_html=True)


st.markdown('<div style="text-align:center"><a href="https://paypal.me/h0licede" target="_blank" rel="noopener noreferrer">Please consider donating to my coffee fund to support my work</a></div>', unsafe_allow_html=True)




st.write("<h4 style='font-size: 14px; text-align: center;'>Join Dark Knights [D!K] guild now! We are looking for experienced rally leaders and T4/T5 fillers to join our team. Be a part of our growing community and conquer the kingdom together.</h4>", unsafe_allow_html=True)
