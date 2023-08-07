from enum import Enum
import textwrap
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate 
from langchain.chains import LLMChain


class Reading(Enum):
    NULL = "--"
    PPF = "Past, Present, and Future"
    BMS = "Body, Mind, and Spirit"
    
    def get_meanings(self):
        if self == Reading.PPF:
            meanings = ["your past","your present","your future"]
        elif self == Reading.BMS:
             meanings = ["your body", "your mind", "your soul"]
        self.meanings = meanings
        return meanings
        # TODO write in the prompt components, creating a dictionary for card1,card2,card3

    def get_description(self):
        m = self.get_meanings()
        desc = f"In this spread, your first card describes {m[0]}, your second card describes {m[1]}, and your third card describes {m[2]}."
        self.description = desc
        return desc 

    def __repr__(self):
        return self.value

    def __str__(self):
        return self.value
    
def load_llm(temp=0.9):
    llm = OpenAI(temperature=temp)
    return llm

title_text = "🌱🔮✨ Welcome to GPTarot ✨🔮🌱"

question_ask = "So, what question would you like to ask the cards? "
c1_ask = "What is your first card? "
c2_ask = "What is your second card? "
c3_ask = "What is your third card? "
wait_msg = "\nGive me a moment to listen to the cards and to drink from the font of documented knowledge... 🧘‍\n"

# TODO add different language - witchy and magical, taro root, pun oriented?, pop culture  
     
intro_text = textwrap.dedent(f"""
    Thank you for allowing me to read your cards.
    Please, sit down and have a cup of tea. 🫖 🍵

    Before we begin, bear in mind I am powered by the collective wisdom - and folly - of human knowledge. 
    I hope to enchant you, but promise nothing beyond entertainment.""")


def gen_reading_text(reading:Reading):
    if reading != Reading.NULL:

        reading_text = textwrap.dedent(f"""

            We will do a simple three card reading of the {reading} spread. {reading.get_description()}
            You can either select the three cards yourself for me to interpret or I can draw the cards randomly from my digital deck.
            """)
    
    else:
         reading_text = ""

    return reading_text


def read_three_card_spread(llm, q,c1,c2,c3,reading=Reading.PPF):
        m1,m2,m3 = reading.meanings

        template_text='''We have a classic tarot card deck with both major and minor arcana. You are the tarot card reader. You use an extremely witchy and magical vocabulary. We are doing a {reading} three card draw. I want to ask the cards 
        the following question: "{question}" First, I draw the card “{card1}” to represent {meaning1}. Next, I draw the card “{card2}" to represent {meaning2}. Finally, I draw the 
        card “{card3}” to represent {meaning3}.  Interpret the cards to answer my question in about 200 words or fewer, making sure that you end with a complete sentence.''' 

        prompt = PromptTemplate.from_template(template_text)

        d = {
                "question":q,
                "card1":c1,
                "card2":c2,
                "card3":c3,
                "reading":reading,
                "meaning1":m1,
                "meaning2":m2,
                "meaning3":m3
                }

        chain = LLMChain(llm=llm, prompt=prompt)

        r = chain.run(d)

        return(r.strip())


if __name__ == "__main__":
        print(title_text,"\n")
        print(intro_text)
        reading_in = Reading.BMS # or BMS

        print(gen_reading_text(reading_in))
        llm = load_llm()

        question = input(question_ask)
        card1 = input(c1_ask) 
        card2 = input(c2_ask)
        card3 = input(c3_ask)
        print(wait_msg)
        reading_out = read_three_card_spread(llm, question,card1,card2,card3,reading_in)
        print(reading_out)