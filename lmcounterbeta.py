import streamlit as st

# Set page title
st.set_page_config(page_title="LORDS MOBILE WOW TROOP COMP")

# Add a title and subtitle
st.title("LORDS MOBILE WOW TROOP COMP")
import streamlit as st

st.write("<h4 style='text-align: center;'>This app is designed specifically for inexperienced / experienced Lords Mobile gamers who lead rallies in World of Wonder, Baron, etc. Using our easy-to-use input functions, you can register and save data on enemy compositions and the troop compositions and formations that you used to counter them. The app uses this registered data to suggest the most common troop compositions and formations used to counter a given enemy composition. The search results show the three most common registered entries for each enemy composition and formation combination.</h4>", unsafe_allow_html=True)








import streamlit as st
import pandas as pd
import git

# Create a list of possible troop compositions and formations
troop_comps = ['001', '002', '003', '004', '005']
formations = ['infantry phalanx', 'ranged phalanx', 'cavalry phalanx', 'infantry wedge', 'ranged wedge', 'cavalry wedge']

# Create an empty dataframe to store user inputs and results
df = pd.DataFrame(columns=['Enemy Troop Comp', 'Enemy Formation', 'Suggested Troop Comp', 'Suggested Formation'])

# Create the user input section
st.header("Enemy and Suggested Troop Compositions")
enemy_comp = st.text_input("Enter enemy troop comp (e.g. 424)")
enemy_form = st.selectbox("Select enemy formation", formations)
suggested_comp = st.text_input("Enter suggested troop comp (e.g. 005)")
suggested_form = st.selectbox("Select suggested formation", formations)
submit = st.button("Submit")

# Add user inputs to the dataframe if the submit button is clicked
if submit:
    df = df.append({'Enemy Troop Comp': enemy_comp,
                    'Enemy Formation': enemy_form,
                    'Suggested Troop Comp': suggested_comp,
                    'Suggested Formation': suggested_form},
                   ignore_index=True)
    # Save the dataframe to a CSV file
    df.to_csv('troop_comps.csv', index=False)
    # Commit the CSV file to the Git repository
    repo = git.Repo.init('.')
    repo.index.add(['troop_comps.csv'])
    repo.index.commit("Update troop comps data")
    remote_origin = repo.remote(name='origin')
    remote_origin.push()

# Filter out duplicate rows and display the results
df = df.drop_duplicates()
if not df.empty:
    st.header("Results")
    st.dataframe(df)
else:
    st.info("No results yet. Enter some troop compositions and formations.")











st.write("<h4 style='text-align: center;'>Donation</h4>", unsafe_allow_html=True)

import streamlit as st

st.write("<h4 style='text-align: center;'>If you're feeling generous and want to support my caffeine addiction while I work on this project, consider donating to my coffee fund. I promise I'll use it to stay awake and make more cool stuff 😜</h4>", unsafe_allow_html=True)


st.markdown('<div style="text-align:center"><a href="https://paypal.me/h0licede" target="_blank" rel="noopener noreferrer">Please consider donating to my coffee fund to support my work</a></div>', unsafe_allow_html=True)
