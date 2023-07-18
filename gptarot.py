from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate 
from langchain.chains import LLMChain

llm = OpenAI(temperature=0.9)

title_text = "~~~🌱🔮✨ WELCOME TO GPTAROT ✨🔮🌱~~~"

intro_text = """
Thank you for allowing me to read your cards.
Please, sit down and have a cup of tea. 🫖 🍵

We will do a simple three card draw, where your first card is your past, your second card is your present, and your third card is the future.
You can either select the three cards yourself for me to interpret or I can draw the cards from my digital deck.

Before we begin, bear in mind I am powered by the collective wisdom - and folly - of human knowledge. 
I hope to enchant you, but promise nothing beyond entertainment.
"""

question_ask = "So, what question would you like to ask the cards? "
c1_ask = "What is your first card? "
c2_ask = "What is your second card? "
c3_ask = "What is your third card? "
wait_msg = "\nGive me a moment to listen to the cards and to drink from the font of documented knowledge... 🧘‍\n"

# TODO add different language - witchy and magical, taro root, pun oriented?, pop culture  

def read_three_card_spread(q,c1,c2,c3):

        template_text='''We have a classic tarot card deck with both major and minor arcana. You are the tarot card reader. We are doing a three card draw. I want to ask the cards 
        the following question: "{question}" First, I draw the card “{card1}” to represent the past. Next, I draw the card “{card2}" to represent the present. Finally, I draw the 
        card “{card3}” to represent the future. Interpret the cards to answer my question in 100 words or less, using an extremely witchy and magical vocabulary.'''

        prompt = PromptTemplate.from_template(template_text)

        d = {
                "question":q,
                "card1":c1,
                "card2":c2,
                "card3":c3
                }

        chain = LLMChain(llm=llm, prompt=prompt)

        r = chain.run(d)

        return(r.strip())


if __name__ == "__main__":
        print(title_text,"\n")
        print(intro_text)

        question = input(question_ask)
        card1 = input(c1_ask) 
        card2 = input(c2_ask)
        card3 = input(c3_ask)
        print(wait_msg)
        reading = read_three_card_spread(question,card1,card2,card3)
        print(reading)