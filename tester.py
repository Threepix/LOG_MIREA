import os
import sys
import datetime

class DEBUG:
    def __init__(self,message):
        level = "DEBUG"
        vremya = str(datetime.datetime.now())
        stw  ="[" + vremya + ": " + level + "]" +" "+message+"\n"
        try:
            my_file = open("log.txt", "a")
            my_file.write(stw)
            my_file.close()
        except Exception:
            my_file = open("log.txt", "w+")
            my_file.write(stw)
            my_file.close()
        print(stw)

class INFO:
    def __init__(self,message):
        level = "INFO"
        vremya = str(datetime.datetime.now())
        stw = "[" + vremya + ": " + level + "]" +" "+message+"\n"
        try:
            my_file = open("log.txt", "a")
            my_file.write(stw)
            my_file.close()
        except Exception:
            my_file = open("log.txt", "w+")
            my_file.write(stw)
            my_file.close()
        print(stw)

class ERROR:
    def __init__(self,message):
        level = "ERROR"
        vremya = str(datetime.datetime.now())
        stw = "[" + vremya + ": " + level + "]" +" "+message+"\n"
        try:
            my_file = open("log.txt", "a")
            my_file.write(stw)
            my_file.close()
        except Exception:
            my_file = open("log.txt", "w+")
            my_file.write(stw)
            my_file.close()
        print(stw)