import eel
import desktop
import translate

app_name="html"
end_point="index.html"
size=(700,600)

@ eel.expose
def translate_execute(source, origin_lang, trans_lang):
    translate.translate_execute(source, origin_lang, trans_lang)
 
desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)