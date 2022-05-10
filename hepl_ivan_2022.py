with open('log.txt') as file:
    array = [row.strip() for row in file]
    word = input()

    for i in array:
        for word in i:
            f = open("gay.txt", "w+")
            f.write(i)