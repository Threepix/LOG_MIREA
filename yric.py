# первый код сортировка по вводимым значениям
import datetime
with open('log.txt') as file:
    array = [row.strip() for row in file]
    word = input()

    for i in array:
        if word in i:
            print(i)

# второй сортировка по времени возрастающая
array = sorted(array, key=lambda x: datetime.datetime.strptime(x['date'], '%Y-%m-%d %H:%M:%S'), reverse=False)
print(array)

# второй сортировка по времени убывающая
array = sorted(array, key=lambda x: datetime.datetime.strptime(x['date'], '%Y-%m-%d %H:%M:%S'), reverse=True)
print(array)

# вывести первые n строк
n = int(input())
with open("log.txt", 'r') as f:
    for i in range(n):
        print(f.readline())

# вывести последние n строк
n = int(input())
f_read = open("log.txt", "r")
last_line = f_read.readlines()[-n]
print(last_line)
