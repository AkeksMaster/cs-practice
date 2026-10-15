import sys

from stats import average_by_city, read_valid, warmest_city


def main():
    lines = sys.stdin.read().splitlines()
    records = read_valid(lines)

    non_empty_lines = [line for line in lines if line.strip()]
    skipped = len(non_empty_lines) - len(records)

    averages = average_by_city(records)
    city = warmest_city(records)

    print(len(records))
    print(skipped)

    if city:
        print(f"{averages[city]:.1f}")
    else:
        print("0.0")


if __name__ == "__main__":
    main()