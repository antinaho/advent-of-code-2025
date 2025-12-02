import sys

if __name__ == "__main__":
    I = sys.stdin.read()
    ranges = I.split(",")

    # Star 1
    ans = 0
    for r in ranges:
        start = r.split("-")[0]
        end = r.split("-")[1]

        for n in range(int(start), int(end) + 1):
            str_n = str(n)
            if str_n[len(str_n) // 2 :] == str_n[: len(str_n) // 2]:
                ans += n

    print(ans)

    # Star 2
    ans = 0
    for r in ranges:
        start = r.split("-")[0]
        end = r.split("-")[1]

        for n in range(int(start), int(end) + 1):
            ns = str(n)
            max_segments = len(str(n)) // 2
            f = False
            for i in range(1, max_segments + 1):
                if len(ns) % i == 0:
                    si = i
                    prev = ns[0:i]
                    while si <= len(ns):
                        if prev != ns[si : si + i]:
                            break

                        prev = ns[si : si + i]
                        si += i
                    if si >= len(ns):
                        f = True
            if f:
                ans += n
    print(ans)
