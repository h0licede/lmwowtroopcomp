# import Streamlit module
import streamlit as st

# Set page title
st.set_page_config(page_title="LORDS MOBILE WOW TROOP COMP")

# Add a title and subtitle
st.title("LORDS MOBILE WOW TROOP COMP")


@st.cache(allow_output_mutation=True)
def get_shared_data():
    """
    This function gets the shared data and returns it as a dictionary.
    If the shared data is not present, it returns an empty dictionary.
    """
    shared_data = {}
    if 'data' in st.secrets:
        shared_data = st.secrets['data']
    return shared_data


def save_data(input1, input2, output1, output2):
    """
    This function saves the data to Streamlit data sharing.
    """
    shared_data = get_shared_data()
    data_to_save = [input1, input2, output1, output2]
    existing_data = shared_data.get('existing_data', [])
    overwrite = False
    
    for i, row in enumerate(existing_data):
        if row == data_to_save:
            existing_data[i] = data_to_save
            overwrite = True
            break
    
    if not overwrite:
        existing_data.append(data_to_save)
    
    shared_data['existing_data'] = existing_data
    st.secrets['data'] = shared_data
    st.success("Data saved")
    return not overwrite


def search_data(search_input1, search_input2):
    """
    This function searches for the data in the Streamlit data sharing and returns the matching entries.
    """
    matching_entries = []
    shared_data = get_shared_data()
    existing_data = shared_data.get('existing_data', [])
    for row in existing_data:
        input1, input2, output1, output2 = row
        if input1 == search_input1 and (search_input2 == "" or input2 == search_input2):
            matching_entries.append((output1, output2))
            if len(matching_entries) == 10:  # return when 10 entries have been found
                return matching_entries
    return matching_entries  # return all entries found


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
