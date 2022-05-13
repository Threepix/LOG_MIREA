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


# Четвёртая сортировка по времени убывающая
file = open("log.txt",'r')
lines = file.read().split("\n")
file.close()
file = open("log.txt", "w")
file.write("\n".join(lines[::-1]))
file.close()

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
