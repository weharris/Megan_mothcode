#!/usr/bin/python3

#if we want to run the autofocus process via the command line (which seems to work better?)
import subprocess

'''
cmd = "libcamera-hello -t 10000 --autofocus"
subprocess.call(cmd, shell = True)
#'''


import time
import datetime
computerName = "noname"

import os, platform
if platform.system() == "Windows":
	print(platform.uname().node)
else:
	computerName = os.uname()[1]
	print(os.uname()[1])   # doesnt work on windows


def takePhotowithCMD():

    now = datetime.datetime.now()
    timestamp = now.strftime("%y%m%d%H%M%S")
    print(timestamp)

    usbPath= "/media/pi/Moth_Store2/"
    filename = usbPath+"Focus_Locked_"+computerName+"_"+timestamp+".jpg"

    cmd = "/usr/local/bin/libcamera-still -o "+filename
    subprocess.call(cmd, shell = True)


takePhotowithCMD()


print("took pic")
print("Done")  
