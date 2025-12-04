import sys

if __name__ == "__main__":
    I = sys.stdin.readlines()

    grid = []
    for line in I:
        line = line.strip()
        grid.append(list(line))

    delta = [[-1, 1], [0, 1], [1, 1], [-1, 0], [1, 0], [-1, -1], [0, -1], [1, -1]]

    # Star 1 + 2

    def remove_barrel_from_point(x, y):
        b = 0
        for d in delta:
            xd, yd = x + d[0], y + d[1]
            if xd < 0 or xd >= len(grid[y]) or yd < 0 or yd >= len(grid):
                continue
            if grid[yd][xd] == "@":
                b += 1

        if b < 4:
            return True
        return False

    ans = 0

    while True:
        removed_barrels = []
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == ".":
                    continue

                remove_this = remove_barrel_from_point(x, y)
                if remove_this:
                    removed_barrels.append([x, y])

        ans += len(removed_barrels)
        for point in removed_barrels:
            grid[point[1]][point[0]] = "."

        if len(removed_barrels) == 0:
            break

        # Star 1 uncomment below
        # break

    print(ans)
