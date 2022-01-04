from PIL import ImageGrab

import os, time
from datetime import datetime



def getNumberOfFrames(dir):
    list = os.listdir(dir)
    return len(list)

def init():
    args=["", "", "", "", ""]    
    args[0] = input("Please select Run Mode. Type: < capture > to start taking frames, < create > to compile the final timelapse. >> ")
    args[1]=input("Type Output Folder Name >> ") + '/'
    if args[0] == "capture":

        args[2]=int(input("Type Time Interval Between Frames (seconds) >> "))
    if args[0] == "create":
        args[3] = int(input("Type Desired Framerate >> "))
    args[4]= getNumberOfFrames(args[1])
    return args


def saveFrame(relPath, index):
    im = ImageGrab.grab()
    dt = datetime.now()
    fname = "frame_{}.png".format(index)
    im.save(relPath+fname, 'png')
    return index+1

    

# Main

args = init()

mode = args[0]
relativePath = args[1]
numberOfFrames = args[4]


if mode == "capture":

    cooldownTime = args[2]
    print("From Now, Every " + str(cooldownTime) + " Seconds a Screenshot Will Be Saved.")
    while True:
        numberOfFrames = saveFrame(relativePath, numberOfFrames)
        time.sleep(args[2])


if mode == "create":
    outFrameRate = int(args[3])
    os.system('ffmpeg -y -framerate 1 -i %s/frame*.png -r 5 -c:v libx264 -pix_fmt yuv420p %s/timelapse.mp4' % (relativePath, outFrameRate, relativePath))