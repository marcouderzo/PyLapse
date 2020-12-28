#Require:
# https://github.com/loonghao/photoshop-python-api
# 

import photoshop.api as ps
from photoshop import Session
from pynput.mouse import Listener

ps = Session(action="active_document")

def onClick(x, y, button, pressed):
        doc = ps.active_document
        print(doc)
        options = ps.JPEGSaveOptions(quality=5)
        jpg = 'C:/Users/marco/Desktop/test.jpg'
        doc.saveAs(jpg, options, asCopy=True)
        pass


with Listener(on_click=onClick) as listener:
        listener.join()



