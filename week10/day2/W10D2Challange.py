from translate import Translator

english_words = ["hello", "see you later", "chair", "desk"]
translator = Translator(to_lang="he")
translation = translator.translate(english_words[2])
print(translation)

