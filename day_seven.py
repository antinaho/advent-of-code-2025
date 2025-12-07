import sys

if __name__ == "__main__":
    I = sys.stdin.read()

    grid = [list(row) for row in I.splitlines()]

    height = len(grid)
    width = len(grid[0])

    # Star 1

    beams = set()
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if col == "S":
                beams.add((int(x), int(y) + 1))

    ans = 0
    while True:
        new_beams = set()

        for x, y in beams:
            if x < 0 or x == width - 1 or y == height - 1:
                continue

            symbol = grid[y][x]
            if symbol == ".":
                new_beams.add((x, y + 1))
            if symbol == "^":
                new_beams.add((x + 1, y + 1))
                new_beams.add((x - 1, y + 1))

                ans += 1
        beams = new_beams
        # print(ans)

        if len(beams) == 0:
            break

    # print(beams)
    print(ans)

    # Star 2

    beam = []
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if col == "S":
                beam = [(int(x), int(y) + 1, 1)]

    ans = 0
    while True:
        new_beams = []

        for x, y, i in beam:
            if y + 1 >= height:
                ans += i
                continue

            if x < 0 or x == width - 1 or y == height - 1:
                continue

            symbol = grid[y][x]
            if symbol == ".":
                new_beams.append((x, y + 1, i))
            if symbol == "^":
                new_beams.append((x + 1, y + 1, i))
                new_beams.append((x - 1, y + 1, i))

        import collections

        count = collections.defaultdict(int)
        for x, y, i in new_beams:
            count[(x, y)] += i

        beam = []
        for x, y in count.keys():
            beam.append((x, y, count[(x, y)]))

        if len(beam) == 0:
            break

    # print(beams)
    print(ans)
