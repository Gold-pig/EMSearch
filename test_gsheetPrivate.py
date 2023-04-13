import streamlit as st
from gsheetsdb import connect
from google.oauth2 import service_account
from PIL import Image

# Create a connection object.
# conn = connect()

# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.

credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
    ],
)
conn = connect(credentials=credentials)
@st.cache_resource(ttl=600)

def run_query(query):
    rows = conn.execute(query, headers=1)
    rows = rows.fetchall()
    return rows

def search(a1,a2):
    sheet_url = st.secrets["private_gsheets_url"]
    # a1 = str('{}'.format(name))
    a1 = '{}'.format(a1)
    a1 = a1.lower()
    a2 = '{}'.format(a2)
    a2 = a2.lower()

    # rows = run_query(f'SELECT * FROM "{sheet_url}" WHERE name = "{a1}"')
    rows = run_query(f'SELECT * FROM "{sheet_url}"')
    # Print results.
    print(rows)
    n = 0
    for row in rows:
        if f"{row.name}" == a1 and f"{row.num}" == a2:
            st.write(f"{row.name} bag is: {row.status}:")
            row_ty = f"{row.num}"
            print(row_ty.type())
            #sta = row.status
            #if int(sta[0]) == 1:
                #image = Image.open('mc.png')
                #st.image(image,caption='')
                #print('1')
            #elif int(sta[0]) == 2:
                #image = Image.open('kfc.png')
                #st.image(image,caption='')
                #print('2')

            n+=1
    if n == 0:
        st.write(f"Not found")


st.title('EM Bag Service Status Tracking')
# st.subheader('This is a subheader')
whichcasno1 = st.text_input('Enter First Name', value = '', max_chars = None, key = 1, type = 'default', help = 'Alice')
whichcasno2 = st.text_input('Enter Order Num', value = '', max_chars = None, key = 2, type = 'default', help = 'R101')

if whichcasno1!='' and whichcasno2!='':
    st.write('Your bag service staus is following:')
    query_test = search(whichcasno1,whichcasno2)




