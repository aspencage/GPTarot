import streamlit as st 
import argparse
from gptarot import title_text
from helpers import *
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

parser = argparse.ArgumentParser()
parser.add_argument('--noauth', action='store_false', help='Include this flag after two dashes and a space to bypass the authentication page (i.e., streamlit run app.py -- --noauth)')
args = parser.parse_args()
auth_needed = args.noauth

def main(auth_needed:bool=True):
    st.set_page_config(page_title="🔮 GPTarot 🔮")

    st.title(title_text)

    if auth_needed:
        with open(YAML_PATH) as file:
            config = yaml.load(file, Loader=SafeLoader)

        authenticator = stauth.Authenticate(
            config['credentials'],
            config['cookie']['name'],
            config['cookie']['key'],
            config['cookie']['expiry_days']
        )

        # initial settings
        if "back_clicked" not in st.session_state:
            st.session_state.back_clicked = True

        if "create_clicked" not in st.session_state:
            st.session_state.create_clicked = False

        if "login_clicked" not in st.session_state:
            st.session_state.login_clicked = False

        if st.session_state.back_clicked:
            st.write("")
            st.write("🧚 Welcome! GPTarot only works for humans, not bots. Log in to show us that you are indeed a human. 🍃")
            st.write("")
            _, col1, col2, _ = st.columns([1,1,1,1])

            with col1:
                st.button("Create account", key="create", on_click=click_create)

            with col2:
                st.button("Log in", key="login", on_click=click_login)

        if st.session_state.create_clicked:
            register(authenticator, config)

        if st.session_state.login_clicked:
            authenticate(authenticator)

    else: 
        tarot_stream() 

main(auth_needed)