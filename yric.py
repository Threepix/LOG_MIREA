# первый код сортировка по вводимым значениям
import datetime
with open('log.log') as file:
    array = [row.strip() for row in file]
    word = input()

    for i in array:
        if word in i:
            print(i)
# Второй код сортировка по времени от n до m часов            
n = int(input())
m = int(input())
file = open('log.log', "r")
for line in file:
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
array = sorted(array, key=lambda x: datetime.datetime.strptime(x['date'], '%Y-%m-%d %H:%M:%S'), reverse=False)
print(array)

# Четвёртая сортировка по времени убывающая
array = sorted(array, key=lambda x: datetime.datetime.strptime(x['date'], '%Y-%m-%d %H:%M:%S'), reverse=True)
print(array)

# вывести первые n строк
n = int(input())
with open("log.log", 'r') as f:
    for i in range(n):
        print(f.readline())

# вывести последние n строк
n = int(input())
f_read = open("log.log", "r")
last_line = f_read.readlines()[-n]
print(last_line)
