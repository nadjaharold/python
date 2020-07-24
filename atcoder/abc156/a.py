# ABC156-A
n, r = map(int, input().split())
if (n >= 10):
    x = r
else:
    x = 100 * (10 - n) + r
print(x)
