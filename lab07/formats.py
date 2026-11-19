import json


def csv_to_records(text: str) -> list[dict]:
    lines = text.splitlines()
    if not lines:
        return []
    headers = lines[0].split(",")
    records = []
    for line in lines[1:]:
        if not line.strip():
            continue
        values = line.split(",")
        record = dict(zip(headers, values))
        records.append(record)
    return records


def parse_value(value: str):
    value = value.strip()
    if value.lower() in ("true", "yes"):
        return True
    if value.lower() in ("false", "no"):
        return False
    try:
        return int(value)
    except ValueError:
        pass
    try:
        return float(value)
    except ValueError:
        pass
    return value


def parse_settings(lines: list[str]) -> dict:
    settings = {}
    current_key = None
    for line in lines:
        line = line.split("#", 1)[0].strip()
        if not line:
            continue
        if line.startswith("- ") and current_key is not None:
            settings[current_key].append(parse_value(line[2:]))
        elif ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            if value == "":
                settings[key] = []
                current_key = key
            else:
                settings[key] = parse_value(value)
                current_key = None
    return settings


def merge_by_key(rows: list[dict], extra: dict, key: str = "id") -> list[dict]:
    records = []
    for row in rows:
        record = extra.get(row.get(key), {}).copy()
        record.update(row)
        records.append(record)
    return records


def records_to_json(records: list[dict]) -> str:
    return json.dumps(records, sort_keys=True, indent=2, ensure_ascii=False)