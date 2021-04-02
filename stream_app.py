import yfinance as yf
import streamlit as st

import requests
def send_req(x):
    url = 'http://127.0.0.1:9000/result'
    myobj = {"txt":x}

    x = requests.post(url, json = myobj)

    return x.text



st.write("""
# Sentiment Analysis
""")


st.write("""
## Enter Text Here
""")

txt = st.text_input("Enter Your Text","")


if st.button("Submit"):
    result = send_req(txt)
    st.success(result)