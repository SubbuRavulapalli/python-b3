from newspaper import *
import nltk
from gtts import gTTS
import os

# Get the article
article = Article('https://www.thehindu.com/society/go-green-with-your-diwali-gift-hampers-this-festive-season/article66004238.ece')

article.download()
article.parse()

nltk.download('punkt')
article.nlp()

# Get the articles text
mytext = article.text

language = 'en'  # English

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("News_article.mp3")

os.system("start read_article.mp3")