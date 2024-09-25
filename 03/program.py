import string

alpha = "_" + string.ascii_lowercase
alpha += string.ascii_uppercase
sum = 0
f = open("input.txt", "r")
ff = f.read().split("\n")
# print(ff)
# part1
# for i in f:
#     idx = len(i) / 2
#     tmp = i[: int(idx)]
#     tmp1 = i[int(idx) :]
#     for j in tmp:
#         if j in tmp1:
#             print(j, alpha.find(j))
#             sum += alpha.find(j)
#             break
d = 0
for i, j, k in zip(ff, ff[1:], ff[2:]):
    if d == 0:
        for e in i:
            if e in j and e in k and e in i:
                sum += alpha.find(e)
                break
        d += 1
    elif d == 2:
        d = 0
    else:
        d += 1

print(sum)
