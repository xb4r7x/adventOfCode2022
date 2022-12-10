with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

def main():
    print("The solution for part 1 is: {0}".format(part1Solution(lines)))
    print("The solution for part 2 is: {0}".format(part2Solution(lines)))

def pixelState(pixels, x):
    if len(pixels) in range(x - 1,x + 2):
        pixel = "#"
    else:
        pixel = "."
    return pixel

def getSignal(cycle, x):
    if cycle in [20, 60, 100, 140, 180, 220]:
        return cycle * x
    return 0

def part1Solution(lines):
    X = 1
    cycles = 0
    signals = []
    rows = []
    pixels = []
    for idx, line in enumerate(lines):
        line = line.split()
        if line[0] == "addx":
            for i in range(2):
                cycles += 1
                signals.append(getSignal(cycles, X))
                pixels.append(pixelState(pixels, X))
                if len(pixels) == 40:
                    rows.append(pixels.copy())
                    pixels.clear()
            X += int(line[1])
        elif line[0] == "noop":
            cycles += 1
            signals.append(getSignal(cycles, X))
            pixels.append(pixelState(pixels, X))
            if len(pixels) == 40:
                rows.append(pixels.copy())
                pixels.clear()

    string = ""
    for list in rows:
        for char in list:
            string += char
            if len(string) == 40:
                print(string)
                string = ""

    return sum(signals)

def part2Solution(lines):
    
    return 2

if __name__ == "__main__":
    main()
