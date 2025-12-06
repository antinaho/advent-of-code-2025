import sys

if __name__ == "__main__":
    I = sys.stdin.readlines()

    num_line, operations = I[:-1], I[-1]

    import collections

    d = collections.defaultdict(list)

    # Star 1

    for line in num_line:
        line = line.strip()
        num = ""
        j = 0
        for c in line:
            if c == " ":
                if num != "":
                    d[j].append(int(num))
                    num = ""
                    j += 1
                continue
            else:
                num += c
        if num != "":
            d[j].append(int(num))

    ans = 0
    i = 0
    for op in operations:
        if op == "*":
            m = 1
            for n in d[i]:
                m *= n

            ans += m

            i += 1
        elif op == "+":
            m = 0
            for n in d[i]:
                m += n

            ans += m

            i += 1

    print(ans)

    # Star 2

    d = collections.defaultdict(list)
    spaces = set()

    for i, c in enumerate(num_line[0]):
        if c == " ":
            spaces.add(i)

    for line in num_line[1:]:
        secondary = set()
        for i, c in enumerate(line):
            if c == " ":
                secondary.add(i)
        spaces = spaces.intersection(secondary)
    start_end = {-1, len(num_line[0]) - 1}
    spaces = spaces.union(start_end)

    stops = list(spaces)
    stops.sort()

    # print(stops)

    for line in num_line:
        for i, (start, end) in enumerate(zip(stops, stops[1:])):
            chunk = line[start + 1 : end]
            d[i].append([k for k in chunk])

    # print(d)

    ans = 0
    i = 0
    for op in operations:
        if op == "*":
            m = 1
            n = d[i]  # [['1', '2', '3'], [' ', '4', '5'], [' ', ' ', '6']]
            # print(n)
            for j in range(1, len(n[0]) + 1):
                k = ""
                for s in n:
                    if s[-j] == " ":
                        continue

                    k += s[-j]

                # print(k)
                if k != "":
                    m *= int(k)

            # print(m)
            ans += m

            i += 1

        elif op == "+":
            m = 0
            n = d[i]  # [['1', '2', '3'], [' ', '4', '5'], [' ', ' ', '6']]
            # print(n)
            for j in range(1, len(n[0]) + 1):
                k = ""
                for s in n:
                    if s[-j] == " ":
                        continue

                    k += s[-j]

                # print(k)
                if k != "":
                    m += int(k)

            # print(m)
            ans += m

            i += 1

    print(ans)
