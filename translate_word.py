from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate 
from langchain.chains import LLMChain

llm = OpenAI(temperature=0.9)

template_text = "Translate the word {word} from English to {language}."
prompt = PromptTemplate.from_template(template_text)

word = input("What word would you like to translate? ")
language = input("What language would you like to translate it into? ")

print("\nPROMPT:", prompt.format(word=word,language=language))

chain = LLMChain(llm=llm, prompt=prompt)

d = {
	"word":word,
	"language":language
	}

r = chain.run(d)

print("\nRESPONSE:", r.strip())
