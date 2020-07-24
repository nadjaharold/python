# ABC158-C
import math
a, b = map(int, input().split())
x = -1
for i in range(1, 1001):
    if int(i * 0.08) == a and int(i * 0.1) == b:
        x = i
        break
print(x)

a, b = map(int, input().split())

x = math.floor(a / 8 * 100)
y = math.floor(b / 10 * 100)

print(x)
print(y)
