import pandas as pd
import datetime
import eel
import sys
from googletrans import Translator

def translate_ja(source, origin_lang, trans_lang):
    print("元文は:{}".format(source))
    translator = Translator(service_urls=['translate.googleapis.com'])
    print('翻訳結果---->',translator.translate(source, src="{}".format(origin_lang) ,dest="{}".format(trans_lang)).text)
    result_text = (translator.translate(source, src="{}".format(origin_lang) ,dest="{}".format(trans_lang)).text)
    eel.set_ja(result_text)