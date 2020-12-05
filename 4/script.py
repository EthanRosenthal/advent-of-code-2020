import re


def load():
    with open("input.txt", "r") as f:
        return [line.strip() for line in f.readlines()]


def part_1():
    lines = load()
    required_fields = {
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
        # cid is not required
        # "cid"
    }
    num_valid_passports = 0
    fields_seen = set()
    for line in lines:
        if not line:
            # Done parsing this passport.
            # Check for all required fields.
            if fields_seen & required_fields == required_fields:
                num_valid_passports += 1
            fields_seen = set()
            continue
        items = line.split()
        for item in items:
            field, value = item.split(":")
            fields_seen.update([field])
    # If the last line is not an empty line, then
    # we need to handle the last passport
    if line:
        if fields_seen & required_fields == required_fields:
            num_valid_passports += 1
    return num_valid_passports


def parse_byr(val: str) -> bool:
    try:
        val = int(val)
    except:
        # Not an integer
        return False
    return 1920 <= val <= 2002


def parse_iyr(val: str) -> bool:
    try:
        val = int(val)
    except:
        return False
    return 2010 <= val <= 2020


def parse_eyr(val: str) -> bool:
    try:
        val = int(val)
    except:
        return False
    return 2020 <= val <= 2030


def parse_hgt(val: str) -> bool:
    try:
        val, units = val[:-2], val[-2:]
    except IndexError:
        return False
    try:
        val = int(val)
    except:
        return False
    if units == "cm":
        return 150 <= val <= 193
    if units == "in":
        return 59 <= val <= 76
    # Unknown units
    return False


def parse_hcl(val: str) -> bool:
    try:
        hash_, hex_ = val[0], val[1:]
    except IndexError:
        return False
    if hash_ != "#":
        return False
    if len(hex_) != 6:
        return False
    return bool(re.match(r"([a-z]|[0-9])*", hex_))


def parse_ecl(val: str) -> bool:
    valid_colors = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
    return val in valid_colors


def parse_pid(val: str) -> bool:
    return len(val) == 9 and val.isdigit()


def part_2():
    lines = load()
    parse_map = {
        "byr": parse_byr,
        "iyr": parse_iyr,
        "eyr": parse_eyr,
        "hgt": parse_hgt,
        "hcl": parse_hcl,
        "ecl": parse_ecl,
        "pid": parse_pid,
        # cid is not required
        # "cid"
    }

    required_fields = set(parse_map.keys())
    num_valid_passports = 0
    valid_fields_seen = set()

    for line in lines:
        if not line:
            # Done parsing this passport.
            # Check for all required fields.
            if valid_fields_seen & required_fields == required_fields:
                num_valid_passports += 1
            valid_fields_seen = set()
            continue
        items = line.split()
        for item in items:
            field, value = item.split(":")
            parse_func = parse_map.get(field)
            if parse_func is None:
                # Does not count towards a valid field
                continue
            if parse_func(value):
                valid_fields_seen.update([field])

    # If the last line is not an empty line, then
    # we need to handle the last passport
    if line:
        if valid_fields_seen & required_fields == required_fields:
            num_valid_passports += 1
    return num_valid_passports


if __name__ == "__main__":
    print("Part 1")
    num_valid_passports = part_1()
    print(f"Number of valid passports: {num_valid_passports}")

    print("Part 2")
    num_valid_passports = part_2()
    print(f"Number of valid passports: {num_valid_passports}")
