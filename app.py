import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import bcrypt
from streamlit_chat import message
import requests

#hashed_passwords = stauth.Hasher(['123', '456']).generate()
#print(hashed_passwords)



st.title(":blue[Trading Bot] 🤖")

with st.container():

    with open('login.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)

    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['preauthorized']
    )

    name, authentication_status, username = authenticator.login('Login', 'main')


    if st.session_state["authentication_status"]:
        authenticator.logout('Logout', 'main')
        st.write(f'Welcome *{st.session_state["name"]}*')
        st.title('Some content')
    elif st.session_state["authentication_status"] is False:
        st.error('Username/password is incorrect')
    elif st.session_state["authentication_status"] is None:
        st.warning('Please enter your username and password')

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            footer:after{
                content: 'Made by Group 3";
                display:block;
                position: relative;
                color:tomato;
                padding:5px;
                top:3px;
            }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
