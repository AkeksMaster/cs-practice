def csv_to_records(text: str) -> list[dict]:
    lines = text.splitlines()
    headers = lines[0].split(",")
    records = []
    for line in lines[1:]:
        values = line.split(",")
        record = dict(zip(headers, values))
        records.append(record)
    return records