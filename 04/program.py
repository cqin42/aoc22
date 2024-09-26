f = open("input.txt", "r").read().splitlines()
lst = []
def p1():
    count = 0
    for e in f:
        tt = e.split(",")
        tmp = tt[0].split("-")
        lst = [j for j in range(int(tmp[0]), int(tmp[1]) + 1)]
        tmp1 = tt[1].split("-")
        lst1 = [j for j in range(int(tmp1[0]), int(tmp1[1]) + 1)]
        count += (
            int(tmp[0]) in lst1
            and int(tmp[1]) in lst1
            or int(tmp1[0]) in lst
            and int(tmp1[1]) in lst
        )
    return count

def p2():
    count = 0
    for e in f:
        tt = e.split(",")
        tmp = tt[0].split("-")
        lst = [j for j in range(int(tmp[0]), int(tmp[1]) + 1)]
        tmp1 = tt[1].split("-")
        lst1 = [j for j in range(int(tmp1[0]), int(tmp1[1]) + 1)]
        # print(set(lst + lst1), len(set(lst + lst1)))
        # print(lst, lst1, (len(lst) + len(lst1)))
        if len(set(lst + lst1)) != (len(lst) + len(lst1)):
            count +=1
    return count

print(p1(),p2())
