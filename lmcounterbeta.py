import streamlit as st
import gspread
from google.oauth2 import service_account

# Authenticate with Google Sheets using st.secrets
creds = service_account.Credentials.from_service_account_info(st.secrets["gcp_service_account"])
client = gspread.authorize(creds)

# Define the Google Sheets worksheet
worksheet = client.open('Troop Compositions').sheet1

# Define the possible formations
formations = ['infantry phalanx', 'ranged phalanx', 'cavalry phalanx',
              'infantry wedge', 'ranged wedge', 'cavalry wedge']

# Define the Streamlit app
def app():
    st.title('Troop Composition Suggestions')
    
    # Define the input form
    enemy_troops = st.text_input('Enemy Troop Composition (3 numerical values):')
    enemy_formation = st.selectbox('Enemy Formation:', formations)
    
    # Define the output table
    st.write('Suggested Troop Composition and Formation:')
    st.write('| Enemy Troops | Enemy Formation | Suggested Troops | Suggested Formation |')
    st.write('|--------------|----------------|------------------|---------------------|')
    
    # Define the search criteria
    search_criteria = [enemy_troops, enemy_formation]
    
    # Search for matching rows in the worksheet
    rows = worksheet.findall(search_criteria)
    
    # Display the matching rows
    for row in rows:
        values = worksheet.row_values(row.row)
        if values != search_criteria:
            st.write(f'| {values[0]} | {values[1]} | {values[2]} | {values[3]} |')
    
    # Define the suggestion form
    suggested_troops = st.text_input('Suggested Troop Composition (3 numerical values):')
    suggested_formation = st.selectbox('Suggested Formation:', formations)
    
    # Add the suggestion to the worksheet
    if suggested_troops and suggested_formation:
        worksheet.append_row([enemy_troops, enemy_formation, suggested_troops, suggested_formation])
        st.success('Suggestion added to the Troop Compositions worksheet.')

# Run the Streamlit app
if __name__ == '__main__':
    app()
