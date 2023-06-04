import streamlit as st

def main():
    st.title('How to Use Trading Journal')
    
    st.markdown('Welcome to the Trading Journal app! This app allows you to keep track of your trades and analyze your trading performance. Here are the steps to use the app:')
    
    st.header('Step 1: Record Trade')
    st.markdown('In the "Record Trade" section, enter your trade details such as Forex pair, risk/reward ratio, session, status, etc. You can also add comments and upload a screenshot if needed.')
    
    st.header('Step 2: Save Trade')
    st.markdown('Click the "Save Trade" button to save your trade record. The app will calculate your new balance based on the trade result and update the database.')
    
    st.header('Step 3: View Trade Records')
    st.markdown('In the "Trade Records" section, enter your username and click the "Display" button. The app will retrieve your trade records from the database and display them in a card format. You can see details such as trade ID, Forex pair, session, risk/reward, etc. You can also view the screenshot of a trade by clicking the "View Screenshot" button.')
    
    st.header('Step 4: Analyze Performance')
    st.markdown('The app provides a line chart that shows the balance of your trades over time. You can analyze your trading performance based on the chart. Additionally, the app displays summary statistics such as total trades, total wins, total losses, and win rate.')
    
    st.markdown('That\'s it! You now know how to use the Trading Journal app. Start recording your trades and analyzing your performance. Happy trading!')
    
    st.markdown('---')
    
    st.markdown('### Notes')
    st.markdown('This app is for demonstration purposes only and does not provide actual trading functionality. The data used in the app is not real-time and is only for illustrative purposes.')
    st.markdown('Please make sure to use proper risk management and do thorough research before making any trading decisions.')
    st.markdown('---')

if __name__ == "__main__":
    main()
