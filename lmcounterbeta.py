import streamlit as st
import requests

# Define the FormSubmit API endpoint
endpoint = "https://formsubmit.co/lyricsstanza@gmail.com"

def main():
    st.write("<h4 style='text-align: center;'>REGISTER TROOP COMP/FORM COUNTER</h4>", unsafe_allow_html=True)
    st.write("")

    enemy_comp = st.text_input("Enemy Comp", "")
    enemy_formation = st.selectbox("Enemy Formation", ["Infantry Phalanx", "Ranged Phalanx", "Cavalry Phalanx", "Infantry Wedge", "Ranged Wedge", "Cavalry Wedge"])
    suggested_comp = st.text_input("Suggested Comp", "")
    suggested_formation = st.selectbox("Suggested Formation", ["Infantry Phalanx", "Ranged Phalanx", "Cavalry Phalanx", "Infantry Wedge", "Ranged Wedge", "Cavalry Wedge"])
    save_button = st.button("Submit")

    if save_button:
        # Set the form data as a dictionary
        form_data = {
            "enemy_comp": enemy_comp,
            "enemy_formation": enemy_formation,
            "suggested_comp": suggested_comp,
            "suggested_formation": suggested_formation,
        }

        # Send the form data using a POST request
        response = requests.post(endpoint, data=form_data)

        # Check if the request was successful and display appropriate message
        if response.status_code == 200:
            st.success("Data submitted successfully")
        else:
            st.error("Error submitting data")

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
