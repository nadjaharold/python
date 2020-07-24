# ABC149-B
a, b, k = map(int, input().split())
while(k > 0):
    if (a > 0):
        a -= 1
        k -= 1
    elif (b > 0):
        b -= 1
        k -= 1
    else:
        k -= 1
print("%s %s" % (a, b))
a, b, k = map(int, input().split())
print(max(a - k, 0), max(b - max(k - a, 0), 0))
