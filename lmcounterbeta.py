import streamlit as st

# Set page title
st.set_page_config(page_title="LORDS MOBILE WOW TROOP COMP")

# Add a title and subtitle
st.title("LORDS MOBILE WOW TROOP COMP")
st.write("This app is designed specifically for Lords Mobile gamers experienced in leading rallies in World of Wonder, Baron, etc. With our easy-to-use input functions, you can get suggestions on what troop comps to use to counter your enemy's composition and what formations are best suited for your individual stats. ")











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


# Define the Streamlit app
def main():
    st.subheader("Register and search counter data")
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

    st.subheader("Search counter data")
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

st.title("My Awesome Donation Page")

st.header("Hello kind stranger!")
st.subheader("If you enjoy using my program, please consider fueling my coding with a coffee or two. ☕️")
st.write("Your donations will help me stay up late and write better code. 😉")

st.write("---")

st.write("To donate, please click the button below:")

st.write("")

st.markdown('<center><form action="https://www.paypal.com/donate" method="post" target="_blank"> \
            <input type="hidden" name="hosted_button_id" value="CGZCEX4YJQ8EG" /> \
            <input type="image" src="https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif" \
            border="0" name="submit" title="PayPal - The safer, easier way to pay online!" \
            alt="Donate with PayPal button" /> \
            <img alt="" border="0" src="https://www.paypal.com/en_CA/i/scr/pixel.gif" width="1" height="1" /> \
            </form></center>', unsafe_allow_html=True)
