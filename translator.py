from googletrans import Translator

def translate(text):
    translator = Translator()
    return list(zip(text, [i.text for i in translator.translate(text, dest='hi', src='en')]))