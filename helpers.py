import streamlit as st 
from tarot_stream import tarot_stream
import yaml

YAML_PATH = 'credentials.yml'

def click_create():
    st.session_state.back_clicked = False
    st.session_state.create_clicked = True
    st.session_state.login_clicked = False


def click_login():
    st.session_state.back_clicked = False
    st.session_state.login_clicked = True
    st.session_state.create_clicked = False


def click_back():
    st.session_state.back_clicked = True
    st.session_state.create_clicked = False
    st.session_state.login_clicked = False


def show_back():
    st.button("Back", key="back", on_click=click_back)


def blank_space(n:int=1):
    for _ in range(n):
        st.write("")


def authenticate(authenticator):
    _, authentication_status, _ = authenticator.login('Who seeks the wisdom of the cards?', 'main')
    
    if authentication_status:
        tarot_stream() 
        blank_space(7)
        authenticator.logout('Log out', 'main')
    elif authentication_status == False:
        st.error("That's not quite right. Would you like to try again?", icon="😕")
        show_back()
    elif authentication_status == None:
        show_back() 


def register(authenticator, config):
    try:
        if authenticator.register_user('Register user', preauthorization=False):
            st.success('You registered successfully. GPTarot will now read your cards.')
            with open(YAML_PATH, 'w') as file:
                    yaml.dump(config, file, default_flow_style=False)
    except Exception as e:
        st.error(e)
    show_back()
