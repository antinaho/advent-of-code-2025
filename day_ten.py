import sys

if __name__ == "__main__":
    I = sys.stdin.readlines()

    ans = 0
    for i, line in enumerate(I):
        # line = line.strip()
        items: list[str] = line.split(" ")

        light = items[0][1:-1]
        target, i = 0, 0
        for d in light[::-1]:
            if d == ".":
                i += 1
            if d == "#":
                target = (1 << i) ^ target
                i += 1

        buttons = items[1:-1]
        masks = []
        for btn in buttons:
            btn = btn[1:-1]

            nums = list(map(int, btn.split(",")))
            mask = 0
            for num in list(map(int, btn.split(","))):
                mask = (1 << len(light) - num - 1) ^ mask

            masks.append(mask)

        joltages = items[-1]

        import collections

        q = collections.deque()

        d = {}
        d[0] = 0
        q.append(0)

        while len(q) > 0:
            current = q.popleft()

            if current == target:
                print(d[target])
                ans += d[target]
                break

            for m in masks:
                if (current ^ m) not in d:
                    d[current ^ m] = d[current] + 1
                    q.append(current ^ m)

    print(ans)

# [....]
# [.##.]
#       (3)   (1,3)  (2)    (2,3)  (0,2)   (0,1)                {3,5,4,7}
#      [...#] [.#.#] [..#.] [..##] [#.#.] [##..]


# [...#.]
#         (0,2,3,4) (2,3)     (0,4)   (0,1,2) (1,2,3,4)                  {7,5,12,7,2}
#           [#.###]  [..##.] [#...#]  [###..] [.####]


# [.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
