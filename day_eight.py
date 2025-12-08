import sys

if __name__ == "__main__":
    I = sys.stdin.read()

    coords = [list(map(int, line.split(","))) for line in I.splitlines()]

    def dist(point1, point2):
        return (
            (point1[0] - point2[0]) ** 2
            + (point1[1] - point2[1]) ** 2
            + (point1[2] - point2[2]) ** 2
        )

    distances = []

    for i in range(len(coords)):
        for j in range(len(coords)):
            if i == j:
                continue
            distances.append([i, j, dist(coords[i], coords[j])])

    distances.sort(key=lambda x: x[2])

    import collections

    # Star 1

    connections = collections.defaultdict(set)
    cn = 1000

    while cn > 0:
        for i in range(0, len(distances), 2):
            p1, p2, d = distances[i]
            if cn <= 0:
                break

            dupe = False

            modified = False
            p = [-1, -1]
            for k, v in connections.items():
                if p1 in v and p2 in v:
                    dupe = True
                    cn -= 1
                    break

                if p2 not in v and p1 in v:
                    p[0] = k

                if p2 in v and p1 not in v:
                    p[1] = k

            if dupe:
                continue

            if p[0] != -1 and p[1] != -1:
                connections[p[0]] = connections[p[0]].union(connections[p[1]])
                modified = True
                connections.pop(p[1])
                cn -= 1

            elif p[0] == -1 and p[1] != -1:
                connections[p[1]].add(p1)
                modified = True
                cn -= 1
            elif p[0] != -1 and p[1] == -1:
                connections[p[0]].add(p2)
                modified = True
                cn -= 1

            # print(p1, p2, connections)

            if modified:
                # print(p1, p2, coords[p1], coords[p2])
                continue

            # print(p1, p2, coords[p1], coords[p2])
            connections[p1].add(p1)
            connections[p1].add(p2)
            cn -= 1
        break

    # print(connections)

    ans = 1
    biggest_cons = list(connections.values())
    biggest_cons.sort(key=lambda k: -len(k))
    for b in biggest_cons[:3]:
        ans *= len(b)

    print(ans)

    # Star 2
    connections = collections.defaultdict(set)

    while True:
        for i in range(0, len(distances), 2):
            p1, p2, d = distances[i]
            # print(connections)
            # print(p1, p2)
            dupe = False

            modified = False
            p = [-1, -1]
            for k, v in connections.items():
                if p1 in v and p2 in v:
                    dupe = True
                    break

                if p2 not in v and p1 in v:
                    p[0] = k

                if p2 in v and p1 not in v:
                    p[1] = k

            if dupe:
                continue

            if p[0] != -1 and p[1] != -1:
                connections[p[0]] = connections[p[0]].union(connections[p[1]])
                modified = True
                connections.pop(p[1])

                # print(len(connections[p[0]]))
                if len(connections[p[0]]) == len(coords):
                    print(coords[p1][0] * coords[p2][0])
                    assert False

            elif p[0] == -1 and p[1] != -1:
                connections[p[1]].add(p1)

                if len(connections[p[1]]) == len(coords):
                    print(coords[p1][0] * coords[p2][0])
                    assert False

                modified = True
            elif p[0] != -1 and p[1] == -1:
                connections[p[0]].add(p2)

                if len(connections[p[0]]) == len(coords):
                    print(coords[p1][0] * coords[p2][0])
                    assert False

                modified = True

            if modified:
                continue

            connections[p1].add(p1)
            connections[p1].add(p2)

    # 7
    # connections[19]: [19, 0, 7, 14]
    # connections[13]: [13, 2, 8]
    # connections[18] : [18, 17]
    # connections[12] : [12, 9]
    # connections[16] : [16, 11]
