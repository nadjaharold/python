# ABC156-B
a, b = map(int, input().split())


def Base_10_to_n(X, n):
    if (int(X / n)):
        return Base_10_to_n(int(X / n), n) + str(X % n)
    return str(X % n)


a = Base_10_to_n(a, b)
print(len(a))
# (参考)http://iatlex.com/python/base_change

# # aの除算可能な回数を計測することでも桁数はわかるよ
# a, b = map(int, input().split())
# c = 0
# while a > 0:
#     a //= b
#     c += 1
# print(c)
