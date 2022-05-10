#AUTHOR: Cole Horvat
# EVALUATE IF ANY OF THE STRINGS IN THE READ FILE EQUAL THE GIVEN KEY
def evalString(key, readF, writeF):
    for i in readF:
        testString = i
        wordList = testString.split(" ")

        for j in wordList:
            j.lower()
            if j == key:
                j.upper()
                finalString = " ".join(wordList)
                writeF.write(finalString + "\n")
    readFile.seek(0)

# GET USER KEYWORD
userSynonyms = []
userKeyword = input("What keyword are you searching? ")
userKeyword = userKeyword.lower()

# GET READ AND WRITE FILE
while True:
    try:
        readFileName = input("Enter the name of the file you want to read from: ")
        readFile = open(readFileName, "r")

        writeFileName = input("Enter the name of the file you want to write the data to: ")
        writeFile = open(writeFileName, "w")

    except:
        print("Error occurred. Please try again")
    break

# WRITE KEYWORD SECTION TO FILE
writeFile.write("KEYWORD: " + userKeyword.upper() + "\n\n")
