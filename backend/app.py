import streamlit as st
import requests
import json

dialog_sms_url ="http://127.0.0.1:8000/sendMessageDialog"

def dialogSms():
    st.markdown("# Dialog SMS")
    txt_message=st.text_input("Message")
    btn_dialog_sms=st.button("Dialog SMS")

    if btn_dialog_sms:
        session = requests.Session()
        try:
            data ={
                    "message":txt_message
                }
            result = session.post(dialog_sms_url)
            st.write(result)
        except Exception:
            st.write("Error")
    

def mobitelSms():
    st.markdown("# Mobitel SMS")

def whatsapp():
    st.markdown("# Whatsapp")


page_names_to_funcs = {
    "Dialog SMS": dialogSms,
    "Mobitel SMS": mobitelSms,
    "Whatsapp": whatsapp,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()