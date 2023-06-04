import streamlit as st
from database import *
import pandas as pd
import os


st.title('Trading Journal')

st.subheader('Record Trade')
st.subheader('User')
username = st.text_input('', placeholder='Username')
col1, col2 = st.columns(2)
with col1:
    forex_pair = st.selectbox('Forex Pair', ['USDJPY', 'EUROUSD', 'GBPUSD'])
    risk_reward = st.number_input('Profit Percentage')
    trade_session = st.selectbox('Session', ['London', 'Asian', 'NewYork'])
    status = st.selectbox('Status', ['Won', 'Lost', 'Break Even'])

with col2:
    buy_sell = st.selectbox('Buy/Sell', ['Buy', 'Sell'])
    time = st.time_input('Time')
    trade_date = st.date_input('Date')
    confirmation = st.multiselect('Confirmation', ['LQS', 'MSS', 'Displacement', 'FVG'])


comments = st.text_area('Comments')
screenshot = st.file_uploader('Screenshot', type=['jpg', 'png', 'jpeg'])

session = Session(bind=engine)
# query Trade database by user and get the balance value of the last item if it is a vailable
bal = session.query(Trade).filter_by(user=username).order_by(Trade.time.desc()).first()

bal = bal.balance
def calculate_balance(balance):
    if balance is not None:
        if status == 'Won':
            return balance + (balance * (risk_reward / 100))
        else:
            return balance - (balance * 0.01)
    else:
        return 100




if st.button('Save Trade'):
    image_name = screenshot.name
    with open(os.path.join("./images", image_name), "wb") as f:
        f.write(screenshot.getbuffer())
    image_path = os.path.join("./images", image_name)
    balance = calculate_balance(bal)
    st.subheader(balance)

    # Create a trade object and populate its attributes with the user inputs
    trade = Trade(forex_pair=forex_pair,
                  user=username,
                  risk_reward=risk_reward,
                  time=datetime.now(),
                  session=trade_session,
                  buy_sell=buy_sell,
                  trade_date=trade_date,
                  confirmation=', '.join(confirmation),
                  comments=comments, 
                  screenshot=image_name,
                  balance=balance,
                  status=status)

    # Add the trade object to the database
    with Session(engine) as session:
        session.add(trade)
        session.commit()

    st.success('Trade saved')
