# ABC155-B
n = int(input())
a = list(map(int, input().split()))
num = 0
count = 0
for item in a:
    if (item % 2 == 0):
        num += 1
        if(item % 3 == 0 or item % 5 == 0):
            count += 1
if(num == count):
    print("APPROVED")
else:
    print("DENIED")

# # こっちの方が綺麗
# n = int(input())
# a = list(map(int, input().split()))


# def ans():
#     for i in range(n):
#         if a[i] % 2 == 0 and (a[i] % 3 != 0 and a[i] % 5 != 0):
#             print('DENIED')
#             return
#     print('APPROVED')


# ans()
