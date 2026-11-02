#1
m = int(input())
n = int(input())
for i in range(m, n + 1):
    if i % 17 == 0 or i % 10 == 9 or (i % 3 == 0 and i % 5 == 0):
        print(i)

#2
n = int(input())
for i in range(1, n + 1):
    if 5 <= i <= 9:
        continue
    if 17 <= i <= 37:
        continue
    if 78 <= i <= 87:
        continue
    print(i)

#3
n = int(input())
for i in range(n):
    print(n, n, n)
