import os
import pyAesCrypt
import io


def crypter(filename):
    #шифрует
    password = 'bbbo-02-21'
    buffer = 512 * 1024
    pyAesCrypt.encryptFile(filename,'logenc.txt',password,buffer)
    os.remove(filename)

def decrypter(filename):
    #Дешифрует
    password = 'bbbo-02-21'
    buffer = 512 * 1024
    pyAesCrypt.decryptFile(filename,'yric.py',password,buffer)

def MemoryCrypter(filename,is_encrypted):
    sequence_bytes = io.BytesIO()
    bufferSize = 64 * 1024
    password = "yurayadamvjopueslipoluchitsya"
    with open(filename,"rb") as f:
        file_content = io.BytesIO(f.read())
        
    with open(filename,"wb") as f:
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

MemoryCrypter("yric.py",False)
    