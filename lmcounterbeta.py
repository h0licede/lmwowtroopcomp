import streamlit as st

# Set page title
st.set_page_config(page_title="LORDS MOBILE WOW TROOP COMP")

# Add a title and subtitle
st.title("LORDS MOBILE WOW TROOP COMP")
import streamlit as st


st.write("<h4 style='font-size: 14px; text-align: center;'>This app is designed specifically for inexperienced / experienced Lords Mobile gamers who lead rallies in World of Wonder, Baron, etc. Using our easy-to-use input functions, you can register and save data on enemy compositions and the troop compositions and formations that you used to counter them. The app uses this registered data to suggest the most common troop compositions and formations used to counter a given enemy composition. The search results show the 10 most common registered entries for each suggested composition and formation combination.</h4>", unsafe_allow_html=True)




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












st.write("<h4 style='text-align: center;'>Donation</h4>", unsafe_allow_html=True)

import streamlit as st

st.write("<h4 style='text-align: center;'>If you're feeling generous and want to support my caffeine addiction while I work on this project, consider donating to my coffee fund. I promise I'll use it to stay awake and make more cool stuff 😜</h4>", unsafe_allow_html=True)


st.markdown('<div style="text-align:center"><a href="https://paypal.me/h0licede" target="_blank" rel="noopener noreferrer">Please consider donating to my coffee fund to support my work</a></div>', unsafe_allow_html=True)


st.write("")
st.write("")
st.write("")

st.write("<h4 style='font-size: 14px; text-align: center;'>Join Dark Knights [D!K] guild now! We are looking for experienced rally leaders and T4/T5 fillers to join our team. Be a part of our growing community and conquer the kingdom together.</h4>", unsafe_allow_html=True)
