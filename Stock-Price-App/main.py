from datetime import datetime 
import yfinance as yf
import streamlit as st  
import pandas as pd

#Stock Price App
st.write("""
# Stock Price App

Shown are the **stock closing price** and **volume** of Google 

""")

amzn = yf.Ticker("AMZN")
end_date = datetime.now().strftime('%Y-%m-%d')
print(end_date)
amzn_hist = amzn.history(start='2023-01-01',end=end_date)
print(amzn_hist)

st.write("""
# **Closing Price**

""")
st.line_chart(amzn_hist.Close)
st.write("""
# **Volume**

""")
st.line_chart(amzn_hist.Volume)

