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

def search(a1,a2,a3):
    sheet_url = st.secrets["private_gsheets_url"]
    # a1 = str('{}'.format(name))
    a1 = '{}'.format(a1)
    a1 = a1.lower()
    a2 = '{}'.format(a2)
    a2 = a2.lower()
    #last name
    a3 = '{}'.format(a3)
    a3 = a3.lower()

    # rows = run_query(f'SELECT * FROM "{sheet_url}" WHERE name = "{a1}"')
    rows = run_query(f'SELECT * FROM "{sheet_url}"')
    # Print results.
    print(rows)
    n = 0
    for row in rows:
        if f"{row.name}" == a1 and f"{row.num}" == a2 and f"{row.lastname}" == a3:
            #st.write(f"{row.name} bag is: {row.status}:")
            row_ty = f"{row.num}"
            print(type(row_ty))
            sta = row.status
            print(sta)
            if sta == "EM BAG SPA_Reparaturstatus_1_angeboterhalten.png":
                st.write(f"Your bag status is: Angeboterhalten")
                image = Image.open('mc.png')
                st.image(image,width = 300)
                print('1')
            elif sta == "EM BAG SPA_Reparaturstatus_2_reparaturinbearbeitung.png":
                st.write(f"Your bag status is: Reparaturinbearbeitung")
                image = Image.open('2.png')
                #st.image(image,width = 260)
                st.image(image,use_column_width = "auto")
            elif sta == "EM BAG SPA_Reparaturstatus_3_produktinqualitaetskontrolle.png":
                st.write(f"Your bag status is: Produktinqualitaetskontrolle")
                image = Image.open('3.png')
                st.image(image, use_column_width = "auto")
            elif sta == "EM BAG SPA_Reparaturstatus_4_auftragabgeschlossen.png":
                st.write(f"Your bag status is: Auftragabgeschlossen")
                image = Image.open('4.png')
                st.image(image, use_column_width = "auto")
            elif sta == "EM BAG SPA_Reparaturstatus_5_zurabholungbereit.png":
                st.write(f"Your bag status is: Zurabholungbereit")
                image = Image.open('5.png')
                st.image(image, use_column_width = "auto")
            

            n+=1
    if n == 0:
        st.write(f"Vielen Dank für Ihre Abfrage. Derzeit gibt es noch keinen Status zu Ihrer Reparatur. Bitte schauen Sie in wenigen Tagen noch einmal vorbei.")


st.title('EM Bag Service Status Tracking')
# st.subheader('This is a subheader')
whichcasno1 = st.text_input('Enter First Name', value = '', max_chars = None, key = 1, type = 'default', help = 'Alice')
whichcasno3 = st.text_input('Enter Last Name', value = '', max_chars = None, key = 3, type = 'default', help = 'Alice')
whichcasno2 = st.text_input('Enter Order Num', value = '', max_chars = None, key = 2, type = 'default', help = 'R101')

if whichcasno1!='' and whichcasno2!='':
    #st.write('Your bag service staus is following:')
    query_test = search(whichcasno1,whichcasno2)




