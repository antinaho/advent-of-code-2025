import sys

if __name__ == "__main__":
    I = sys.stdin.read()

    # Star 1
    rotation = 50
    password = 0

    for line in I.splitlines():
        direction = str(line[0])
        amount = int(line[1:])
        if direction == "R":
            rotation += amount
        else:
            rotation -= amount

        rotation = rotation % 100
        if rotation == 0:
            password += 1

    print(password)

    # Star 2
    rotation = 50
    password = 0

    for line in I.splitlines():
        direction = str(line[0])
        amount = int(line[1:])

        for _ in range(amount):
            if direction == "R":
                rotation = (rotation + 1) % 100
            else:
                rotation = (rotation - 1) % 100
            if rotation == 0:
                password += 1

    print(password)
