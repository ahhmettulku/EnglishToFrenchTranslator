""" Translator Module  """
from deep_translator import MyMemoryTranslator

Translater = MyMemoryTranslator


def english_to_french(english_text):
    """ Translation function from english to french"""
    # write the code here
    translated_text = Translater(
        source="english", target="french").translate(english_text)
    return translated_text


def french_to_english(french_text):
    """ Translation function from french to english"""
    # write the code here
    translated_text = Translater(
        source="french", target="english").translate(french_text)
    return translated_text
