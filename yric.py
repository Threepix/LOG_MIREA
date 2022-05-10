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

# EVALUATE IF THE USER WANTS TO INPUT SYNONYMS
while True:
    searchSyn = input("Are you looking for synonyms as well? (Y/N) ")

    if searchSyn == "N" or searchSyn == "n":
        print("No synonyms")
        break
    elif searchSyn == "Y" or searchSyn == "y":
        # Get synonyms from user
        while True:
            userSynonym = input("Enter synonym you also want to search (Enter 0 to stop) ")
            userSynonym = userSynonym.lower()

            if userSynonym == "0":
                break
            else:
                userSynonyms.append(userSynonym)

        break
    else:
        print("Input is invalid")

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
evalString(userKeyword, readFile, writeFile)

synString = ", ".join(userSynonyms)

# WRITE SYNONYMS SECTION TO FILE
writeFile.write("\nSYNONYMS: " + synString.upper() + "\n\n")
for k in userSynonyms:
    evalString(k, readFile, writeFile)

readFile.close()
writeFile.close()