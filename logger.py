import os
import pathlib
import datetime
import pyAesCrypt
import io


def MemoryCrypter(filename, is_encrypted):
    sequence_bytes = io.BytesIO()
    bufferSize = 64 * 1024
    password = "yurayadamvjopueslipoluchitsya"

#True-зашифровать
#False-расшифровать

    with open(filename, "rb") as f:
        file_content = io.BytesIO(f.read())

    with open(filename, "wb") as f:
        if is_encrypted:
            pyAesCrypt.encryptStream(
                file_content,
                sequence_bytes,
                password,
                bufferSize
            )
        else:
            pyAesCrypt.decryptStream(
                file_content,
                sequence_bytes,
                password,
                bufferSize,
                len(file_content.getvalue())
            )
        f.write(sequence_bytes.getvalue())


class DEBUG:
    def __init__(self,message):
        level = "DEBUG"
        vremya = str(datetime.datetime.now())
        stw ="[" + vremya + ": " + level + "]" +" "+message+"\n"
        path = pathlib.Path('log.txt')
        if path.exists() == True:
            MemoryCrypter("log.txt", False)
            my_file = open("log.txt", "a")
            my_file.write(stw)
            my_file.close()
            MemoryCrypter("log.txt", True)
        else:
            my_file = open("log.txt", "w+")
            my_file.write(stw)
            my_file.close()
            MemoryCrypter("log.txt",True)
        print(stw)

class INFO:
    def __init__(self,message):
        level = "INFO"
        vremya = str(datetime.datetime.now())
        stw = "[" + vremya + ": " + level + "]" +" "+message+"\n"
        path = pathlib.Path('log.txt')
        if path.exists()==True:
            MemoryCrypter("log.txt", False)
            my_file = open("log.txt", "a")
            my_file.write(stw)
            my_file.close()
            MemoryCrypter("log.txt", True)
        else:
            my_file = open("log.txt", "w+")
            my_file.write(stw)
            my_file.close()
            MemoryCrypter("log.txt", True)
        print(stw)

class ERROR:
    def __init__(self,message):
        level = "ERROR"
        vremya = str(datetime.datetime.now())
        stw = "[" + vremya + ": " + level + "]" +" "+message+"\n"
        path = pathlib.Path('log.txt')
        if path.exists() == True:
            MemoryCrypter("log.txt", False)
            my_file = open("log.txt", "a")
            my_file.write(stw)
            my_file.close()
            MemoryCrypter("log.txt", True)
        else:
            my_file = open("log.txt", "w+")
            my_file.write(stw)
            my_file.close()
            MemoryCrypter("log.txt", True)
        print(stw)
        
 """class CREATE_pdf:
    def __init__(self,N):
        pass
        with open('log.txt') as file:
            array = [row.strip() for row in file]
        word = input()
        for i in array:
            for word in i:
                f = open("gay.txt", "w+")
        f.write(i)"""
