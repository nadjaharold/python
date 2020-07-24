# ABC135-A
a, b = map(int, input().split())
k = ((a + b) // 2) if (a + b) % 2 == 0 else 0
print(k if k > 0 else "IMPOSSIBLE")
