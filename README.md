# 🌱🔮✨ Welcome to GPTarot ✨🔮🌱

## Let a large language model read the cards for you.

`GPTarot` is a just-for-fun project getting ChatGPT to conduct three card tarot readings. All you need to do is choose your spread and tone, ask a question, and pick three cards (or let randomization do the thinking for you). I recommend drawing randomly from a real tarot deck if you have one onhand. GPTarot will do the rest.

**Customizations:**
* In addition to asking GPTarot your question with particular cards, you can select the tarot spread and tone for your reading.  
* *Spreads*: Currently, GPTarot can do a Past, Present, Future or a Body, Mind, Spirit Tarot spread. 
* *Tones*: Currently, GPTarot can conduct your reading along one of the following themes: mystical, witchy, taro root-themed, pun-oriented, or 90s pop culture references. Let me know if you have any requests for additional tones!

**Experience GPTarot online:**
* GPTarot is now hosted on an AWS EC2 instance and can be accessed live.
* Current address: http://13.59.230.190:8501/.
* GPTarot will be hooked up to a vanity domain in the near future.

**Run GPTarot yourself:**
* You can also run the code for GPTarot on your local machine!
* After meeting the installation requirements below, you can run GPTarot with a graphical user inferface by navigating to the repository and running `streamlit run app.py` on the command line.
* Alternatively, if you prefer a simple presentation, you can simply run `gptarot.py` on the command line. 
* *Requirements*:
  * 1. Have an OpenAI API account and set your machine's `OPENAI_API_KEY` environment variable.
  * 2. Install the requisite Python packages in the `environment.yml` file. The packages that are not part of a typical Python data stack are: `langchain`, `streamlit`, `openai`, and `tiktoken`. I recommend simply creating a Conda environment from this file directly with `mamba env create -f environment.yml`.

**Forthcoming features**: 
* Vanity domain for the web-hosted GPTarot
* Tweaks for convenience and readability
* Options to download and share your reading
* DALL-E visualizations related to your reading?
