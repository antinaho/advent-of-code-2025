import sys

if __name__ == "__main__":

    I = sys.stdin.read()


    parts = I.split("\n\n")

    presents = parts[:-1]
    grid = parts[-1]

    d = {}
    for p in presents:
        num = int(p[0])
        for i in p[1:]:
            if i == "#":
                d[num] = 1 + d.get(num, 0)

    ans = 0
    for j ,g in enumerate(grid.split("\n")):

        config = g.split(" ")
        x, y = config[0].split("x")
        grid_size = int(x) * int(y[:-1])
        present_size = 0
        for i, p in enumerate(config[1:]):
            present_size += d[i] * int(p)

        #print(grid_size, present_size)

        if grid_size < present_size:
            continue

        if grid_size - present_size <= 200:
            print(grid_size, present_size)

        ans += 1   

    print(ans)
        
            
        