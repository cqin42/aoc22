f = open("input.txt", "r")
d = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Lose",
    "Y": "Draw",
    "Z": "Win",
}
game = {"Rock": "Scissors", "Scissors": "Paper", "Paper": "Rock"}
point = {"Rock": 1, "Paper": 2, "Scissors": 3}

t = 0
for e in f:
    tmp = e.split()
    if d[tmp[1]] == "Lose":
        t += point[game[d[tmp[0]]]] + 0
    elif d[tmp[1]] == "Draw":
        t += point[d[tmp[0]]] + 3
    else:
        t += point[game[game[d[tmp[0]]]]] + 6
    # part1
# if game[d[tmp[1]]] == d[tmp[0]]:
#     t += point[d[tmp[1]]] + 6
# elif d[tmp[0]] == d[tmp[1]]:
#     t += point[d[tmp[1]]] + 3
# else:
#     t += point[d[tmp[1]]] + 0
print(t)
