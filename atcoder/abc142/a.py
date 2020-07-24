# ABC142-A
n = int(input())
i = 1
list = []
while(i <= n):
    if (i % 2 == 1):
        list.append(i)
    i += 1
print(len(list) / n)
or
N = int(input())
if N % 2 == 0:
    print(0.5)
else:
    print((N + 1) / 2 / N)
