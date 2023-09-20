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

    def get_description(self):
        m = self.get_meanings()
        desc = f"In this spread, your first card describes {m[0]}, your second card describes {m[1]}, and your third card describes {m[2]}.\n"
        self.description = desc
        return desc 

    def __repr__(self):
        return self.value

    def __str__(self):
        return self.value
    

class Lingo(Enum):

    STD = "Mystical"
    WITCH = "Witchy"
    TARO = "Taro root-themed"
    PUNS = "Pun-oriented"
    THROWBACK = "Nineties pop-culture"

    def get_description(self):
        desc = f"Your vocabulary and tone are both extremely {self}. "
        
        if self == Lingo.STD:
            desc += "Be mysterious. Your vocabulary and explanations should draw on a variety of mystical and spiritual traditions, including astrology and gem stones. You may wish to consider the current position of the planets, zodaical constellation, and the current moon phase. You may also wish to consider gemastones that relate to the cards."
        elif self == Lingo.WITCH:
            desc += "Conduct your reading from the perspective of a witch, who lives in a swamp, flies on a broomstick, creates potions, has animal familiars, and casts spells on the townsfolk. Write in the way that an ancient witch would speak. Be spooky. Introduce yourself with a name that sounds like it would be the name of an ancient witch. Make at least two references to things related to witches." 
        elif self == Lingo.TARO:
            desc += "Conduct your reading making direct references to the plant taro, including its botany and life-cycle. Bring at least two scientific facts about the taro root into your reading. You may make puns about the tarot root. You may wish to reference the scientific name of the tarot root. You may reference botanical facts about other plants, as long as they are related to the tarot root."
        elif self == Lingo.PUNS:
            desc += "As much as possible, make puns that tie in the specific tarot cards chosen or the question asked. This reading should be funny and silly. Make at least five puns in this reading."
        elif self == Lingo.THROWBACK:
            desc += "Conduct your reading from the perspective of someone living in the 1990s. Reference popular music, celebrities, and movies. Quote famous movies or hit songs from this period at least three times. Use slang that was popular in the Nineties."

        self.description = desc
        return desc

    def __repr__(self):
        return self.value

    def __str__(self):
        return self.value


def load_llm(temp=0.9, max_tokens=-1):
    llm = OpenAI(temperature=temp, max_tokens=max_tokens)
    return llm


title_text = "🌱🔮✨ GPTarot ✨🔮🌱"

question_ask = "So, what question would you like to ask the cards? "
c1_ask = "What is your first card? "
c2_ask = "What is your second card? "
c3_ask = "What is your third card? "
wait_msg = "\nGive me a moment to listen to the cards and to drink from the fount of documented knowledge... 🧘‍\n"
     
intro_text = textwrap.dedent(f"""
    Thank you for allowing me to read your cards.
    Please, sit down and have a cup of tea. 🫖 🍵

    Before we begin, bear in mind I am powered by the collective wisdom - and folly - of human knowledge. 
    I hope to enchant you, but promise nothing beyond entertainment.
                             
    """)


def gen_reading_text(reading:Reading):
    if reading != Reading.NULL:

        reading_text = textwrap.dedent(f"""

            We will do a simple three card reading of the {reading} spread. {reading.get_description()}
            You can either select the three cards yourself for me to interpret or I can draw the cards randomly from my digital deck.
            """)
    
    else:
         reading_text = ""

    return reading_text


def read_three_card_spread(llm:OpenAI,q:str,c1:str,c2:str,c3:str,reading=Reading.PPF,lingo=Lingo.STD):
        m1,m2,m3 = reading.meanings

        template_text='''We have a tarot card deck with both major and minor arcana. You are the tarot card reader. We are doing a {reading} three card draw. I want to ask the cards 
        the following question: "{question}" First, I draw the card “{card1}” to represent {meaning1}. Next, I draw the card “{card2}" to represent {meaning2}. Finally, I draw the 
        card “{card3}” to represent {meaning3}. {lingo}''' 

        prompt = PromptTemplate.from_template(template_text)

        d = {
                "question":q,
                "card1":c1,
                "card2":c2,
                "card3":c3,
                "reading":reading,
                "meaning1":m1,
                "meaning2":m2,
                "meaning3":m3,
                "lingo":lingo.get_description()
                }

        chain = LLMChain(llm=llm, prompt=prompt)

        r = chain.run(d)

        return(r.strip())

# TODO main function(), including interactivity for spread and lingo


if __name__ == "__main__":
        print(title_text,"\n")
        print(intro_text.strip())
        print("\n")
        reading_in = Reading.PPF
        lingo = Lingo.TARO

        print(gen_reading_text(reading_in).strip())
        print("\n")
        llm = load_llm()

        question = input(question_ask) # How can I improve my relationship with my family? 
        card1 = input(c1_ask) # Two of Swords
        card2 = input(c2_ask) # Six of Pentacles
        card3 = input(c3_ask) # Justice
        print(wait_msg)
        reading_out = read_three_card_spread(llm,question,card1,card2,card3,reading_in,lingo)
        print(reading_out)