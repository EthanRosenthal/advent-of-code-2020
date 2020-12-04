with open("input.txt", "r") as f:
    report = [int(x.strip().rstrip("\n")) for x in f.readlines()]

found = False
for idx_a, item_a in enumerate(report[:-2], start=1):
    for idx_b, item_b in enumerate(report[idx_a:-1], start=2):
        for item_c in report[idx_b:]:
            the_sum = item_a + item_b + item_c
            if the_sum == 2020:
                found = True
                break
        if found:
            break
    if found:
        break

if found:
    print("Found!")
    print(f"Item A: {item_a}, Item B: {item_b}, Item C: {item_c}")
    print(f"Their product: {item_a * item_b * item_c}")
else:
    print("No items sum to 2020")

