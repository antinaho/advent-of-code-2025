import sys

if __name__ == "__main__":
    I = sys.stdin.readlines()

    ingredients_i = 0
    ranges = []
    ingredients = []
    passed = False
    for i, line in enumerate(I):
        line = line.strip()
        if passed:
            ingredients.append(int(line))

        else:
            if line == "":
                passed = True
                continue

            start, end = line.split("-")
            ranges.append([int(start), int(end)])

    # Star 1

    ranges.sort(key=lambda x: x[0])
    ingredients.sort()

    ans = 0
    r = 0
    for i in ingredients:
        if r >= len(ranges):
            break

        low = ranges[r][0]
        high = ranges[r][1]

        if i < low:
            continue
        elif low <= i <= high:
            ans += 1
            continue

        l = r + 1
        while l < len(ranges):
            if ranges[l][0] > i:
                break

            if ranges[l][0] <= i <= ranges[l][1]:
                r = l
                ans += 1
                break

            l += 1

    print(ranges)
    # print(ingredients)
    print(ans)

    # Star 2

    ranges.sort(key=lambda x: x[0])
    ans = 0
    s = ranges[0][0]
    e = ranges[0][1]

    for r in ranges[1:]:
        low = r[0]
        high = r[1]

        if low > e:
            ans += e - s + 1
            s = low
            e = high

        e = max(e, high)

    ans += e - s + 1

    print(ans)
