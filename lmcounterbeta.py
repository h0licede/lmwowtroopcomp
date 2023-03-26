import streamlit as st
import requests

# Define the FormSubmit API endpoint
endpoint = "https://formsubmit.co/lyricsstanza@gmail.com"

def main():
    st.write("<h4 style='text-align: center;'>TROOP COMP/FORMATION COUNTER</h4>", unsafe_allow_html=True)
    st.write("")

    input1 = st.text_input("Enemy Comps", "")
    input2 = st.selectbox("Enemy Formation", ["Infantry Phalanx", "Ranged Phalanx", "Cavalry Phalanx", "Infantry Wedge", "Ranged Wedge", "Cavalry Wedge"])
    output1 = st.text_input("Suggested Comps", "")
    output2 = st.selectbox("Suggested Formation", ["Infantry Phalanx", "Ranged Phalanx", "Cavalry Phalanx", "Infantry Wedge", "Ranged Wedge", "Cavalry Wedge"])
    save_button = st.button("Submit")

    if save_button:
        # Set the form data as a dictionary
        form_data = {
            "enemy_comps": input1,
            "enemy_formation": input2,
            "suggested_comps": output1,
            "suggested_formation": output2,
        }

        # Send the form data using a POST request
        response = requests.post(endpoint, data=form_data)

        # Check if the request was successful and display appropriate message
        if response.status_code == 200:
            st.success("Data submitted successfully")
        else:
            st.error("Error submitting data")

if __name__ == "__main__":
    main()
