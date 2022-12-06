import streamlit as st
from gsheetsdb import connect


# Create a connection object.
conn = connect()

# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    rows = rows.fetchall()
    return rows

# sheet_url = st.secrets["public_gsheets_url"]
# sheet_url = 'https://docs.google.com/spreadsheets/d/1Vj3lhdCPzZWvKXzA2RDRugx8wckHyp7u65maLDhSsPY/edit#gid=0'

# rows = run_query(f'SELECT * FROM "{sheet_url}"')
def search(name):
    sheet_url = 'https://docs.google.com/spreadsheets/d/1Vj3lhdCPzZWvKXzA2RDRugx8wckHyp7u65maLDhSsPY/edit#gid=0'
    a1 = str('{}'.format(name))
    rows = run_query(f'SELECT * FROM "{sheet_url}" WHERE name = "{a1}"')
    # Print results.
    for row in rows:
        st.write(f"{row.name} bag is :{row.status}:")

whichcasno = st.text_input('Enter CAS number', value = '', max_chars = None, key = None, type = 'default', help = 'CAS号形如1336-21-6')
st.write(whichcasno,'Service Staus is following:')
query_test = search(whichcasno)

