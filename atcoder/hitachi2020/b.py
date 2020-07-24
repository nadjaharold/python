# hitachi2020_b
A, B, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = min(a) + min(b)
for k in range(M):
    x, y, c = map(int, input().split())
    ans = min(ans, ((a[x - 1] + b[y - 1]) - c))
print(ans)

# xyc = list(list(map(int, input().split())) for _ in range(M))
# lc = []
# lx = []
# ly = []

# min_a = min(a)
# min_b = min(b)
# for k in range(M):

#     # lc.append(list(c for x, y, c in xyc))
#     # lx.append(list(x for x, y, c in xyc))
#     # ly.append(list(y for x, y, c in xyc))

#     x, y, c = map(int, input().split())

#     # num_x = lx[0][k]
#     # num_y = ly[0][k]
#     # max_lc = max(list(map(int, max(lc))))
#     # ans = min((min_a + min_b), ((a[num_x - 1] + b[num_y - 1]) - max_lc))

#     ans = min((min_a + min_b), ((a[x - 1] + b[y - 1]) - c))
# print(ans)

# print(min((min_a + min_b),
#           ((a[lx[0]] + b[ly[0]]) - max_l1)))

# print(max(l1))
