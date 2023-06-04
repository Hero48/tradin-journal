from database import *

import streamlit as st

# Display a line chart of records from the database
st.subheader('Trade ID')
username = st.text_input('', placeholder='Username')


# Query the database for all trades by User


# display a line chart between the number of trades and the balance
trades = Session(bind=engine).query(Trade).filter_by(user=username).all()
all_trades = []



won = []
lost = []

for trade in trades:
    if trade.status == 'Won':
        won.append(trade.balance)
    else:
        lost.append(trade.balance)




total_trades = len(trades)
    




for trade in trades:
    all_trades.append(trade.balance)
   



if total_trades != 0:
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
            <div class="trade-card", style="color: #c1e6c2 ;">
            <h3>Total Trades</h3>
            <br>
            <h2>{total_trades}</h2>

            """, unsafe_allow_html=True)
        
    with col2:
        st.markdown(f"""
            <div class="trade-card", style="color: #c1e6c2 ;">
            <h3>Total Wins</h3>
            <br>
            <h2>{len(won)}</h2>

            """, unsafe_allow_html=True)
        
    with col3:
     st.markdown(f"""
        <div class="trade-card", style="color: #c1e6c2 ;">
        <h3>Total Loss</h3>
        <br>
        <h2>{len(lost)}</h2>

        """, unsafe_allow_html=True)
if total_trades != 0:
    st.markdown(f"""
                <br>
        <div class="trade-card", style="color: #c1e6c2 ; width: 100%;">
            <h3>Win Rate</h3>
            <br>
        <h2>{(len(won)/total_trades)*100 :.2f}</h2>


            """, unsafe_allow_html=True)

st.write('___')





   
data = {'Balance': all_trades}
st.line_chart(data)


st.markdown("""
<style>
.trade-card {
 background: rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(10px);
  border-radius: 10px;
  padding: 20px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  width: 200px;

}

</style>
""", unsafe_allow_html=True)

