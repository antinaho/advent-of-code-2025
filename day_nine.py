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

    c = 0
    lines = I.splitlines()

    reds = set()
    greens = set()
    yellow = set()
    start_x, start_y = list(map(int, lines[0].split(",")))

    def F(point1, point2):
        if point1[0] == point2[0]:
            if point1[1] < point2[1]:
                return "DOWN"
            return "UP"
                
        else:
            if point1[0] < point2[0]:
                return "LEFT"
            return "RIGHT" 

    dir = "UP"
    while c < len(lines):
        x, y = list(map(int, lines[c].split(",")))
        reds.add((x, y))

        if c == len(lines) - 1:
            x_next, y_next = start_x, start_y
        else:
            x_next, y_next = list(map(int, lines[c + 1].split(",")))

        dir = F((x, y), (x_next, y_next))

        if x == x_next:
            for dif in range(min(y, y_next), max(y, y_next) + 1):
                greens.add((x, dif))
                if dir == "UP":
                    yellow.add((x - 1, dif))
                else:
                    yellow.add((x + 1, dif))
        elif y == y_next:
            for dif in range(min(x, x_next), max(x, x_next) + 1):
                greens.add((dif, y))
                if dir == "RIGHT":
                    yellow.add((dif, y + 1))
                else:
                    yellow.add((dif, y - 1))
        c += 1

    

    # for y in range(ymin - 1, ymax + 2):
    #     s = ""
    #     for x in range(xmin - 2, xmax + 2):
    #         if (x, y) in reds:
    #             s += "#"
    #         elif (x, y) in greens:
    #             s += "X"
    #         elif (x, y) in yellow:
    #             s += "@"
    #         else:
    #             s += "."
    #     print(s)

    # print(len(reds))
    # print(len(greens))

    greens = greens.union(reds)
    yellow.difference_update(greens)
    print(len(yellow))
    areas.sort(key=lambda a: a[2])
    
    for n, (i, j, a) in enumerate(areas):


        p1 = tuple(coords[i])
        p2 = tuple(coords[j])
        p3 = (p1[0], p2[1])
        p4 = (p2[0], p1[1])

        min_x, max_x = min(p1[0], p4[0]), max(p1[0], p4[0])
        y = p1[1]
        hit = False
        for x in range(min_x, max_x + 1):
            if (x, y) in yellow:
                hit = True
                break
        if hit:
            continue

        min_x, max_x = min(p3[0], p2[0]), max(p3[0], p2[0])
        y = p2[1]
        hit = False
        for x in range(min_x, max_x + 1):
            if (x, y) in yellow:
                hit = True
                break
        if hit:
            continue

        min_y, max_y = min(p1[1], p3[1]), max(p1[1], p3[1])
        x = p1[0]
        hit = False
        for y in range(min_y, max_y + 1):
            if (x, y) in yellow:
                hit = True
                break
        if hit:
            continue

        
        min_y, max_y = min(p2[1], p4[1]), max(p2[1], p4[1])
        x = p1[0]
        hit = False
        for y in range(min_y, max_y + 1):
            if (x, y) in yellow:
                hit = True
                break
        if hit:
            continue


        print(a)

        # #  p1   p4
        # #
        # #  p3   p2


        

        





        # # p1 <-> p4
        # y = p1[1]
        # passes = 0
        # was_in = False
        # in_ = False
        # s, e = -1, -1

        # for x in range(min(p1[0], p4[0]) - 2, max(p1[0], p4[0]) + 2):
        #     if not in_ and (x, y) in greens:
        #         in_ = True
        #     elif in_ and (x, y) not in greens:
        #         in_ = False

        #     if was_in and not in_:
        #         passes += 1

        #     was_in = in_

        #     if (x, y) == p4:
        #         s = passes
        #     if (x, y) == p1:
        #         e = passes

        #     if e != -1 and s != -1:
        #         break
        # if s != e:
        #     continue

        

        # # p3 <-> p2
        # y = p2[1]
        # passes = 0
        # in_ = False
        # was_in = False
        # s, e = -1, -1
        # for x in range(min(p3[0], p2[0]) - 2, max(p3[0], p2[0]) + 2):

        #     if not in_ and (x, y) in greens:
        #         in_ = True
        #     elif in_ and (x, y) not in greens:
        #         in_ = False

        #     if was_in and not in_:
        #         passes += 1

        #     was_in = in_
        #     if (x, y) == p3:
        #         s = passes
        #     if (x, y) == p2:
        #         e = passes
 
        #     if e != -1 and s != -1:
        #         break
        # if s != e:
        #     continue

    
        # # p1 v^ p3
        # x = p1[0]
        # passes = 0
        # in_ = False
        # was_in = False
        # s, e = -1, -1
        # for y in range(min(p1[1], p3[1]) - 2, max(p1[1], p3[1]) + 2):

        #     if not in_ and (x, y) in greens:
        #         in_ = True
        #     elif in_ and (x, y) not in greens:
        #         in_ = False

        #     if not was_in and in_:
        #         passes += 1

        #     was_in = in_

        #     if (x, y) == p3:
        #         s = passes
        #     if (x, y) == p1:
        #         e = passes
            
        #     if e != -1 and s != -1:
        #         break

        # if s != e:
        #     #print("Not in", p3)
        #     continue
        
    
        # # p4 v^ p2
        # x = p2[0]
        # passes = 0
        # in_ = False
        # was_in = False
        # s, e = -1, -1
        # for y in range(min(p2[1], p4[1]) - 2, max(p2[1], p4[1]) + 2):
 
        #     if not in_ and (x, y) in greens:
        #         in_ = True
        #     elif in_ and (x, y) not in greens:
        #         in_ = False

        #     if not was_in and in_:
        #         passes += 1

        #     was_in = in_

        #     if (x, y) == p4:
        #         s = passes
        #     if (x, y) == p2:
        #         e = passes
            
        #     if e != -1 and s != -1:
        #         break

        
        # if s != e:
        #     #print(p1, p2, p3, p4, s, e, a)
        #     continue

        # print(a)
        # break
        
    
    # for y in range(ymin, ymax + 1):
    #     s = ""
    #     for x in range(xmin, xmax + 1):
    #         if (x, y) in reds:
    #             s += "#"
    #         elif (x, y) in greens:
    #             s += "X"
    #         elif (x, y) in yellows:
    #             s += "@"
    #         else:
    #             s += "."
    #     print(s)
    



