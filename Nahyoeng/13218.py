import sys

sys.stdin = open("input.txt", "r")


def check(input):
    global sol
    if (input - 3 == 0):
        sol += 1
    elif (input - 4 == 0):
        sol += 1
    elif (input - 5 == 0):
        sol += 1
    elif (input - 3 < 0):
        return
    else:
        sol += 1
        check(input - 3)


for i in range(0, int(input())):
    sol = 0
    check(int(input()))

    print("#{:.0f} {:.0f}".format(i + 1, sol))
