import unittest

from stats import (
    parse_record,
    read_valid,
    average_by_city,
    warmest_city,
)


class TestStats(unittest.TestCase):
    def test_parse_record(self):
        record = parse_record("Азов;24.5;2026-07-01")
        self.assertEqual(record["city"], "Азов")
        self.assertEqual(record["temperature"], 24.5)

    def test_invalid_record(self):
        with self.assertRaises(ValueError):
            parse_record("мусор")

    def test_read_valid_skips_bad_lines(self):
        records = read_valid([
            "Азов;24.5;2026-07-01",
            "",
            "мусор",
        ])
        self.assertEqual(len(records), 1)

    def test_average_by_city(self):
        records = read_valid([
            "Азов;24.5;2026-07-01",
            "Азов;25.5;2026-07-02",
            "Таганрог;30;2026-07-01",
        ])
        self.assertEqual(average_by_city(records)["Азов"], 25.0)

    def test_warmest_city(self):
        records = read_valid([
            "Азов;25;2026-07-01",
            "Таганрог;30;2026-07-01",
        ])
        self.assertEqual(warmest_city(records), "Таганрог")


if __name__ == "__main__":
    unittest.main()