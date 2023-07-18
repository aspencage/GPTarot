# tarot_stream.py

import streamlit as st 
from collections import Counter
from gptarot import *
from tarot_deck import *

'''
NOTE need to install streamlit in `langu` (which has OpenAI)
    instrealit installation erroprs
    try the conda-forge build 1.24.0 which is working for paper plane project

TODO add an authentication service before spinning up online version 
'''

st.set_page_config(page_title="🔮 GPTarot 🔮")
st.title(title_text)
st.write(intro_text)

deck = Deck()
question = st.text_input(question_ask)

if st.checkbox("Randomly draw my three cards"):
    c1,c2,c3 = deck.draw_random_cards(3)
else:
    c1 = st.selectbox(c1_ask,deck.base_cards) 
    c2 = st.selectbox(c2_ask,deck.base_cards)
    c3 = st.selectbox(c3_ask,deck.base_cards)

cs = [c1,c2,c3]
duplicate_check = lambda l: sum(Counter(l).values()) > len(Counter(l))

if st.button("Read the cards"):

    if duplicate_check(cs):
        duplicated = [val for val,count in Counter(cs).items() if count>1] 
        # there can only be 1 duplicated card value in a three card draw 
        dup_str = f"You cannot select duplicate cards. Currently there are multiple copies of {duplicated[0]} chosen. Please adjust your choices and we will continue with the reading."
        st.write(dup_str)

    else:
        st.write(wait_msg)

        # reading = read_three_card_spread(question,c1,c2,c3)
        # st.write(reading)