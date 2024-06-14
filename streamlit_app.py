import streamlit as st
import sqlite3

conn = sqlite3.connect('dane.db', check_same_thread=False)
cursor = conn.cursor()

st.title("Welcome")

def form_creation():
    st.write("Fill the form")
    with st.form(key="Registracion form"):
        surname = st.text_input('surname: ')
        name = st.text_input('name: ')
        date = st.date_input('podaj date')
        submit = st.form_submit_button(label='Register')
    
    if submit == True:
        st.success("Success")
        add_info(surname, name, date)
        
    
def add_info(a,b,c):
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS registracion (SURNAME TEXT(50), NAME TEXT(50), DATE TEXT(50) )
        """
    )
    cursor.execute("INSERT INTO registracion VALUES (?,?,?)", (a,b,c))
    conn.commit()
    conn.close()
    st.success("SQLITE update")
form_creation()

