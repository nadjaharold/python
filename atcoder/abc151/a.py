# # # # # # # # # # # # # # # # # # #ord(A)でAの文字コードを取得、英字を数値として扱える
# ABC151-A
c = str(input())
X = ord(c) + 1
print(chr(X))
# ↓↓
# print(chr(ord(str(input())) + 1))
