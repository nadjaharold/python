# ABC141-A
s = str(input())
i = 0
list = ["Sunny", "Cloudy", "Rainy", "Sunny"]
for item in list:
    if (s == item and i < 3):
        print(list[i + 1])

    i += 1
