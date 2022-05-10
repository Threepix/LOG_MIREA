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

"""class CREATE_PDF:
    def __init__(self,n):
        a = datetime.datetime.now()
        while True:
            path = pathlib.Path('log.txt')
            if path.exists() == True:
                if a.hour + int(n) == datetime.datetime.now():
                    MemoryCrypter("log.txt", False)
                    with open('log.txt',"r") as myfile:
                        count = sum(1 for line in myfile)
                        for i in range(count):
                            line = myfile.readline()
                            if line[30]=="D":
                                row = open("otchet.txt", "w+")
                                row.write(line)
                                row.close()
                                myfile.close()
                                MemoryCrypter("log.txt", True)
            else:
                pass

"""