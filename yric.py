# первый код сортировка по вводимым значениям
with open('log.log') as file:
    array = [row.strip() for row in file]
    word = input()

    for i in array:
        if word in i:
            print(i)
# Второй код сортировка по времени от n до m часов            
n = int(input())
m = int(input())
with open("log.txt") as file:
    array = [row.rstrip() for row in file]
for line in array:
    while True:
        true_line = line
        time_str = line[22] + line[23]
        time = (sum(map(int, time_str.split())))
        if ((time >= n) and (time <= m)) or (time == n) or (time == m):
            print(true_line)
            break
        else:
            break

# Третий сортировка по времени возрастающая
import datetime
with open('log.txt') as file:
    array = [row.strip() for row in file]
    array = sorted(array, key=lambda x: datetime.datetime.strptime(x['date'], '%Y-%m-%d %H:%M:%S'), reverse=False)
    print(array)

# Четвёртая сортировка по времени убывающая
import datetime
with open('log.txt') as file:
    array = [row.strip() for row in file]
    array = sorted(array, key=lambda x: datetime.datetime.strptime(x['date'], '%Y-%m-%d %H:%M:%S'), reverse=True)
    print(array)

# вывести первые n строк
n = int(input())
with open("log.log", 'r') as f:
    for i in range(n):
        print(f.readline())

# вывести последние n строк
n=int(input())
from collections import deque
with open("log.txt") as f:
    for row in deque(f,n):
        print(row.strip())
