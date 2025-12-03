import sys

if __name__ == "__main__":
    I = sys.stdin.readlines()

    # Star 1

    power = 0
    for line in I:
        line = line.strip()
        a = int(line[0])
        b = int(line[1])
        for i in range(2, len(line)):
            if int(line[i]) > b:
                if b > a:
                    a = b
                b = int(line[i])

            if int(line[i - 1]) > a:
                a = int(line[i - 1])
                b = int(line[i])

        power += 10 * a + b

    print(power)

    # Star 2
    # 2235324222232244322422312234251333343425243363443152244111122632336242225 755555546443
    # 2235324222232244322422312234251333343425243363443152244111122632336242225 745433452452451332445546443

    # 223532422223 <= 2
    #           2
    # 223532422232

    power = 0
    for line in I:
        line = line.strip()
        max_index = -1

        for i in range(12, 0, -1):
            current_index = len(line) - i
            start_value = int(line[current_index])
            j = current_index

            while j > max_index:
                if int(line[j]) >= start_value:
                    start_value = int(line[j])
                    current_index = min(j, current_index)
                j -= 1

            max_index = current_index
            # print(current_index, start_value)
            power += int(line[max_index]) * 10 ** (i - 1)

        print(f"{power:_}")

    print(power)
