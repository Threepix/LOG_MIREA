import pathlib
import datetime
import threading
import pyAesCrypt
import io
import schedule

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

def create():
    path = pathlib.Path('log.log')
    if path.exists() == True:
        MemoryCrypter("log.log", False)
        with open('log.log') as file:
            array = [row.strip() for row in file]
        word = "ERROR"
        path = pathlib.Path('gay.log')
        if path.exists() == True:
            for i in array:
                for word in i:
                    f = open("gay.log", "a")
            f.write(i)
            MemoryCrypter("log.log",True)
        else:
            for i in array:
                for word in i:
                    f = open("gay.log", "w+")
            f.write(i+"\n")
            MemoryCrypter("log.log", True)
def thr():
    while True:
        schedule.run_pending()

class DEBUG:
    def __init__(self,message):
        level = "DEBUG"
        vremya = str(datetime.datetime.now())
        stw ="['date' : " + vremya + ": " + level + "]" +" "+message+"\n"
        path = pathlib.Path('log.log')
        if path.exists() == True:
            MemoryCrypter("log.log", False)
            my_file = open("log.log", "a")
            my_file.write(stw)
            my_file.close()
            MemoryCrypter("log.log", True)
        else:
            my_file = open("log.log", "w+")
            my_file.write(stw)
            my_file.close()
            MemoryCrypter("log.log",True)
        print(stw)

class INFO:
    def __init__(self,message):
        level = "INFO"
        vremya = str(datetime.datetime.now())
        stw = "['date' : " + vremya + ": " + level + "]" +" "+message+"\n"
        path = pathlib.Path('log.log')
        if path.exists()==True:
            MemoryCrypter("log.log", False)
            my_file = open("log.log", "a")
            my_file.write(stw)
            my_file.close()
            MemoryCrypter("log.log", True)
        else:
            my_file = open("log.log", "w+")
            my_file.write(stw)
            my_file.close()
            MemoryCrypter("log.log", True)
        print(stw)

class ERROR:
    def __init__(self,message):
        level = "ERROR"
        vremya = str(datetime.datetime.now())
        stw = "['date' : " + vremya + ": " + level + "]" +" "+message+"\n"
        path = pathlib.Path('log.log')
        if path.exists() == True:
            MemoryCrypter("log.log", False)
            my_file = open("log.log", "a")
            my_file.write(stw)
            my_file.close()
            MemoryCrypter("log.log", True)
        else:
            my_file = open("log.log", "w+")
            my_file.write(stw)
            my_file.close()
            MemoryCrypter("log.log", True)
        print(stw)

class CREATE_pdf:
    def __init__(self,N):
        blyadina = N
        schedule.every(blyadina).minutes.do(create)
        threading.Thread(target=thr).start()

class SORTBY:
    def __init__(self,mod):
        print("mods: sort_by_level sort_by_time up_time down_time first_n last_n")
        if mod =="sort_by_level":
            path = pathlib.Path('log.log')
            if path.exists() == True:
                MemoryCrypter("log.log", False)
                with open('log.log') as file:
                    array = [row.strip() for row in file]
                    print("vvedite level\n")
                    word = input()
                    for i in array:
                        if word in i:
                            print(i)
                file.close()
                MemoryCrypter("log.log", True)

        if mod =="sort_by_time":
            path = pathlib.Path('log.log')
            if path.exists() == True:
                path = pathlib.Path('log.log')
                if path.exists() == True:
                    MemoryCrypter("log.log", False)
                    print("vvedite n\n")
                    n = int(input())
                    print("vvedite m\n")
                    m = int(input())
                    file = open('log.log', "r")
                    for line in file:
                        while True:
                            true_line = line
                            time_str = line[21] + line[22]
                            time = (sum(map(int, time_str.split())))
                            if ((time >= n) and (time <= m)) or (time == n) or (time == m):
                                print(true_line)
                                #закрыть и шифрануть файл
                                break
                            else:
                                #как зашифровать ебаный файл
                                break

        if mod =="up_time":
            path = pathlib.Path('log.log')
            if path.exists() == True:
                path = pathlib.Path('log.log')
                if path.exists() == True:
                    MemoryCrypter("log.log", False)
                    with open('log.log') as file:
                        array = [row.strip() for row in file]
                        array = sorted(array, key=lambda x: datetime.datetime.strptime(x['date'], '%Y-%m-%d %H:%M:%S'),
                                   reverse=False)
                        print(array)
                    file.close()
                    MemoryCrypter("log.log", True)

        if mod =="down_time":
            path = pathlib.Path('log.log')
            if path.exists() == True:
                path = pathlib.Path('log.log')
                if path.exists() == True:
                    MemoryCrypter("log.log", False)
                    with open('log.log') as file:
                        array = [row.strip() for row in file]
                        array = sorted(array, key=lambda x: datetime.datetime.strptime(x['date'], '%Y-%m-%d %H:%M:%S'),
                                   reverse=True)
                        print(array)
                    file.close()
                    MemoryCrypter("log.log", True)

        if mod =="first_n":
            path = pathlib.Path('log.log')
            if path.exists() == True:
                path = pathlib.Path('log.log')
                if path.exists() == True:
                    MemoryCrypter("log.log", False)
                    print("input n")
                    n = int(input())
                    with open("log.log", 'r') as f:
                        for i in range(n):
                            print(f.readline())
                    f.close()
                    MemoryCrypter("log.log", True)

        if mod =="last_n":
            path = pathlib.Path('log.log')
            if path.exists() == True:
                path = pathlib.Path('log.log')
                if path.exists() == True:
                    MemoryCrypter("log.log", False)
                    print("input n")
                    n = int(input())
                    f_read = open("log.log", "r")
                    last_line = f_read.readlines()[-n]
                    print(last_line)
                    f_read.close()
                    MemoryCrypter("log.log", True)
