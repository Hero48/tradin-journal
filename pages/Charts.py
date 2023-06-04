from database import *

import streamlit as st

# Display a line chart of records from the database

username = st.text_input('', placeholder='Username')


# Query the database for all trades by User
trades = Session(bind=engine).query(Trade).filter_by(user=username).all()