import sys


def main():
    def do(line):
        invalids = []
        ranges = line.split(",")
        for r in ranges:
            values = r.split("-")
            first: int = int(values[0])
            second: int = int(values[1])
            for i in range(first, second + 1):
                rep = str(i)
                length = len(rep)
                for j in range(1, length):
                    if length % j == 0:
                        # take the first j characters
                        pattern = rep[:j]
                        remade = pattern * (length // j)
                        if remade == rep:
                            print(i)
                            invalids.append(i)
        print(sum(set(invalids)))  # convert to a set to remove double counts
        # eg. 1111 is 11 11 and 1 1 1 1, but only count it once

    if len(sys.argv) == 1:
        with open("input.txt", "r") as f:
            for line in f:
                do(line)
    else:
        do(str(sys.argv[1]))


main()
