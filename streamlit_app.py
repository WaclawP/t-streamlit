import streamlit as st
import pymysql.cursors

# Podanie danych połączenia
db_host = "sql125.lh.pl"
db_user = "serwer274744_streamlit"
db_password = "bazabazA3#"
db_name = "serwer274744_streamlit"

# Utworzenie połączenia
db_connection = pymysql.connect(host=db_host,
                                user=db_user,
                                password=db_password,
                                database=db_name,
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

cursor = db_connection.cursor()

st.title("Welcome")

def form_creation():
    st.write("Fill the form")
    with st.form(key="Registracion form"):
        name = st.text_input('name: ')
        age = st.text_input('age: ')
        submit = st.form_submit_button(label='Register')
    
    if submit == True:
        st.success("Success")
        add_info(name, age)
        
    
def add_info(name,age):
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS data (name VARCHAR(50), age VARCHAR(50))
        """
    )
    cursor.execute(f"""INSERT INTO data VALUES (1,2)""")
    db_connection.commit()
    db_connection.close()
    st.success("SQLITE update")
form_creation()

