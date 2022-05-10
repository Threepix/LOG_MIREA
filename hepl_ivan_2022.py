with open('log.txt') as file:
    array = [row.strip() for row in file]
    word = input()

    for i in array:
        if word in i:
            f = open("gay.txt", "w")
            f.write(str(i))