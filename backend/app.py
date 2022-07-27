import streamlit as st
import requests
import json

dialog_sms_url ="http://127.0.0.1:8000/sendMessageDialog/"

def dialogSms():
    st.markdown("# SMS")
    mask = st.selectbox('Select Your Mask ?',('kainovation', 'Data.io'))
    txt_message=st.text_area("Message")
    number=st.text_input("Number")
    btn_dialog_sms=st.button("Send")

    if btn_dialog_sms:
        session = requests.Session()
        try:
            headers = {
                'accept': 'application/json',
                'content-type': 'application/x-www-form-urlencoded',
            }

            params = {
                'number':  number,
                'message': txt_message,
            }

            response = session.post(dialog_sms_url, params=params, headers=headers)
            st.write(response)
            st.write(response.text)
        except Exception:
            st.write("Error")
    

def dialogSmsBulk():
    st.markdown("# SMS Bulk")
    mask = st.selectbox('Select Your Mask ?',('kainovation', 'Data.io'))
    txt_message=st.text_area("Message")
    file=st.file_uploader("Upload Number List","csv")
    btn_dialog_sms=st.button("Send")
    st.write(mask)
   
    if btn_dialog_sms:
        session = requests.Session()
        try:
            headers = {
                'accept': 'application/json',
                # requests won't add a boundary if this header is set when you pass files=
                # 'Content-Type': 'multipart/form-data',
            }

            params = {
                'message': txt_message,
            }

            files = {
                'file': file,
            }

            response = session.post('http://127.0.0.1:8000/sendBulkDialog', params=params, headers=headers, files=files)
            st.write(response)
            st.write(response.text)
        except Exception:
            st.write("Error")

def whatsapp():
    st.markdown("# Whatsapp")


page_names_to_funcs = {
    "SMS": dialogSms,
    "SMS Bulk": dialogSmsBulk,
    "Whatsapp": whatsapp,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()