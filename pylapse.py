from PIL import ImageGrab

import os, time
from datetime import datetime





def init():
    mode = input("Please select Run Mode. Type: < capture > to start taking frames, < create > to compile the final timelapse. >> ")
    retargs=["a", "a", "a", "a"]
    if mode == "capture":
        relPath=input("Type Output Folder Name >> ") + '/'
        cooldownTime=input("Type Time Interval Between Frames (seconds) >> ")
        retargs[1]= relPath
        retargs[2]= int(cooldownTime)
    if mode == "create":
        fps = input("Type Desired Framerate >> ")  
        retargs[3]= int(fps)

    retargs[0]= mode
    return retargs


def saveFrame(relPath):
    im = ImageGrab.grab()
    dt = datetime.now()
    fname = "frame_{}.{}.png".format(dt.strftime("%d-%m-%Y %H:%M:%S"), dt.microsecond // 100000)
    im.save(relPath+fname, 'png')

    

# Main



args = init()

if args[0] == "capture":
    print("From Now, Every " + str(args[2]) + " Seconds a Screenshot Will Be Saved.")
    while True:
        saveFrame(args[1])
        time.sleep(args[2])

if args[0] == "create":
    os.system('ffmpeg -framerate %d -i %s -c:v libx264 -r 20 -pix_fmt yuv420p %s/%d.mp4' % (args[3],"png", "space",int(time.time())))
