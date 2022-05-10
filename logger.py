import os
import sys
import datetime

class DEBUG:
    def __init__(self,message):
        level = "DEBUG"
        vremya = str(datetime.datetime.now())
        print("[" + vremya + ": " + level + "]" +" "+message)

class INFO:
    def __init__(self,message):
        level = "INFO"
        vremya = str(datetime.datetime.now())
        print("[" + vremya + ": " + level + "]" +" "+message)

class ERROR:
    def __init__(self,message):
        level = "ERROR"
        vremya = str(datetime.datetime.now())
        print("[" + vremya + ": " + level + "]" +" "+message)
