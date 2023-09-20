# tarot_stream.py

import streamlit as st 
from collections import Counter
from gptarot import *
from tarot_deck import *


def stream_draw():
    drawn = Deck().draw_random_cards(3)
    for ix,c in enumerate(drawn):
        st.session_state[f"c{ix+1}"] = c


def tarot_stream():
    st.write(intro_text)

    reading_type = st.selectbox("Which type of Tarot spread shall we do?", Reading, index=0, key="spread")

    st.write(gen_reading_text(reading_type))

    lingo = st.selectbox("What tone and vocabulary should I use in the reading?", Lingo, index=0, key="lingo")

    question = st.text_input(question_ask)

    if "c1" not in st.session_state:
        stream_draw()

    if st.checkbox("Randomly draw my three cards",key="rand_box"):
        if st.button("Redraw cards"):
            stream_draw()

        c1 = st.session_state.c1
        c2 = st.session_state.c2
        c3 = st.session_state.c3
        st.write(f"Your three randomly drawn cards are: `{c1}`,`{c2}`, and `{c3}`.")

    else: 
        c1 = st.selectbox(c1_ask,Deck().base_cards,key="card_select_1",index=0) 
        c2 = st.selectbox(c2_ask,Deck().base_cards,key="card_select_2",index=1)
        c3 = st.selectbox(c3_ask,Deck().base_cards, key="card_select_3",index=2)

    cs = [c1.name,c2.name,c3.name]
    duplicate_check = lambda l: sum(Counter(l).values()) > len(Counter(l))

    with st.spinner("Accessing large language model tarot reader... 📚🔎"):
        llm = load_llm()

    if st.button("Read the cards"):

        if reading_type == Reading.NULL:
            st.write("You must select which type of spread you would like before I can conduct a reading.")

        elif duplicate_check(cs):
            duplicated = [val for val,count in Counter(cs).items() if count>1] # there can only be 1 duplicated card value in a three card draw 
            dup_str = f"You cannot select duplicate cards. Currently there are multiple copies of {duplicated[0]} chosen. Please adjust your choices and we will continue with the reading."
            st.write(dup_str)

        else:
            with st.spinner(wait_msg):
                reading = read_three_card_spread(llm,question,c1,c2,c3,reading_type, lingo)
            
            st.write("My reading for you:")
            st.write(reading)

if __name__ == "__main__":
    tarot_stream()