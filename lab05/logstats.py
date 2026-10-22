
from collections import Counter


VALID_LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR"}


def parse_event(line: str) -> dict:
    parts = line.strip().split(maxsplit=2)

    if len(parts) != 3:
        raise ValueError("Некорректная строка журнала")

    time, level, message = parts

    if level not in VALID_LEVELS or not message:
        raise ValueError("Некорректная строка журнала")

    return {
        "time": time,
        "level": level,
        "message": message,
    }


def count_levels(lines: list[str]) -> dict:
    counts = Counter()

    for line in lines:
        if not line.strip():
            continue

        try:
            event = parse_event(line)
            counts[event["level"]] += 1
        except ValueError:
            counts["BROKEN"] += 1

    return dict(counts)


def top_errors(lines: list[str], n: int) -> list[list]:
    errors = Counter()

    for line in lines:
        if not line.strip():
            continue

        try:
            event = parse_event(line)
            if event["level"] == "ERROR":
                errors[event["message"]] += 1
        except ValueError:
            continue

    return [
        [message, count]
        for message, count in sorted(
            errors.items(), key=lambda item: (-item[1], item[0])
        )[:max(0, n)]
    ]


def format_report(counts: dict, errors: list[list]) -> str:
    lines = ["Отчёт по журналу", ""]

    for level in sorted(counts):
        lines.append(f"{level}: {counts[level]}")

    lines.extend(["", "Частые ошибки:"])

    for message, count in errors:
        lines.append(f"- {message} — {count}")

    return "\n".join(lines) + "\n"
