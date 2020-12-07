def load():
    with open("input.txt", "r") as f:
        return [line.strip() for line in f.readlines()]


def part_1():
    lines = load()
    unique_questions = set()
    num_yes = 0
    for line in lines:
        if not line:
            num_yes += len(unique_questions)
            unique_questions = set()
            continue
        unique_questions.update(list(line))

    if line:
        num_yes += len(unique_questions)
    return num_yes 


def part_2():
    lines = load()
    yes_questions = None
    num_all_yes = 0

    for line in lines:
        if not line:
            num_all_yes += len(yes_questions)
            yes_questions = None
            continue
        if yes_questions is None:
            yes_questions = set(line)
        else:
            yes_questions = yes_questions & set(line)
    if line:
        num_all_yes += len(yes_questions)
    return num_all_yes 


if __name__ == "__main__":
    print("Part 1")
    num_yes = part_1()
    print(f"Total number of yeses: {num_yes}")
    num_all_yes = part_2()
    print(f"Total number of all yeses: {num_all_yes}")
