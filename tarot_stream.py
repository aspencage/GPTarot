# tarot_stream.py

import streamlit as st 
from collections import Counter
from gptarot import *
from tarot_deck import *

st.set_page_config(page_title="🔮 GPTarot 🔮")
st.title(title_text)
st.write(intro_text)

reading = st.selectbox("Which type of Tarot spread shall we do?", Reading,index=0,key="spread")

st.write(gen_reading_text(reading))

deck = Deck()
question = st.text_input(question_ask)


if st.checkbox("Randomly draw my three cards"):
    c1,c2,c3 = deck.draw_random_cards(3)
    st.write(f"Your three randomly drawn cards are: `{c1}`,`{c2}`, and `{c3}`.")

else: 
    c1 = st.selectbox(c1_ask,deck.base_cards,key="card_select_1") 
    c2 = st.selectbox(c2_ask,deck.base_cards,key="card_select_2")
    c3 = st.selectbox(c3_ask,deck.base_cards, key="card_select_3")

cs = [c1.name,c2.name,c3.name]
duplicate_check = lambda l: sum(Counter(l).values()) > len(Counter(l))

if st.button("Read the cards"):

    if reading == Reading.NULL:
        st.write("You must select which type of spread you would like before I can conduct a reading.")

    elif duplicate_check(cs):
        duplicated = [val for val,count in Counter(cs).items() if count>1] # there can only be 1 duplicated card value in a three card draw 
        dup_str = f"You cannot select duplicate cards. Currently there are multiple copies of {duplicated[0]} chosen. Please adjust your choices and we will continue with the reading."
        st.write(dup_str)

    else:
        with st.spinner(wait_msg):
            reading = read_three_card_spread(question,c1,c2,c3)
        
        st.write("My reading for you:")
        st.write(reading)