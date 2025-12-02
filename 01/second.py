def main():
    def process(line: str, current: int):
        # print(line)
        adjustment = int(line[1:])
        step = -1 if line.startswith("L") else 1
        crossings = 0

        result = current
        for i in range(adjustment):
            result += step
            if result < 0:
                result += 100
            if result > 99:
                result -= 100

            if result == 0:
                crossings += 1

        print(current, result, crossings, line)
        return [result, crossings]

    count: int = 0
    current: int = 50
    with open("input", "r") as f:
        for line in f:
            [updated, crossings] = process(line, current)
            current = updated
            count += crossings

    print(count)


main()
