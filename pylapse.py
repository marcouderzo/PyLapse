from PIL import ImageGrab

import os, time
from datetime import datetime



def getNumberOfFrames(dir):
    list = os.listdir(dir)
    return len(list)

def init():
    args=["", "", "", ""]    
    args[0]=input("Type Output Folder Name >> ") + '/'
    args[1]=int(input("Type Time Interval Between Frames (seconds) >> "))
    args[2]= getNumberOfFrames(args[0])
    return args


def saveFrame(relPath, index):
    im = ImageGrab.grab()
    dt = datetime.now()
    fname = "frame_{}.png".format(index)
    im.save(relPath+fname, 'png')
    return index+1





# Main

def main():
    args = init()
    relativePath = args[0]
    cooldownTime = args[1]
    print("From Now, Every " + str(cooldownTime) + " Seconds a Screenshot Will Be Saved.")
    while True:
        numberOfFrames = saveFrame(relativePath, numberOfFrames)
        time.sleep(cooldownTime)
        
if __name__ == "main":
    main()
       
