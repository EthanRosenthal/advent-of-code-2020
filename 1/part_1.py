with open("input.txt", "r") as f:
    report = [int(x.strip().rstrip("\n")) for x in f.readlines()]

found = False
for idx, item_a in enumerate(report[:-1], start=1):
    for item_b in report[idx:]:
        the_sum = item_a + item_b
        if the_sum == 2020:
            found = True
            break
    if found:
        break

if found:
    print("Found!")
    print(f"Item A: {item_a}, Item B: {item_b}")
    print(f"Their product: {item_a * item_b}")
else:
    print("No items sum to 2020")

