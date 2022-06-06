import streamlit as st
import requests

dialog_sms_url ="http://127.0.0.1:8000/sendMessage/dialog"

btn_dialog_sms=st.button("Dialog SMS")

if btn_dialog_sms:
    session = requests.Session()
    try:
        result = session.post(dialog_sms_url)
        st.write(result)
    except Exception:
        st.write("Error")
    