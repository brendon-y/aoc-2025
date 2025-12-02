def main():
    count: int = 0
    current: int = 50

    def process(line: str):
        adjustment = int(line[1:])
        result = current - adjustment if line.startswith("L") else current + adjustment
        while result > 99:
            result = result - 100
        while result < 0:
            result = result + 100
        return result

    with open("input", "r") as f:
        for line in f:
            current = process(line)
            if current == 0:
                count += 1

    print(count)


main()
