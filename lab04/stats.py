def parse_record(line: str) -> dict:
    """Разбирает одну строку журнала наблюдений."""
    fields = line.split(";")

    if len(fields) != 3:
        raise ValueError("В строке должно быть ровно три поля")

    city, temp, date = fields
    city = city.strip()
    temp = temp.strip()
    date = date.strip()

    if not city:
        raise ValueError("Не указан город")

    if not date:
        raise ValueError("Не указана дата")

    try:
        temperature = float(temp)
    except ValueError:
        raise ValueError("Температура должна быть числом")

    return {
        "city": city,
        "temperature": temperature,
        "date": date,
    }


def read_valid(lines: list[str]) -> list[dict]:
    """Возвращает корректные записи, пропуская пустые и негодные строки."""
    records = []

    for line in lines:
        if not line.strip():
            continue

        try:
            record = parse_record(line)
        except ValueError:
            continue

        records.append(record)

    return records


def average_by_city(records: list[dict]) -> dict:
    """Вычисляет среднюю температуру каждого города, округляя до десятых."""
    totals = {}
    counts = {}

    for record in records:
        city = record["city"]
        temperature = record["temperature"]

        totals[city] = totals.get(city, 0.0) + temperature
        counts[city] = counts.get(city, 0) + 1

    return {
        city: round(totals[city] / counts[city], 1)
        for city in totals
    }


def warmest_city(records: list[dict]) -> str:
    """Возвращает город с наибольшей средней температурой."""
    if not records:
        return ""

    totals = {}
    counts = {}

    for record in records:
        city = record["city"]
        temperature = record["temperature"]

        totals[city] = totals.get(city, 0.0) + temperature
        counts[city] = counts.get(city, 0) + 1

    return min(
        totals,
        key=lambda city: (-totals[city] / counts[city], city),
    )