# This is for secound page in web to contact us
import streamlit as st

st.header('Contact Me')

with st.form(key='email_forms'): #create form dialog box
    user_email = st.text_input('Your email address') #1st dialog box
    raw_message = st.text_area('Your message') # message dialog box
    message = f"""
Subject: New email from {user_email}

From: {user_email}
{raw_message}

"""
    button = st.form_submit_button('Submit') # button for submission
    print(button)
    if button:
        send_email(message)
        st.info('Your msg send successfullly')
# To save the email we have created another py file named as send_email