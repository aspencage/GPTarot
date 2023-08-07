# 🌱🔮✨ Welcome to GPTarot ✨🔮🌱

## Let a large language model read the cards for you.

`GPTarot` is a just-for-fun project getting ChatGPT to conduct three card tarot readings. All you need to do is choose your spread, ask a question, and choose three cards (or let randomization do the thinking for you). I recommend drawing randomly from a real tarot deck if you have one onhand. GPTarot will do the rest.

**Running GPTarot:**
* Currently, you must run the code for GPTarot on your local machine.
* After meeting the requirements below, you can run GPTarot with a graphical user inferface by navigating to the repository and running `streamlit run tarot_stream.py` on the command line.
* Alternatively, if you prefer a simple presentation, you can simply run `gptarot.py` on the command line. 

**Requirements:**
1. Have an OpenAI API account and set your machine's `OPENAI_API_KEY` properly.
2. Install the requisite Python packages in the `environment.yml` file. The packages that are not part of a typical Python data stack are: `langchain`, `streamlit`, `openai`, and `tiktoken`. I recommend simply creating a Conda environment from this file directly with `mamba env create -f environment.yml`.

**Forthcoming features**: 
* Web-hosted version behind an authentication page (to avoid bot spam), which will alow for use by anyone interested.
* Select different types of vocabulary for the tarot reading to use. 