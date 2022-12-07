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
def search(a1,a2):
    sheet_url = 'https://docs.google.com/spreadsheets/d/1Vj3lhdCPzZWvKXzA2RDRugx8wckHyp7u65maLDhSsPY/edit#gid=0'
    # a1 = str('{}'.format(name))
    a1 = '{}'.format(a1)
    a2 = '{}'.format(a2)

    # rows = run_query(f'SELECT * FROM "{sheet_url}" WHERE name = "{a1}"')
    rows = run_query(f'SELECT * FROM "{sheet_url}"')
    # Print results.
    print(rows)
    for row in rows:
        if f"{row.name}" == a1 and f"{row.num}" == a2:
            st.write(f"{row.name} bag is :{row.status}:")
    # return rows
whichcasno1 = st.text_input('Enter CAS number', value = '', max_chars = None, key = 1, type = 'default', help = 'CAS号形如1336-21-6')
whichcasno2 = st.text_input('Enter CAS number', value = '', max_chars = None, key = 2, type = 'default', help = 'CAS号形如1336-21-6')

st.write(whichcasno1,'Service Staus is following:')
query_test = search(whichcasno1,whichcasno2)

