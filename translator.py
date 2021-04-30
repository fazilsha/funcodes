
from googletrans import Translator
print("E.g ")
language = input("Enter the language to translate: ")
translator = Translator()
text=input("Enter your text: ")
translation = translator.translate(text,dest=language)
print(translation.text)
