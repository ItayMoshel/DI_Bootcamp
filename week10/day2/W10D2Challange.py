from translate import Translator

french_words = ["hello", "see you later", "chair", "desk"]
translator = Translator(to_lang="he")
translation = translator.translate(french_words[2])
print(translation)

