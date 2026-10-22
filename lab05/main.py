
from pathlib import Path

from logstats import count_levels, top_errors, format_report


def main():
    filename = input().strip()
    folder = Path(__file__).resolve().parent
    log_path = folder / filename
    report_path = folder / "report.txt"

    total = 0
    error_count = 0
    broken_count = 0

    with open(log_path, encoding="utf-8") as log:
        counts = count_levels(log)

    total = sum(counts.values())
    error_count = counts.get("ERROR", 0)
    broken_count = counts.get("BROKEN", 0)

    with open(log_path, encoding="utf-8") as log:
        errors = top_errors(log, 10)

    print(total)
    print(error_count)
    print(broken_count)

    report = format_report(counts, errors)

    with open(report_path, "w", encoding="utf-8") as output:
        output.write(report)


if __name__ == "__main__":
    main()
