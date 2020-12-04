def load():
    with open("input.txt", "r") as f:
        return [line.strip() for line in f.readlines()]


def part_1():
    lines = load()
    valid_passwords = 0

    for line in lines:
        interval, key, password = line.split()
        min_, max_ = interval.split("-")
        min_, max_ = int(min_), int(max_)
        key = key.rstrip(":")
        count = 0
        for letter in password:
            if letter == key:
                count += 1
        if min_ <= count <= max_:
            valid_passwords += 1

    print(f"Number of valid passwords: {valid_passwords}")


def part_2():
    lines = load()
    valid_passwords = 0

    for ctr, line in enumerate(lines):
        positions, key, password = line.split()
        first, second = positions.split("-")
        first, second = int(first), int(second)
        key = key.rstrip(":")
        first_matches = False
        second_matches = False
        for idx, letter in enumerate(password, start=1):
            if idx == first:
                first_matches = letter == key
            if idx == second:
                second_matches = letter == key

        if first_matches ^ second_matches:
            valid_passwords += 1

    print(f"Number of valid passwords: {valid_passwords}")


if __name__ == "__main__":
    print("Part 1")
    part_1()
    print("Part 2")
    part_2()
