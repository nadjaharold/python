# ABC158-B
n, a, b = map(int, input().split())
print(n // (a + b) * a + min(a, n % (a + b)))

# x = [0] * n
# xx = ["1" if b > 0 else 0 for b in x]

# print("0" if a == 0 else a + ((n - (a + b))) % b)
# x = 0
# while(n > a):
#     x += a
#     n -= a
#     if (n > b):
#         n -= b
# if(n - a > 0):
#     x += n - a
# else:
#     x += -(a - n)
# print(x)
# while (n > 0):
#     if (an > 0):
#         an -= 1
#         n -= 1
#     elif (bn > 0):
#         bn -= 1
#         n -= 1
#     else:
#         n -= 1
# x = []
# x += b * an
# n -= an
# x += r * bn
# n -= bn
# y += x
# if():
#     n -= 1

# a, b, k = map(int, input().split())
# while(k > 0):
#     if (a > 0):
#         a -= 1
#         k -= 1
#     elif (b > 0):
#         b -= 1
#         k -= 1
#     else:
#         k -= 1
# print("%s %s" % (a, b))
# a, b, k = map(int, input().split())
# print(max(a - k, 0), max(b - max(k - a, 0), 0))


# print(y.count(b))


# while (len(x.split()) < n):

#     print(x)
# sum = an + bn
# if (an == 0):
#     print("0")
# else:
#     print(an * (n - bn if n - sum < 0 else 1) + (n - sum))

# for i in range(n):
#     if(n < an + bn):
#         x = x + ("b" * an) + ("r" * bn)
#     else:
#         list.pop(blue * an)
#         list.pop(red * bn)
