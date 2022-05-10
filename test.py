import pathlib

from tester import DEBUG,INFO,ERROR
import pyAesCrypt
import io

DEBUG('debug')
DEBUG('blyat')
DEBUG('blyat')
DEBUG('blad')
DEBUG('debug')
DEBUG('blyat')
DEBUG('blyat')
DEBUG('blad')
DEBUG('debug')
DEBUG('blyat')
DEBUG('blyat')
DEBUG('blad')


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