import sys

if __name__ == "__main__":
    I = sys.stdin.read()

    # Star 1

    coords = [list(map(int, coord.split(","))) for coord in I.splitlines()]
    areas = []
    xmin, ymin, xmax, ymax = 10**20, 10**20, -(10**20), -(10**20)
    reds = set()
    for i, (x1, y1) in enumerate(coords):
        for j, (x2, y2) in enumerate(coords):
            if j > i:
                xmin = min(xmin, min(x1, x2))
                xmax = max(xmax, max(x1, x2))
                ymin = min(ymin, min(y1, y2))
                ymax = max(ymax, max(y1, y2))

                area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)

                reds.add((x1, y1))
                reds.add((x2, y2))

                areas.append((i, j, area))

    areas.sort(key=lambda a: -a[2])
    print(areas[0][2])

    # Star 2

    import collections

    x_ranges = collections.defaultdict(list)
    y_ranges = collections.defaultdict(list)
    c = 0
    lines = I.splitlines()

    reds = set()
    greens = set()
    start_x, start_y = list(map(int, lines[0].split(",")))

    while c < len(lines):
        x, y = list(map(int, lines[c].split(",")))
        reds.add((x, y))

        if c == len(lines) - 1:
            x_next, y_next = start_x, start_y
        else:
            x_next, y_next = list(map(int, lines[c + 1].split(",")))

        if x == x_next:
            for dif in range(min(y, y_next) + 1, max(y, y_next)):
                greens.add((x, dif))

        if y == y_next:
            for dif in range(min(x, x_next) + 1, max(x, x_next)):
                greens.add((dif, y))
        c += 1

    for y in range(ymin, ymax + 1):
        s = ""
        for x in range(xmin, xmax + 1):
            if (x, y) in reds:
                s += "#"
            elif (x, y) in greens:
                s += "X"
            else:
                s += "."
        print(s)

    yellow = set()

    for i, j, a in areas:
        x1, y1 = coords[i]
        x2, y2 = coords[j]

        corner_one = (x1, y2)
        corner_one_x, corner_one_y = corner_one

        corner_two = (x2, y1)
        corner_two_x, corner_two_y = corner_two

        beam1 = ()

        X, Y = (xmin - 1, corner_one_y)
        dx, dy = ((x1 - X) // abs(x1 - X), (y2 - Y) // abs(y2 - Y))

        # Move to point 1
        IN = False
        k = 0
        c = False
        while X != xmax + 1:
            if not IN and ((X, Y) in reds or (X, Y) or greens):
                IN = True
            if (X, Y) not in reds and (X, Y) not in greens:
                k += 1
                IN = False

        k = 0
        while sx != x1:
            if (sx, sy) in greens or (sx, sy) in reds:
                k += 1

        k = 0
        while corner_one_x != x1:
            if (corner_one_x, corner_one_y) in reds or (cx, corner_one_y) in greens:
                k += 1

            cx += dx

        corner = (x2, y1)

        yellow.add((corner1[0], corner1[1]))
        yellow.add((corner2[0], corner2[1]))

        break

    print()
    for y in range(ymin, ymax + 1):
        s = ""
        for x in range(xmin, xmax + 1):
            if (x, y) in yellow:
                s += "@"
            elif (x, y) in reds:
                s += "#"
            elif (x, y) in greens:
                s += "X"
            else:
                s += "."
        print(s)
