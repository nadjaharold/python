import numpy as np
import itertools
import sys
# ABC157-B
a = []
for i in range(3):
    a += list(map(int, input().split()))
n = int(input())
b = []
for i in range(n):
    b.append(int(input()))
x = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7],
     [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
for i in range(8):
    if a[x[i][0] - 1] in b and a[x[i][1] - 1] in b and a[x[i][2] - 1] in b:
        print("Yes")
        sys.exit()
print("No")


a = [input().split() for i in range(3)]
n = int(input())
b = [input().split() for i in range(n)]
x = list(itertools.chain.from_iterable(a))

list1 = [x[0], x[1], x[2]]
list2 = [x[0], x[3], x[6]]
list3 = [x[0], x[4], x[8]]
list4 = [x[1], x[4], x[7]]
list5 = [x[2], x[5], x[8]]
list6 = [x[2], x[4], x[6]]
list7 = [x[3], x[4], x[5]]
list8 = [x[6], x[7], x[8]]

b1 = np.array(b)
x1 = list(itertools.chain.from_iterable(b1))
count = 0

for z in range(8):
    l1 = np.array("list" + "{z}")

    for e1 in l1:
        if any(e1 in e2 for e2 in x1):
            count += 1
        else:
            count = count
if (count == 3):
    print('Yes')
else:
    print('No')


def abc():
    count = 0
    for i in range(8):
        l1 = set(list[i]) & set(b)
        if (len(l1) == 3):
            print("Yes")
            return
        else:
            count += 1

    if (count == 8):
        print("No")


# def abc():
#     count = 0
#     for i in range(8):
#         l1 = set(list1) & set(b)
#         if (len(l1) == 3):
#             print("Yes")
#             return
#         else:
#             count += 1

#     if (count == 8):
#         print("No")


abc()
