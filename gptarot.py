from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate 
from langchain.chains import LLMChain

llm = OpenAI(temperature=0.9)

def read_three_card_spread(q,c1,c2,c3):
        print("~~~🌱🔮✨ WELCOME TO GPTAROT ✨🔮🌱~~~")
        print("Thank you for allowing me to read your cards.") 
        print("Please, sit down and have a cup of tea. 🫖 🍵")
        print("We will do a simple three card draw, where your first card is your past, your second card is your present, and your third card is the future.\n")

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

        print("\nGive me a moment to listen to the cards... 🧘‍\n")

        chain = LLMChain(llm=llm, prompt=prompt)

        r = chain.run(d)

        return(r.strip())

if __name__ == "__main__":
        question = input("So, what question would you like to ask the cards? ")
        card1 = input("What is your first card? ") 
        card2 = input("What is your second card? ")
        card3 = input("What is your third card? ")
        reading = read_three_card_spread(question,card1,card2,card3)
        print(reading)