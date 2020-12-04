def load():
    with open("input.txt", "r") as f:
        return [line.strip() for line in f.readlines()]


def part_1(x_step, y_step):
    lines = load()
    height = len(lines)
    width = len(lines[0])

    x = 0
    y = 0
    tree_count = 0
    while y < height:
        tree_count += lines[y][x] == "#"
        x = (x + x_step) % width
        y += y_step

    print(f"Number of trees: {tree_count}")
    return tree_count


def part_2():
    step_combos = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    product = 1
    for x_step, y_step in step_combos:
        product *= part_1(x_step, y_step)

    print(f"Product of trees: {product}")


if __name__ == "__main__":
    print("Part 1")
    part_1(3, 1)
    print("Part 2")
    part_2()
