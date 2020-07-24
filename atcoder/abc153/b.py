# ABC153-B
h, n = map(int, input().split())
a = list(map(int, input().split()))
if (sum(a) >= h):
    print('Yes')
else:
    print('No')
# if文はコンパクトにまとめましょう
print("Yes"if sum(a) >= h else "No")
