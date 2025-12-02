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
                # print(rep, length)
                if rep[: length // 2] == rep[length // 2 :]:
                    print(rep)
                    invalids.append(i)
        print(sum(invalids))

    if len(sys.argv) == 1:
        with open("input.txt", "r") as f:
            for line in f:
                do(line)
    else:
        do(str(sys.argv[1]))


main()
