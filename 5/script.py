from collections import defaultdict
from math import ceil, floor
from typing import List


def load() -> List[str]:
    with open("input.txt", "r") as f:
        return [line.strip() for line in f.readlines()]


def partition(
    codes: List[str], min_: int, max_: int, lower_key: str, upper_key: str
) -> int:
    """
    Recursively binary partition a range between min_ and max_ based on a
    list of codes saying whether to partition the lower or upper half of the range.
    """
    if len(codes) == 1:
        # We're at the bottom of the recursion.
        # Return the actual value.
        if codes[0] == lower_key:
            return min_
        elif codes[0] == upper_key:
            return max_
        else:
            raise ValueError(f"Unknown codes: {codes}")
    this_code, codes = codes[0], codes[1:]
    if this_code == lower_key:
        return partition(
            codes, min_, min_ + floor((max_ - min_) / 2), lower_key, upper_key
        )
    elif this_code == upper_key:
        return partition(
            codes, min_ + ceil((max_ - min_) / 2), max_, lower_key, upper_key
        )
    else:
        raise ValueError(f"Unknown codes: {codes}")


def part_1() -> int:
    passes = load()
    max_seat_id = -1
    for pass_ in passes:
        row_codes, column_codes = pass_[:7], pass_[7:]
        row = partition(row_codes, 0, 127, "F", "B")
        column = partition(column_codes, 0, 7, "L", "R")
        seat_id = row * 8 + column
        if seat_id > max_seat_id:
            max_seat_id = seat_id
    return max_seat_id


def part_2() -> int:
    # Need to find the only seat missing between 1 and 980
    # where the seats before and after are present.

    MAX_SEAT_ID = 980
    # Start with all seats, and then remove each one that is seen.
    seats_not_seen = set(range(1, MAX_SEAT_ID + 1))
    # Create a map of each seat to its nearest before and after
    # neighbors that have been seen.
    seat_to_neighbors = defaultdict(set)
    passes = load()
    for pass_ in passes:
        row_codes, column_codes = pass_[:7], pass_[7:]
        row = partition(row_codes, 0, 127, "F", "B")
        column = partition(column_codes, 0, 7, "L", "R")
        seat_id = row * 8 + column

        seats_not_seen.remove(seat_id)
        seat_to_neighbors[seat_id - 1].update([seat_id])
        seat_to_neighbors[seat_id + 1].update([seat_id])

    # Our seat must be in one of the seats not seen,
    # both of its neighbors must have been seen,
    # and it cannot have been either the first or last seat.
    possible_seats = [
        seat
        for seat in seats_not_seen
        if len(seat_to_neighbors[seat]) == 2 and 2 <= seat_id <= MAX_SEAT_ID
    ]
    assert (
        len(possible_seats) == 1
    ), f"Multiple seats found for ourself: {possible_seats}"
    return possible_seats[0]


if __name__ == "__main__":
    print("Part 1")
    max_seat_id = part_1()
    print(f"Max seat_id: {max_seat_id}")
    print("Part 2")
    our_seat_id = part_2()
    print(f"Our seat_id: {our_seat_id}")
