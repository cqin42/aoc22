f = open("input.txt", "r")
l = []
somme = 0
for e in f:
    if e == "\n":
        l.append(somme)
        somme = 0
    else:
        somme += int(e)

l = sorted(l, reverse=True)
print(sum(l[i] for i in range(3)))
