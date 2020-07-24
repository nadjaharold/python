# hitachi-A
s = str(input())
x = "hi"
i = 1
count = 0

for i in range(1, 6):
    if(s == x * i):
        count += 1

if(count == 1):
    print("Yes")
else:
    print("No")
