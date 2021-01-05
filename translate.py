import pandas as pd
import datetime
import eel
import sys
from googletrans import Translator

def translate_execute(source, origin_lang, trans_lang):
    translator = Translator(service_urls=['translate.googleapis.com'])
    result_text = (translator.translate(source, src="{}".format(origin_lang) ,dest="{}".format(trans_lang)).text)
    eel.set_trans_result(result_text)