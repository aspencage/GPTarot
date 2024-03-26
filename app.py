import streamlit as st 
import argparse
from gptarot import title_text
from tarot_stream import tarot_stream
from helpers import manage_authentication


parser = argparse.ArgumentParser()
parser.add_argument('--noauth', action='store_false', help='Include this flag after two dashes and a space to bypass the authentication page (i.e., streamlit run app.py -- --noauth)')
args = parser.parse_args()
auth_needed = args.noauth

def main(auth_needed:bool=True):
    st.set_page_config(page_title="🔮 GPTarot 🔮")

    st.title(title_text)

    # prepare authorization
    if auth_needed:
        manage_authentication()

    else: 
        tarot_stream() 

main(auth_needed)