#!/usr/bin/env python

##
# Usage:
# btdoo.py [bluetooth address] somescript.sh
#
# This script will try to detect the specified bluetooth device
# and when it does then the specfied script is run.

from sys import argv
from time import sleep
import subprocess
import bluetooth

def runAction(script):
    subprocess.call(script)

def getArgs():
    return argv[1], argv[2:]

def isAvailable(btAddr):
    btName = bluetooth.lookup_name(btAddr)
    if btName:
        return True
    else:
        return False

def detect():
    device, script = getArgs()
    while True:
        if  isAvailable(device):
            print("Is detected")
            runAction(script)
            sleep(60)
        else:
            print("Not detected")
            sleep(10)


if __name__ == "__main__":
    detect()

