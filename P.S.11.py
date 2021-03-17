# -*- coding: utf-8 -*-
import streamlit as st
import datetime as dt
import pandas_datareader as pdr

today_date = dt.date.today()
start_date = today_date - dt.timedelta(days=365)
st.write("# Stock Closing Prices")
st.sidebar.header("Enter Stock Information")
stocky = st.sidebar.text_input("Stock Name", "NTDOY")
start = st.sidebar.text_input("Start Date",f"{start_date}")
end = st.sidebar.text_input("End Date",f"{today_date}")
st.write(f"## {stocky}")
button = st.sidebar.button("Create Chart")

if button:
    stocky = stocky.upper()
    data = pdr.get_data_yahoo(stocky, start, end)
    st.line_chart(data["Close"])
