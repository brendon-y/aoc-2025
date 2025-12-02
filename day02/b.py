import sys


def main():
    def check(value):
        rep = str(value)
        length = len(rep)
        for j in range(1, length):
            if length % j == 0:  # we can repeat j characters
                # take the first j characters
                pattern = rep[:j]
                remade = pattern * (length // j)
                if remade == rep:
                    return value
        return 0

    def do(line):
        invalids = 0
        ranges = line.split(",")
        for r in ranges:
            values = r.split("-")
            first: int = int(values[0])
            second: int = int(values[1])
            for i in range(first, second + 1):
                invalids += check(i)
        print(invalids)

    if len(sys.argv) == 1:
        with open("input.txt", "r") as f:
            for line in f:
                do(line)
    else:
        do(str(sys.argv[1]))


main()
